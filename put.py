# Solicitud PUT / se utiliza para actualizar un recurso existente

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

# Nuevos datos para actualizar el post
data = {
    "title": "Actualizado",
    "body": "Este es el cuerpo del post actualizado",
    "userId": 1
}

# Realizamos la solicitud PUT
r = requests.put(url, json=data)

# Comprobar el codigo de estado y mostrar la respuesta
if r.status_code == 200: # 200 indica exito de la actualizacion
    print("El post ha sido actualizado correctamente")
else:
    print("Error en la solicitud PUT: {r.status_code}")