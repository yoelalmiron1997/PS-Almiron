> # Práctica Supervisada - UTN FRLP!
> Realicé la práctica supervisada en el Centro de Investigación (CODAPLI) en la UTN FRLP. Mi nombre es Yoel Maximiliano Almirón. 
> - [Biblioteca libre de visión artificial](https://opencv.org/) for [OpenCV](https://opencv.org/releases/)
> - [Leguaje Python](https://www.python.org/) for [Python](https://www.python.org/doc/)
> - [C.Investigación](https://www.frlp.utn.edu.ar/) for [CODAPLI](https://codapli.frlp.utn.edu.ar/)
> - [LINKEDIN](https://www.linkedin.com/in/yoel-almiron/)

<br>



<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/5/53/OpenCV_Logo_with_text.png" width="250" height="280">
</div>

# Haar Cascade

*Cascade Classifier* <br>
*La detección de objetos mediante clasificadores en cascada 
  basados en funciones de Haar es un método eficaz de detección 
  de objetos propuesto por Paul Viola y Michael Jones en su artículo.*

*OpenCV significa Open Computer Vision (Visión Artificial Abierta),* <br>
*se ha utilizado en una gran cantidad de aplicaciones y, hasta el 2020, sigue siendo la biblioteca más popular de visión artificial.*

<br>
  
## Resumen Ejecutivo

Este proyecto presenta un desarrollo para la sincronización de vehículos en zonas urbanas utilizando una técnica de cascada para facilitar el tránsito en las ciudades. Si bien la coordinación de los semáforos actuales puede percibirse como útil mediante la "onda verde", en ocasiones no resulta justa para todos los conductores. En la solución planteada, se propone una demostración que utiliza técnicas de inteligencia artificial para lograr una mejor sincronización, más justa y más segura, evitando la acumulación innecesaria de tiempo en distintas zonas.

  
<br>
  
# Proyecto de Ciudad Inteligente: Optimización de la sincronización vehicular con algoritmos de inteligencia artificial

## Introducción

El término "Ciudad Inteligente" plantea el objetivo de optimizar objetos cotidianos y adjuntar servicios más eficientes y funcionales en diversas ciudades y pueblos del mundo. En este proyecto, aspiramos a utilizar un algoritmo para hacer uso de los recursos hardware y simplificar la sincronización vehicular, implementando la técnica de inteligencia artificial más conocida como Haar Cascade para el seguimiento de imágenes.

El tránsito vehicular es un factor creciente que genera desconcierto, accidentes y retrasos temporales en distintas situaciones y sectores de distintas ciudades y pueblos. Muchas personas suelen tener disconformidades por estar expuestos a sufrir este tipo de desorden a diario, siendo perjudicados gran cantidad de personas por variantes que no son controladas.

Para evitar esto, se optó por implementar el concepto de Onda verde, que permite facilitar el tránsito y la sincronización de los semáforos. Sin embargo, este enfoque no contempla todas las posibles eventualidades, como el caso en que hay pocos vehículos esperando en una avenida y sin ningún peatón o vehículo cercano a las calles que intersectan con ella. Esto podría ser peligroso en algunas zonas, además de no ser equitativo para el resto de vehículos.

En este proyecto, se busca implementar un algoritmo de seguimiento de imágenes con Haar Cascade para optimizar la sincronización vehicular y mejorar la seguridad y equidad en el tránsito.

## Desarrollo de Sincronización de Vehículos en una Zona Urbana Utilizando Raspberry Pi y Haar Cascade

En este proyecto, se presenta una solución para mejorar la sincronización de los vehículos en una zona urbana utilizando la técnica de Haar Cascade y Raspberry Pi. La Raspberry Pi 4B, equipada con una cámara Catda C1130 con visión nocturna, se utiliza para detectar vehículos en diferentes momentos del día y en distintas condiciones. 

Se ha utilizado el lenguaje de programación Python 3 y el tipo abstracto de datos OpenCV, que incluye un motor de inferencia Intel Back-end (OpenVino) para el procesamiento de imágenes en tiempo real. También se ha instalado la interfaz de Raspberry Pi OS 32 bit para proporcionar muchas herramientas, incluyendo Python + IDE para realizar la codificación.

Para detectar los vehículos, se ha utilizado un algoritmo con la técnica de Haar cascade, que permite contar los vehículos y aplicar un algoritmo de prioridad más justo y equitativo para el resto de vehículos. En este proyecto, se ha utilizado un Haar cascade construido por Andrew Sobral, entrenado con diferentes vehículos en diferentes situaciones.

El objetivo de este proyecto es evitar la falta de la onda verde en las avenidas, donde se podría aplicar el desarrollo mencionado para una mejor sincronización del tráfico. 

