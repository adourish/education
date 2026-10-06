<#
.SYNOPSIS
  Builds the AWS SAA-C03 memorization notes into a single PDF.

.DESCRIPTION
  Combines every markdown file in ..\notes into one HTML document with pandoc,
  then prints that HTML to PDF with headless Chrome.

  Requirements:
    - pandoc on PATH (or at %LOCALAPPDATA%\Pandoc\pandoc.exe)
    - Google Chrome or Microsoft Edge installed

.EXAMPLE
  .\build-pdf.ps1
  .\build-pdf.ps1 -KeepHtml
#>
[CmdletBinding()]
param(
    [string] $OutFile = "aws-saa-c03-memorization-notes.pdf",
    [switch] $KeepHtml
)

$ErrorActionPreference = 'Stop'

$here      = Split-Path -Parent $MyInvocation.MyCommand.Path
$notesDir  = Join-Path (Split-Path -Parent $here) 'notes'
$cssPath   = Join-Path $here 'print.css'
$titlePath = Join-Path $here 'title.html'
$htmlPath  = Join-Path $here 'combined.html'
$pdfPath   = Join-Path $here $OutFile

# --- locate pandoc ---------------------------------------------------------
$pandoc = (Get-Command pandoc -ErrorAction SilentlyContinue).Source
if (-not $pandoc) {
    $candidate = Join-Path $env:LOCALAPPDATA 'Pandoc\pandoc.exe'
    if (Test-Path $candidate) { $pandoc = $candidate }
}
if (-not $pandoc) { throw "pandoc not found. Install it from https://pandoc.org/installing.html" }

# --- locate a Chromium browser --------------------------------------------
$browser = $null
$browserCandidates = @(
    "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
    "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
    "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe",
    "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe"
)
foreach ($c in $browserCandidates) {
    if (Test-Path $c) { $browser = $c; break }
}
if (-not $browser) { throw "Neither Chrome nor Edge was found; one is needed to print the PDF." }

# --- gather the notes in filename order ------------------------------------
$files = Get-ChildItem -Path $notesDir -Filter '*.md' | Sort-Object Name
if ($files.Count -eq 0) { throw "No markdown files found in $notesDir" }

Write-Host "Combining $($files.Count) markdown files..." -ForegroundColor Cyan
foreach ($f in $files) { Write-Host "  $($f.Name)" -ForegroundColor DarkGray }

# --- markdown -> HTML ------------------------------------------------------
$pandocArgs = @(
    '--from=gfm'
    '--to=html5'
    '--standalone'
    '--toc'
    '--toc-depth=2'
    "--css=$cssPath"
    '--embed-resources'
    '--metadata'
    'title=AWS Solutions Architect Associate - Memorization Notes'
    "--include-before-body=$titlePath"
    "--output=$htmlPath"
) + ($files | ForEach-Object { $_.FullName })

& $pandoc @pandocArgs
if ($LASTEXITCODE -ne 0) { throw "pandoc failed with exit code $LASTEXITCODE" }
Write-Host "HTML written: $htmlPath" -ForegroundColor Cyan

# --- HTML -> PDF -----------------------------------------------------------
if (Test-Path $pdfPath) { Remove-Item $pdfPath -Force }

$uri     = ([System.Uri]$htmlPath).AbsoluteUri
$profile = Join-Path $env:TEMP ("chrome-pdf-" + [guid]::NewGuid().ToString('N').Substring(0,8))

& $browser `
    --headless=new `
    --disable-gpu `
    --no-sandbox `
    --no-first-run `
    --no-pdf-header-footer `
    "--user-data-dir=$profile" `
    --run-all-compositor-stages-before-draw `
    --virtual-time-budget=20000 `
    "--print-to-pdf=$pdfPath" `
    $uri 2>$null

# Chrome can return before the PDF is fully flushed to disk, so wait for a
# file whose size has stopped changing.
$lastSize = -1
for ($i = 0; $i -lt 60; $i++) {
    Start-Sleep -Milliseconds 500
    if (-not (Test-Path $pdfPath)) { continue }
    $size = (Get-Item $pdfPath).Length
    if ($size -gt 0 -and $size -eq $lastSize) { break }
    $lastSize = $size
}
Remove-Item $profile -Recurse -Force -ErrorAction SilentlyContinue

if (-not (Test-Path $pdfPath)) { throw "Chrome did not produce $pdfPath" }

$sizeKb = [math]::Round((Get-Item $pdfPath).Length / 1KB)
Write-Host "PDF written: $pdfPath ($sizeKb KB)" -ForegroundColor Cyan

if (-not $KeepHtml) { Remove-Item $htmlPath -Force }
