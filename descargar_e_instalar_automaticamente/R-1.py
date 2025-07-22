import requests
import os
import subprocess
import shutil  # ✅ Importar al inicio por claridad

# 📦 URL cruda del archivo R-1.py en GitHub (rama master)
url = "https://raw.githubusercontent.com/marlonblandon/practica_PyEz/master/R-1.py"

# 📁 Carpeta donde guardarás el archivo
destino = os.path.expanduser("~/R-1")
archivo = "R-1.py"
ruta_completa = os.path.join(destino, archivo)

# 🔧 Crear carpeta si no existe
os.makedirs(destino, exist_ok=True)

print(f"🔽 Descargando '{archivo}' desde GitHub...")
respuesta = requests.get(url)

if respuesta.status_code == 200:
    with open(ruta_completa, "w") as f:
        f.write(respuesta.text)
    print(f"✅ Archivo guardado en: {ruta_completa}")

    # 🚀 Ejecutar el script descargado
    print("⚙ Ejecutando el script sobre el router R-1...")
    resultado = subprocess.run(["python3", ruta_completa], capture_output=True, text=True)

    print("📦 Salida:")
    print(resultado.stdout)
    print("❗ Errores (si hubo):")
    print(resultado.stderr)
    #..............esta parte entre los puntos es pocional.................
    # 🧹 Eliminar carpeta después de aplicar la configuración
    try:
        shutil.rmtree(destino)
        print(f"🗑️ Carpeta '{destino}' eliminada automáticamente después de ejecutar la configuración.")
    except Exception as e:
        print(f"⚠️ No se pudo eliminar la carpeta '{destino}': {e}")
    #......................................................................     
else:
    print(f"❌ Error al descargar el archivo. Código: {respuesta.status_code}")
