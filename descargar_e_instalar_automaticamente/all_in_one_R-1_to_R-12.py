import requests
import os
import subprocess

# Lista de routers
routers = [f"R-{i}" for i in range(1, 13)]  # R-1 hasta R-12

# Repositorio base
base_url = "https://raw.githubusercontent.com/marlonblandon/practica_PyEz/master"

for router in routers:
    print(f"🔽 Procesando configuración para {router}...")

    # URL y destino
    file_name = f"{router}.py"
    url = f"{base_url}/{file_name}"
    destino = os.path.expanduser(f"~/{router}")
    ruta_completa = os.path.join(destino, file_name)

    # Crear carpeta
    os.makedirs(destino, exist_ok=True)

    # Descargar archivo
    response = requests.get(url)
    if response.status_code == 200:
        with open(ruta_completa, "w") as f:
            f.write(response.text)
        print(f"✅ Archivo guardado en: {ruta_completa}")

        # Ejecutar script
        print(f"⚙ Ejecutando configuración en {router}...")
        resultado = subprocess.run(["python3", ruta_completa], capture_output=True, text=True)

        print(f"📦 Resultado para {router}:")
        print(resultado.stdout)
        if resultado.stderr:
            print(f"❗ Errores en {router}:")
            print(resultado.stderr)
    else:
        print(f"❌ No se pudo descargar {file_name}. Código: {response.status_code}")
