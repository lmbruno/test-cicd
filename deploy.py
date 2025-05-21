#!/usr/bin/env python3

import os
import subprocess

def deploy():
  print("Obteniendo el codigo...")
  subprocess.run(["git", "pull"], check=True)
  print("Ejecutando pruebas ...")
  # Aqui iria la logi para crear un paquete zip.
  print("Desplegando la app")
  # Simula el despliegue copiando el archivo a un directorio destino
  os.makedirs("destino", exist_ok=True)
  subprocess.run(["cp", "index.html", "destino/index.html"],check=True)
  print("Despliegue realizado en el destino")

if __name__ == "__main__":
  deploy()
