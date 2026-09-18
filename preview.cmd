@echo off
REM ---------------------------------------------------------------------------
REM  Preview the site locally. Double-click this file.
REM
REM  Why this exists: browsers refuse to load web fonts from a file:// page for
REM  security reasons, so opening index.html straight from Explorer shows the
REM  fallback typefaces instead of Newsreader and Inter, and the Telugu
REM  subtitles may not render. Serving the folder over http fixes all of that.
REM
REM  Needs Python, which you already have. Close the black window to stop.
REM ---------------------------------------------------------------------------

cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
  echo.
  echo   Python was not found on PATH.
  echo   Install it from https://www.python.org/downloads/ ^(tick "Add to PATH"^),
  echo   or open this folder in VS Code and use the Live Server extension.
  echo.
  pause
  exit /b 1
)

echo.
echo   Serving this folder at http://localhost:4181/
echo   Opening your browser... close this window to stop the server.
echo.

start "" "http://localhost:4181/"
python -m http.server 4181 --bind 127.0.0.1
