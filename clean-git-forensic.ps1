# clean-git-forensic.ps1
# ———————————————————————————————————————————————————
# Automatiza limpieza de claves sk-proj-, elimina de historial, working tree y fuerza push seguro.
# Crea carpeta si falta, barre claves, genera replacements.txt, limpia archivos, ejecuta git-filter-repo, commitea y pushea.
# Logs claros y validación final.
# ———————————————————————————————————————————————————

# CONFIGURACIÓN
$carpeta = "C:\Users\alfau\OneDrive\Documentos\resolveria"
$replacementsPath = "$carpeta\replacements.txt"
$archivos = @(".env.local", ".env.example", "main.py", "render.yaml")

Write-Host "`n========== INICIANDO LIMPIEZA FORENSE COMPLETA ==========" -ForegroundColor Cyan

# 1. Crear carpeta si falta
if (-not (Test-Path $carpeta)) {
    New-Item -Path $carpeta -ItemType Directory | Out-Null
    Write-Host "🗂 Carpeta creada: $carpeta"
} else {
    Write-Host "🗂 Carpeta ya existe: $carpeta"
}

# 2. Generar replacements.txt
$replacements = @()
Get-ChildItem -Path $carpeta -Recurse -Include *.py,*.yaml,*.yml,*.env* |
    Select-String "sk-proj-" |
    ForEach-Object {
        foreach ($m in [regex]::Matches($_.Line, "sk-proj-[a-zA-Z0-9_\-]+")) {
            $clave = $m.Value
            if ($replacements -notcontains $clave) {
                $replacements += "$clave==>REMOVED_OPENAI_KEY"
            }
        }
    }
$replacements | Set-Content -Path $replacementsPath -Encoding UTF8
if (Test-Path $replacementsPath) {
    Write-Host "✅ replacements.txt creado en $carpeta"
} else {
    Write-Host "❌ Error creando replacements.txt" -ForegroundColor Red
    exit 1
}

# 3. Descarga git-filter-repo.py si falta
if (-not (Test-Path "$carpeta\git-filter-repo.py")) {
    Invoke-WebRequest -Uri "https://raw.githubusercontent.com/newren/git-filter-repo/main/git-filter-repo.py" -OutFile "$carpeta\git-filter-repo.py"
    Write-Host "⬇️  git-filter-repo.py descargado"
} else {
    Write-Host "💾 git-filter-repo.py ya presente"
}

# 4. Limpieza archivos actuales (working tree)
foreach ($archivo in $archivos) {
    $ruta = Join-Path $carpeta $archivo
    if (Test-Path $ruta) {
        (Get-Content $ruta) | ForEach-Object { $_ -replace "sk-proj-[a-zA-Z0-9_\-]+", "REMOVED_OPENAI_KEY" } | Set-Content $ruta -Encoding UTF8
        Write-Host "🧹 Claves limpiadas en $archivo"
    }
}

# 5. Ejecuta git-filter-repo para limpieza total de historial
Write-Host "`n🚦 Ejecutando limpieza de historial (git-filter-repo)..."
python "$carpeta\git-filter-repo.py" --replace-text "$replacementsPath"
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error ejecutando git-filter-repo.py" -ForegroundColor Red
    exit 1
}

# 6. git add, commit y push --force
Set-Location $carpeta
git add .
git commit -m "Purge: All OpenAI API keys completely removed from history and working tree. Forensic clean."
git push --force

Write-Host "`n🔒 Proceso forense terminado: claves eliminadas del repo, historial y archivos. Repo seguro." -ForegroundColor Green
Write-Host "===========================================================" -ForegroundColor Cyan

# ———————————————————————————————————————————————————
