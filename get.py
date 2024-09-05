# Solicitud HTTP get / Enviar una solicitud get al servidor / PEDIR

import requests

url="https://jsonplaceholder.typicode.com/posts"

r = requests.get(url, timeout=5)

data = r.json()

# Comprobar el codigo de estado de la respuesta
if r.status_code == 200:
    data = r.json()
    for d in data:
        print(d)
        print("***************************")
else:
    print(f"Error: {r.status_code}")
    
# Manejo de errores
try:
    r = requests.get(url)
    r.raise_for_status() # Esto lanza una excepcion si la solicitud falla
    data = r.json()
    for d in data:
        print(d)
        print("***************")
except requests.exceptions.HTTPError as e:
        print(f"Error en la solicitud: {e}")