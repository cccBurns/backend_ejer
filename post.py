# Solicitud POST

import requests

url = "https://jsonplaceholder.typicode.com/posts"

# Datos que queremos enviar
data = {
    "title": "Mi nuevo post",
    "body": "Este es el cuerpo del nuevo post",
    "userId": 1
}

# Realizamos la solicitud POST
r = requests.post(url, json=data)

# Comprobar el codigo de estado y mostrar la respuesta
if r.status_code == 201: # 201 es el codigo de exito para crear
    print("El post se ha creado correctamente", r.json())
else:
    print(f"Error en la solicitud POST: {r.status_code}")