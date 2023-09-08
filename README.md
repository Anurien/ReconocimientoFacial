# ReconocimientoFacial

Este proyecto es una aplicación de Python que utiliza la biblioteca OpenCV para realizar el reconocimiento facial y contar monedas en imágenes o videos. Puede ser útil en aplicaciones como sistemas de seguridad, análisis de video, o incluso en juegos interactivos.

## Requisitos
Antes de comenzar, asegúrate de tener Python instalado en tu sistema. Además, necesitarás instalar algunas bibliotecas adicionales, incluyendo OpenCV.

## Instalación de OpenCV
Para instalar OpenCV, puedes utilizar pip, el gestor de paquetes de Python. Abre una terminal y ejecuta el siguiente comando:  
``` pip install opencv-python ``` si no funciona en windows utilizar: ``` py -m pip install opencv-python ```  
Yo tuve problemas con las versiones y no me autocompletaba, lo solucioné con :  
 ``` py -m pip install opencv-python==4.5.5.64 ```  

Este comando instalará la versión de OpenCV más reciente disponible en PyPI.

## Uso
Una vez que hayas instalado OpenCV, puedes utilizar este proyecto de reconocimiento facial para contar monedas en imágenes o videos.

Clona este repositorio o descarga los archivos del proyecto.  
``` git clone https://github.com/Anurien/ReconocimientoFacial.git ``` 

Abre una terminal y navega al directorio del proyecto.  
```cd MonedasContorno ```  

Ejecuta el script principal para iniciar la aplicación.  
``` python contadorMonedas.py ```

La aplicación te pedirá ingresar la ruta de la imagen o video que deseas analizar.  
Recuerda que las rutas en windows se escriben con este formato:  
``` '//Users//Usuario//Documents//Python//MonedasContorno//contorno.jpg' ```


La aplicación procesará la imagen o el video y mostrará el resultado, incluyendo el número de monedas detectadas.
