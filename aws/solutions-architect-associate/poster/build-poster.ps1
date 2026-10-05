<#
.SYNOPSIS
  Renders the SAA-C03 recall poster to a single-page PDF.

.DESCRIPTION
  Prints poster.html with headless Chrome at the page size declared in the
  file's own @page rule (18 x 24 in portrait). No pandoc step — the poster is
  already a self-contained HTML document.

  Requires Google Chrome or Microsoft Edge.

.EXAMPLE
  .\build-poster.ps1
  .\build-poster.ps1 -Png          # also render a PNG preview
#>
[CmdletBinding()]
param(
    [string] $OutFile = "aws-saa-c03-poster.pdf",
    [switch] $Png
)

$ErrorActionPreference = 'Stop'

$here     = Split-Path -Parent $MyInvocation.MyCommand.Path
$htmlPath = Join-Path $here 'poster.html'
$pdfPath  = Join-Path $here $OutFile

if (-not (Test-Path $htmlPath)) { throw "poster.html not found in $here" }

$browser = $null
foreach ($c in @(
    "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
    "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
    "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe",
    "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe"
)) { if (Test-Path $c) { $browser = $c; break } }
if (-not $browser) { throw "Neither Chrome nor Edge was found; one is needed to print the poster." }

if (Test-Path $pdfPath) { Remove-Item $pdfPath -Force }

$uri     = ([System.Uri]$htmlPath).AbsoluteUri
$profile = Join-Path $env:TEMP ("chrome-poster-" + [guid]::NewGuid().ToString('N').Substring(0,8))

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

# Chrome can return before the file is flushed; wait for a stable size.
$lastSize = -1
for ($i = 0; $i -lt 60; $i++) {
    Start-Sleep -Milliseconds 400
    if (-not (Test-Path $pdfPath)) { continue }
    $size = (Get-Item $pdfPath).Length
    if ($size -gt 0 -and $size -eq $lastSize) { break }
    $lastSize = $size
}
Remove-Item $profile -Recurse -Force -ErrorAction SilentlyContinue

if (-not (Test-Path $pdfPath)) { throw "Chrome did not produce $pdfPath" }

$sizeKb = [math]::Round((Get-Item $pdfPath).Length / 1KB)
Write-Host "Poster written: $pdfPath ($sizeKb KB)" -ForegroundColor Cyan

# Report the page count — the poster must stay on ONE page.
$pages = $null
try {
    $bytes = [System.IO.File]::ReadAllBytes($pdfPath)
    $text  = [System.Text.Encoding]::Latin1.GetString($bytes)
    $pages = ([regex]::Matches($text, '/Type\s*/Page[^s]')).Count
} catch { }

if ($pages) {
    if ($pages -eq 1) {
        Write-Host "Page count: 1 — fits on a single sheet." -ForegroundColor Cyan
    } else {
        Write-Warning "Page count: $pages — content overflows. Reduce the row font size in poster.html."
    }
}

if ($Png) {
    $pngPath = [System.IO.Path]::ChangeExtension($pdfPath, '.png')
    & python -c @"
import fitz, sys
d = fitz.open(r'$pdfPath')
d[0].get_pixmap(dpi=150).save(r'$pngPath')
print('PNG written: $pngPath')
"@
}
