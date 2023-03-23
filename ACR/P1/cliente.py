#!/usr/bin python3

import socket
import numpy as np
import time

def deco(mensaje):
    msgDeco = mensaje.decode('utf-8')
    return msgDeco

def cod(mensaje):
    msgCod = mensaje.encode('utf-8')
    return msgCod

inicio = time.time()
HOST = "192.168.0.120"  # Hostname o  dirección IP del servidor
PORT = 65432  # Puerto del servidor
buffer_size = 1024
fila = 0
columna = 0
mina = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))
    dificultad = input("Introduce la dificultad, 1 para principiante, 2 para avanzado: ")
    if not dificultad:
        print("Error al enviar la dificultad")
    TCPClientSocket.send(cod(dificultad))
    print("Esperando una respuesta...")
    data = TCPClientSocket.recv(buffer_size)
    print("Recibido: ", deco(data) , " de", TCPClientSocket.getpeername())
    print("Esperando una respuesta...")
    tablero = TCPClientSocket.recv(buffer_size)
    if not tablero:
        print("Error al recibir el tablero")
    print("Este es tu tablero:\n", deco(tablero))
    #AQUI INICAN LAS COORDENADAS DEL CLIENTE
    while True:
        fila = input("Ingresa la fila: ")
        TCPClientSocket.send(cod(fila))
        print("Enviando fila al servidor")
        columna = input("Ingresa la columna: ")
        TCPClientSocket.send(cod(columna))
        print("Enviando columna al servidor")
        print("Esperando recibir tablero actualizado")
        tablero = TCPClientSocket.recv(buffer_size)
        if not tablero:
            print("Error al recibir el tablero actualizado")
        print("Este es tu tablero actualizado:\n", deco(tablero))
        dificultad = int(dificultad)
        fila = int(fila)
        columna = int(columna)
        if dificultad == 1:
            if (fila == columna) or (fila == 0 and columna == 9):
                print("Perdiste:(\nElegiste una mina")
                break
        if dificultad == 2:
            if columna == 0 or columna == 15:
                print("Perdiste:(\nElegiste una mina")
fin = time.time()
print("Duracion del juego: ", fin-inicio, "segundos")
    
        


