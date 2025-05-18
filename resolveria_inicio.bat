@echo off
echo Iniciando sistema Resolver IA con modelo gratuito de Hugging Face...
cd /d "%~dp0"
chcp 65001 > nul

REM Ejecuta primero la revisión de archivos
python procesar_archivos.py

REM Luego lanza el sistema principal
python langchain_rag_huggingface.py

pause
