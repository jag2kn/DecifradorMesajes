DecifradorMesajes
=================

Implementación para decifrar mensajes en RSA conociendo la llave publica y mediante un diccionario de los primeros 50 millones de numeros primos

El algoritmo fue implementado a partir de la explicación de este video: 

https://www.youtube.com/watch?v=HRUfPca7uec

Uso
===
Descargar la base de datos de numeros primos
<pre>
make descargar
</pre>


Archivo de mensajes
===================

Formato del archivo

<pre>
Mensaje número	1
n	21175164103
Llave pública	97
Mensaje cifrado:
2403886947	12682442110	10160707153	18701704406
</pre>

Ejecución
=========

<pre>
python decifradorMensajesRSA.py archivoMensajes.py
</pre>

