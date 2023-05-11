import socket
import time
import numpy as np




HOST = "192.168.1.93"
PORT = 65432  
buffer_size = 1024
jugandoP = 0


print("Ingresa la IP del servidor")
HOST = input()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    #Establece la conexión con el servidor
    TCPClientSocket.connect((HOST, PORT))
    #Recibe e imprime el mensaje de bienvenida
    data = TCPClientSocket.recv(buffer_size)
    info = str(data)[2:(len(str(data)) - 1)]
    print(info)
    #Mandamos la dificultad que queremos al servidor
    print("Selecciona la dificultad")
    mensaje = input()
    TCPClientSocket.sendall(bytes(mensaje, "UTF-8"))
    #Recibimos el primer mensaje del servidor
    data = TCPClientSocket.recv(buffer_size)
    info = str(data)[2:(len(str(data)) - 1)]
    print(info)
    data = TCPClientSocket.recv(buffer_size)
    info = str(data)[2:(len(str(data)) - 1)]
    print(info)
    data = TCPClientSocket.recv(buffer_size)
    info = str(data)[2:(len(str(data)) - 1)]
    print(info)
    data = TCPClientSocket.recv(buffer_size)
    info = str(data)[2:(len(str(data)) - 1)]
    print(info)
    jugandoP = 1
    time.sleep(2)
    if(mensaje == "principiante"):
        tablero = np.zeros((9, 9))
        while True:
            print("Selecciona una casilla")
            mensaje = input()
            TCPClientSocket.sendall(bytes(mensaje, "UTF-8"))
            data = TCPClientSocket.recv(buffer_size)
            info = str(data)[2:(len(str(data)) - 1)]
            print(info)
            if (info == "Okey"):
                tablero[int(mensaje[0]), int(mensaje[1])] = 8
                print(tablero)
            if (info == "Mina"):
                print("Has perdido")
                tablero[int(mensaje[0]), int(mensaje[1])] = 1
                print(tablero)
                data = TCPClientSocket.recv(buffer_size)
                info = str(data)[2:(len(str(data)) - 1)]
                print("Estuvo conectado: ", info, " segundos.")
                TCPClientSocket.close()
                break
    if(mensaje == "avanzado"):
        tablero = np.zeros((16, 16))
        while True:
            print("Haga su tiro en formato de dos números conformados por dos dígitos cada uno (xxyy), donde xx representa la fila mientras que yy representa la columna (números 0-15)")
            mensaje = input()
            TCPClientSocket.sendall(bytes(mensaje, "UTF-8"))
            data = TCPClientSocket.recv(buffer_size)
            info = str(data)[2:(len(str(data)) - 1)]
            print(info)
            
            if (info == "Okey"):
                tablero[int(mensaje[0:2]), int(mensaje[2:4])] = 8
                print(tablero)
            if (info == "Mina"):
                print("Has perdido")
                tablero[int(mensaje[0:2]), int(mensaje[2:4])] = 1
                print(tablero)
                data = TCPClientSocket.recv(buffer_size)
                info = str(data)[2:(len(str(data)) - 1)]
                print("Estuvo conectado: ", info, " segundos.")
                TCPClientSocket.close()
                break
                
            if not data:
                print("No hubo datos :(")
                exit()