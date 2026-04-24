Write-Host ""
Write-Host " Syncing to GitHub..." -ForegroundColor Cyan
Write-Host ""

Set-Location $PSScriptRoot

git add .
git commit -m "manual sync"
git push

Write-Host ""
Write-Host " Done!" -ForegroundColor Green
