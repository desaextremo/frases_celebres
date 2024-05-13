'''
Versión 2
Usar FastApi para exponer nuestros métodos a internet

1 importar paquete random
2 Definir método 'anotado' para consultar una frase aleatoria
  
	leer todo el contenido del archivo de frases
	Seleccionar aleatoriamente una frase del listado
	Retornarla
	random.choice(lista)
	
3 Configurar seguridad CORS
4 Probar aplicación con servidor uvicorn
'''

import random
#1  Agregar sentencias import al inicio del código para usar e instanciar a FastAPI y Uvicorn
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#Llamamos a FastAPI, y desde este momento haremos referencia a este mediante la variable 'app'
app = FastAPI()

#2 Agregar instrucciones para evitar bloqueos de seguridad tipo CORS
# Permitir solicitudes desde todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir esto a los orígenes que desees permitir
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

#3 definir una función 'anotada' o con anotaciones de Fastapi
# para leer todo el contenido del archivo de frases, seleccionar una frase y retornarla
@app.get("/obtenerfrase")
def retornar_frase():
    nombrearchivo ="frases.txt"
    archivo = open(nombrearchivo,"r",encoding="utf8")
    #lista = ["Frase 1","Frase 2","Frase 3".... n frases]
    #obtener el contenido del archivo en una lista de python
    frases = archivo.readlines()
    #seleccionamos una frase aleatoria de la lista de frases
    return random.choice(frases)
    

#iniciar servidor uvicorn
#localhost:8080/obtenerfrase
'''if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
'''