DecifradorMesajes
=================

Implementación para decifrar mensajes en RSA conociendo la llave publica y mediante un diccionario de los primeros 50 millones de numeros primos



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
python decifradorMensajes.py archivoMensajes.py
</pre>

