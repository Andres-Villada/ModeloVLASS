Para ejecutar la parte del modelo junto con el servicio de Flask es necesario seguir los siguientes pasos:

1. Montar el servicio de Flask, para ello teniendo python instalado en la versión 3.10.0rc2, en cmd se ejecuta: python -m venv flask.
2. Una vez montado el servicio de flask, usando cmd dentro de la carpeta Scripts se activa el servicio de flask con el comando: activate
3. Ahora se instala las dependencias anexadas como "dependences.txt", asi mismo, las versiones de tensorflow 2.15.0 y keras 2.15.0
4. Para continuar se debe colocar dentro de la carpeta "FlaskService" los archivos app.py y el modelo
5. Con el servicio de flask activo, es necesario redirigirse desde el cmd a la carpeta "FlaskService" y se corre el servicio con el comando: flask run
 

Por cuestiones del tamaño del modelo no es posible subirlo por este medio, se encuentra aqui:
https://drive.google.com/file/d/1kx6T1UTXZRiX4LjhrCFyMZUTSYgWfALV/view?usp=sharing
