# Solicitud Delete / eliminar un recurso del servidor

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

# Realizamos la solicitud DELETE
r = requests.delete(url)

# Comprobar el codigo de estado y mostrar la respuesta
if r.status_code == 200: # 200 indica que el recurso se elimino correctamente
    print("El recurso se elimino correctamente")
else:
    print(f"Error en la solicitud DELETE: {r.status_code}")