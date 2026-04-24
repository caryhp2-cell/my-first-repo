@echo off
echo.
echo  Syncing to GitHub...
echo.

cd /d %~dp0

git add .
git commit -m "manual sync"
git push

echo.
echo  Done! Press any key to close.
pause > nul
