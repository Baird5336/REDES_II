import socket

def buscar():
    print ("                 ")
    print ("     1       2       3     4     5      6       7       8       9")
    print ("     |=======|=======|=======|=========|======|=====|======|=======|======|")
    print ("a    |   %c  |   %c  |   %c  |  %c     |  %c  |  %c |  %c   |  %c  |    %c"%(M[0], M[1], M[2], M[3], M[4], M[5], M[6], M[7], M[8]))
    print ("     |=======|=======|=======|=========|======|=====|======|=======|======|")
    print ("b    |   %c  |   %c  |   %c  |  %c     |  %c  |  %c |  %c   |  %c  |    %c"%(M[10], M[11], M[12], M[13], M[14], M[15], M[16], M[17], M[18]))
    print ("     |=======|=======|=======|=========|======|=====|======|=======|======|")
    print ("c    |   %c  |   %c  |   %c  |  %c     |  %c  |  %c |  %c   |  %c  |    %c"%(M[19], M[20], M[21], M[22], M[23], M[24], M[25], M[26], M[27]))
    print ("     |=======|=======|=======|=========|======|=====|======|=======|======|")
    print ("d    |   %c  |   %c  |   %c  |  %c     |  %c  |  %c |  %c   |  %c       %c  |"%(M[28], M[29], M[30], M[31], M[32], M[33], M[34], M[35], M[36]))
    print ("     |=======|=======|=======|=========|======|=====|======|=======|======|")
    print ("e    |   %c  |   %c  |   %c  |  %c     |  %c  |  %c |  %c   |  %c  |    %c"%(M[37], M[38], M[39], M[40], M[41], M[42], M[43], M[44], M[45]))
    print ("     |=======|=======|=======|=========|======|=====|======|=======|======|")
    print ("f    |   %c  |   %c  |   %c  |  %c     |  %c  |  %c |  %c   |  %c  |    %c"%(M[46], M[47], M[48], M[49], M[50], M[51], M[52], M[53], M[54]))
    print ("     |=======|=======|=======|=========|======|=====|======|=======|======|")
    print ("g    |   %c  |   %c  |   %c  |  %c     |  %c  |  %c |  %c   |  %c  |    %c"%(M[55], M[56], M[57], M[58], M[59], M[60], M[61], M[62], M[63]))
    print ("     |=======|=======|=======|=========|======|=====|======|=======|======|")
    print ("h    |   %c  |   %c  |   %c  |  %c     |  %c  |  %c |  %c   |  %c  |    %c"%(M[64], M[65], M[66], M[67], M[68], M[69], M[70], M[71], M[72]))
    print ("     |=======|=======|=======|=========|======|=====|======|=======|======|")
    print ("i   |   %c  |   %c  |   %c  |  %c     |  %c  |  %c |  %c   |  %c  |     %c"%(M[73], M[74], M[75], M[76], M[77], M[78], M[79], M[80], M[81]))
    print ("     |=======|=======|=======|=========|======|=====|======|=======|======|")
M=['0', '0', '0', '0', '0', '0', '0', '0', '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
#Se crea el socket para el servidor
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Se conecta el programa con el servidor con connect
s.connect(("127.0.0.1", 127))
#Creamos un ciclo para mantener la conexion

s.send(b"Juguemos")
buscar()



while True:
    while True:
        f= input("Fila : ")

        if(f == 'a') :
            f=1
        elif (f =='b') :
            f=2
        elif (f =='c') :
            f=3
        elif (f =='d') :
            f=3
        elif (f =='c') :
            f=4
        elif (f =='e') :
            f=5
        elif (f == 'f') :
            f=6
        elif (f == 'g') :
            f=7
        elif (f=='h') :
            f=8
        elif (f=='i') :
            f=9
        else:
            f=0
         
            if (f>0 and f<10):
                c = input ("Columna : ")
                if(c>0 and c<10):
                    p = 3*(f-1)+(c-1)
                    s.send(str(p))
                    break
        print("\n ingrese rango correcto \n")
        k = s.recv(2)
        if (k=='X') :
            M[p]='X'
        else:
            M[p] = "*"
        buscar()
        gana=s.recv(1024)
        if(k == 'X') :
            print("\n Perdiste")
            break
        elif(gana == True):
            print("\n Felicidades, ganaste")
            break
print("\n\n Juego terminado")
s.close()