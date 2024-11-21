# save this as app.py

from flask import Flask,request,jsonify     #
import joblib   #
from flask_cors import CORS #Para manejo de flask
import cv2  #
import numpy as np  #
from io import BytesIO  #
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import io

app = Flask(__name__) #para hacer la aplicacion de flask
CORS(app) #para que quede en aplicaciones cruzadas

model = load_model('modelo.h5')   

def convertir_a_matriz(imagen): #aqui convierte la imagen a matriz y tambien la pone en un so9lo canal de color, aplana y normaliza la imagen
    imagen_bytes = imagen.read()
    #img = image.load_img(imagen, target_size=(299, 299))
    img = image.load_img(io.BytesIO(imagen_bytes), target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

@app.route('/',methods=['POST']) #
def hello():
    try:
        # Obtiene la imagen desde la solicitud POST
        imagen = request.files['imagen'] #En cliente se pone imagen como id de variable por eso aqui va imagen tambien
        

        if imagen:
            #model = load_model('modelo.h5')       
            
            matriz_resultante = convertir_a_matriz(imagen) #se carga el modelo
            print("result",matriz_resultante) 
            yp=model.predict(matriz_resultante)
            predicted_class = np.argmax(yp[0])
            print("predict",predicted_class)
            return jsonify({'y': int(predicted_class)}) #como se coloco y, es la que envia como respuesta
        else:            
            return jsonify({'error': 'No se proporcionó ninguna imagen'}), 400

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)}), 500     
    
        

    
