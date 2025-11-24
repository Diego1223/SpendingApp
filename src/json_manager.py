import json
import os


FILE = "session.json"

def cargar_sesion():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)
    
def guardar_sesion(data:dict):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def cerrar_sesion():
    if os.path.exists(FILE):
        os.remove(FILE)
        
