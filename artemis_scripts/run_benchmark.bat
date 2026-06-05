@echo off
setlocal

rem Directory of this script
set "DIR=%~dp0"

rem Run benchmark via Python orchestrator (cross-platform RSS/CPU sampling).
rem Forwards all args to benchmark.py (e.g. --runs N, --output PATH).
echo Running benchmark
python -m poetry run python "%DIR%benchmark.py" %*

endlocal
exit /b %ERRORLEVEL%
