<#
.SYNOPSIS
  Renders the SAA-C03 recall poster to PDF, in 3-, 2- or 1-column layouts.

.DESCRIPTION
  poster.html is one responsive document. The column count is driven by a
  data-cols attribute on <html>, which this script sets before printing, so the
  same content prints at three sizes:

    3 columns  18 x 24 in   wall or desk poster
    2 columns  12 x 18 in   half size, still pinnable, fits a small frame
    1 columns   5 x 34 in   phone format: narrow, long, read by scrolling

  The HTML also reflows on screen, so opening poster.html on a phone browser
  gives the 1-column layout with no build step at all.

  Requires Google Chrome or Microsoft Edge.

.EXAMPLE
  .\build-poster.ps1                 # all three
  .\build-poster.ps1 -Columns 1      # just the phone one
#>
[CmdletBinding()]
param(
    [ValidateSet('3', '2', '1', 'all')]
    [string] $Columns = 'all'
)

$ErrorActionPreference = 'Stop'

$here     = Split-Path -Parent $MyInvocation.MyCommand.Path
$htmlPath = Join-Path $here 'poster.html'
if (-not (Test-Path $htmlPath)) { throw "poster.html not found in $here" }

$browser = $null
foreach ($c in @(
    "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
    "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
    "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe",
    "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe"
)) { if (Test-Path $c) { $browser = $c; break } }
if (-not $browser) { throw "Neither Chrome nor Edge was found; one is needed to print the poster." }

# cols -> page size (inches) and output name. Page size is injected as an
# @page rule so one HTML file can print at three different sheet sizes.
$variants = @(
    @{ Cols = '3'; W = 18; H = 24; Out = 'aws-saa-c03-poster.pdf';        Label = '3 column - 18x24 in wall poster' }
    @{ Cols = '2'; W = 12; H = 18; Out = 'aws-saa-c03-poster-2col.pdf';   Label = '2 column - 12x18 in half size'   }
    @{ Cols = '1'; W = 5;  H = 34; Out = 'aws-saa-c03-poster-phone.pdf';  Label = '1 column - 5x34 in phone format' }
)
if ($Columns -ne 'all') { $variants = $variants | Where-Object { $_.Cols -eq $Columns } }

$source = Get-Content $htmlPath -Raw

foreach ($v in $variants) {
    $tmpHtml = Join-Path $env:TEMP ("poster-$($v.Cols)col-" + [guid]::NewGuid().ToString('N').Substring(0,6) + ".html")
    $pdfPath = Join-Path $here $v.Out

    # Set the column count, and override the page size for this variant.
    $html = $source -replace '<html lang="en">', ('<html lang="en" data-cols="{0}">' -f $v.Cols)
    $pageRule = '<style>@page {{ size: {0}in {1}in; margin: {2}in; }}</style>' -f `
                 $v.W, $v.H, $(if ($v.Cols -eq '1') { '0.3' } else { '0.42' })
    $html = $html -replace '</head>', "$pageRule`n</head>"
    Set-Content -Path $tmpHtml -Value $html -Encoding utf8

    if (Test-Path $pdfPath) { Remove-Item $pdfPath -Force }

    $uri     = ([System.Uri]$tmpHtml).AbsoluteUri
    $profile = Join-Path $env:TEMP ("chrome-poster-" + [guid]::NewGuid().ToString('N').Substring(0,8))

    & $browser `
        --headless=new --disable-gpu --no-sandbox --no-first-run --no-pdf-header-footer `
        "--user-data-dir=$profile" `
        --run-all-compositor-stages-before-draw `
        --virtual-time-budget=20000 `
        "--print-to-pdf=$pdfPath" `
        $uri 2>$null

    $lastSize = -1
    for ($i = 0; $i -lt 60; $i++) {
        Start-Sleep -Milliseconds 400
        if (-not (Test-Path $pdfPath)) { continue }
        $size = (Get-Item $pdfPath).Length
        if ($size -gt 0 -and $size -eq $lastSize) { break }
        $lastSize = $size
    }
    Remove-Item $profile -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item $tmpHtml -Force -ErrorAction SilentlyContinue

    if (-not (Test-Path $pdfPath)) { throw "Chrome did not produce $pdfPath" }

    $kb = [math]::Round((Get-Item $pdfPath).Length / 1KB)
    # Page count comes from PyMuPDF. Chrome writes its page tree into a
    # compressed object stream, so scanning the raw bytes for /Type /Page or
    # /Count finds nothing - it needs a real PDF parser.
    $pages = 0
    try {
        $out = & python -c "import fitz,sys; print(fitz.open(sys.argv[1]).page_count)" $pdfPath 2>$null
        if ($LASTEXITCODE -eq 0 -and $out) { $pages = [int]($out | Select-Object -First 1) }
    } catch { }

    $note = if (-not $pages) {
        "page count not checked (needs PyMuPDF)"
    } elseif ($v.Cols -eq '1') {
        "$pages pages - scrolling format, several expected"
    } elseif ($pages -eq 1) {
        "1 page - fits on a single sheet"
    } else {
        "WARNING: $pages pages - content overflows, tighten poster.html"
    }

    Write-Host ("{0,-38} {1,6} KB   {2}" -f $v.Label, $kb, $note) -ForegroundColor Cyan
}

Write-Host ""
Write-Host "On a phone, just open poster.html in the browser - it reflows to one column on its own." -ForegroundColor DarkGray
