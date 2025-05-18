import os

# Ruta base
base_dir = r"C:\Users\alfau\OneDrive\Documentos\resolveria"

# Extensiones que se intentarán leer como texto
extensiones_texto = [".txt", ".py", ".json", ".md", ".bat", ".log"]

print("📁 Revisión completa de la estructura y contenidos:\n")

for carpeta_raiz, subdirs, archivos in os.walk(base_dir):
    for archivo in archivos:
        ruta_completa = os.path.join(carpeta_raiz, archivo)
        extension = os.path.splitext(archivo)[1].lower()
        print(f"🗂️ Ruta: {ruta_completa}")
        print(f"     Nombre: {archivo}")
        print(f"     Tipo: {extension or 'Sin extensión'}")
        if extension in extensiones_texto:
            try:
                with open(ruta_completa, "r", encoding="utf-8", errors="ignore") as f:
                    contenido = f.read(300).strip().replace('\n', ' ')
                    print(f"     Contenido (300 primeros caracteres): {contenido or '[Vacío]'}")
            except Exception as e:
                print(f"     ❌ Error leyendo: {e}")
        print("-" * 80)
