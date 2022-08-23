@echo off

call %~dp0telegram_bot\venv\SCripts\activate.bat

cd %~dp0telegram_bot

set TOKEN=5617344667:AAG5dykhtZK5GwBpvYU48r6NZ9RR8JIDym0

python main.py

pause