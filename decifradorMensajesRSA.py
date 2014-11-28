#!/bin/python
# -*- coding: utf-8 -*- 

import math
import sys

def calculadorLlavePrivada(p, q, e):

	#p = 19 #numero primo
	#q = 23 #numero primo
	n = p*q
	phi = (p-1)*(q-1)


	#e=247

	phiT = phi
	eT = e

	cociente=1
	cocientes = []
	i = 0
	modulo=1
	while modulo!=0:
		cociente = phiT/eT
		cocientes.append(cociente)
		modulo = phiT%eT
		phiT = eT
		eT = modulo
		i = i+1	
	
		#print "cociente "+str(cociente)
		#print "modulo "+str(modulo)
		#print "phiT "+str(phiT)
		#print "eT "+str(eT)
	

	xT=1
	yT=0

	i=len(cocientes)-1
	while i!=-1:
		xTT = xT
		xT = yT
		yT = xTT - (yT * cocientes[i])
		i=i-1
	
		#print "xT "+str(xT)
		#print "yT "+str(yT)

	#print "-> "+str(phi*xT+yT*e)
	if yT<0:
		yT = yT+phi

	d = yT

	#print "La llave privada es "+str(d)
	return d



def powerMod(k, n, s):
	#potencias = int(math.log(k)/math.log(2))
	
	'''
	print "-----------"
	print "PowerMod (",
	print k,
	print ", ",
	print n,
	print ", ",
	print s,
	print ")"
	#'''
	
	i=1
	
	t = str(bin(k))[2:]
	
	r = s
	p = s
	a = s
	i=1
	while i!=len(t):
		#print "Paso PowerMod ",i," len ", len(t),t
		#print "Paso PowerMod ",i,"  t [",t,"]  t["+str(i)+"] ",t[i],"   p=",p,"   r=",r,"   n=",n,
		
		if t[i]=="1":
			r = (r*r*p)%n
		else:
			r = (r*r)%n

		#print "  =   r(nuevo) ",r

		i = i + 1
	return r


def encontrarFactoresArchivo(archivo, n):
	with open(archivo) as f:
		content = f.readlines()
		nlinea = 0
		for l in content:
			nlinea = nlinea + 1
			if nlinea>2:
				ds = l.split(" ")
				for d in ds:
					x = d.strip()
					if len(x)>0:
						p=int(x)
						residuo = n%p
						if residuo==0:
							return p

	return n
def encontrarFactores(n):
	print " * Encontrar Factores"
	p = n
	contador = 1
	while p==n and contador<=50:
		print " * Analizando archivo de primos ",contador
		p = encontrarFactoresArchivo("Primos/primes"+str(contador)+".txt", n);
		contador = contador + 1
	print " * El numero primo ",p
	return p


def decifrarMensaje(mensaje, n, llavePublica, datos):
	#print "\t\tDecifrando Mensaje "+mensaje
	#print "n "+str(n)
	#print "llavePublica "+str(llavePublica)
	#print "datos ",
	#print datos


	p = encontrarFactores(n)
	q = n/p
	
	#print "Los factores son ["+str(p)+", "+str(q)+"]"
	
	llavePrivada = calculadorLlavePrivada(p, q, llavePublica)
	
	#print "con los datos da la llavePrivada"
	#print "p ",
	#print p
	#print "q ",
	#print q
	#print "llavePublica ",
	#print llavePublica
	#print "Llave privada ",
	#print llavePrivada
	t = str(bin(llavePrivada))[2:]
	#print t
	#print "--------------"
	
	
	mensaje = ""
	for d in datos:
		r = powerMod(llavePrivada, n, int(d))
		mensaje = mensaje + chr(r)
		#print "-> El resultado del PowerMod para ",d,"  me esta dando : "+str(r)+" - "+chr(r)
	print " * Mensaje decifrado : ",mensaje

		
'''
Mensaje número	1
n	164864459113
Llave pública	97
Mensaje cifrado:
123 123 123 123 123 123
'''
def decifrarArchivo(nombreArchivo):
	mensaje = 0
	n=0
	llavePublica=0
	datos = []
	with open(nombreArchivo) as f:
		content = f.readlines()
		for p in content:
			#print "Analizando "+p
			if p[0:9]=="Mensaje n":
				mensaje = p.split("\t")[1]
			if p[0]=="n":
				n = int(p.split("\t")[1])
			if p[0:5]=="Llave":
				llavePublica = int(p.split("\t")[1])
			if len(p)>30:
				p = p.strip()
				datos = p.split("\t")
				print "\n\n\tAnalizando mensaje ",mensaje
				decifrarMensaje(mensaje, n, llavePublica, datos)
				

'''

p = 19 #numero primo
q = 23 #numero primo
e = 247
d = calculadorLlavePrivada(p, q, e)
print "La llave privada es "+str(d)


r = powerMod(247, p*q, 39)
print "El powerMod es "+str(r)


#n = p*q
n = 140281188347
x = encontrarFactores(n)
print "El los factores de "+str(n)+" son : "+str(x)+" y "+str(n/x)

'''


if len(sys.argv)>1:
	decifrarArchivo(sys.argv[1])
else:
	decifrarArchivo("mensajes2.txt")








