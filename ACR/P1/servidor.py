#!/usr/bin python3
import socket
import numpy as np

minas16 = [[6,7],[6,8],[7,7],[7,8],[8,7],[8,8],[9,7],[9,8]]

def deco(mensaje):
    msgDeco = mensaje.decode('utf-8')
    return msgDeco

def cod(mensaje):
    msgCod = mensaje.encode('utf-8')
    return msgCod

def creaTablero(dificultad):
    if dificultad == 1:
        tablero = np.array([[0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0]])
        return(tablero)
    if dificultad == 2:
        tablero = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
        return(tablero)
    else:
        print("Error al generar el tablero")
HOST = "192.168.0.120"  # Direccion de la interfaz de loopback estándar (localhost)
PORT = 65432  # Puerto que usa el cliente  (los puertos sin provilegios son > 1023)
buffer_size = 1024
fila = 0
columna = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("El servidor TCP está disponible y en espera de solicitudes")

    Client_conn, Client_addr = TCPServerSocket.accept()
    with Client_conn:
        print("Conectado a", Client_addr)
        print("Esperando la dificultad...")
        data = Client_conn.recv(buffer_size)
        if not data:
            print("Error")
        print("La dificultad que elegiste fue: ", deco(data))
        print("Enviando respuesta a", Client_addr)
        Client_conn.sendall(data)
        newData = int(deco(data))
        tab = creaTablero(newData)
        tabSTR = str(tab)
        print("Enviando tablero al cliente...")
        Client_conn.sendall(cod(tabSTR))
        #AQUI SE EMPIEZAN A PEDIR LAS COORDENADAS
        while True:
            print("Esperando fila...")
            fila = Client_conn.recv(buffer_size)
            if not fila:
                print("Error al recibir la fila")
            print("Fila seleccionada: ", deco(fila))
            fila = int(deco(fila))
            print("Esperando columna...")
            columna = Client_conn.recv(buffer_size)
            if not columna:
                print("Error al recibir la columna")
            print("Columna seleccionada: ", deco(columna))
            columna = int(deco(columna))
            if newData == 1:
                if (fila == columna) or (fila == 0 and columna == 9):
                    tab[fila,columna] = 1
                    print(tab)
                    tabSTR = str(tab)
                    print("Enviando tablero actualizado al cliente...")
                    Client_conn.sendall(cod(tabSTR))
                    print("El cliente ha perdido, seleccionó una mina")
                    break
            if newData == 2:
                if columna == 0 or columna == 15:
                    tab[fila,columna] = 1
                    print(tab)
                    tabSTR = str(tab)
                    print("Enviando tablero actualizado al cliente...")
                    Client_conn.sendall(cod(tabSTR))
                    print("El cliente ha perdido, seleccionó una mina")
                    break
            tab[fila,columna] = 4
            print(tab)
            tabSTR = str(tab)
            print("Enviando tablero actualizado al cliente...")
            Client_conn.sendall(cod(tabSTR))


        

