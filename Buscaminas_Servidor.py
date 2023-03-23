import socket
from random import randrange

def minas() :
    print ("                 ")
    print ("     1       2       3     4     5      6       7       8       9")
    print ("     |=======|=======|=======|=========|======|=====|======|=======|======|")
    print ("a    |   %c  |   %c  |   %c  |  %c     |  %c  |  %c |  %c   |  %c  |    %c"%(M[0], M[1], M[2], M[3], M[4], M[5], M[6], M[7], M[8]))
    print ("     |=======|=======|=======|=========|======|=====|======|=======|======|")
    print ("b    |   %c  |   %c  |   %c  |  %c     |  %c  |  %c |  %c   |  %c  |    %c"%(M[10], M[11], M[12], M[13], M[14], M[15], M[16], M[17], M[18]))
    print ("     |=======|=======|=======|=========|======|=====|======|=======|======|")
    print ("c    |   %c  |   %c  |   %c  |  %c     |  %c  |  %c |  %c   |  %c  |    %c"%(M[19], M[20], M[21], M[22], M[23], M[24], M[25], M[26], M[27]))
    print ("     |=======|=======|=======|=========|======|=====|======|=======|======|")
    print ("d    |   %c  |   %c  |   %c  |  %c     |  %c  |  %c |  %c   |  %c  |    %c"%(M[28], M[29], M[30], M[31], M[32], M[33], M[34], M[35], M[36]))
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
    def ganar(M) :
        ganador = True
    for i in range (9) :
        if M[1] == '0' :
            ganador = False
    return ganador

M=['0', '0', '0', '0', '0', '0', '0', '0', '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
#instanciamos un objeto de tipo socket
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 127
#Con el metodo bind le indicamos que puerto debe escuchar y de que servidor esperar conexiones
s.bind(('127.0.0.1', port))
print ("\n\nservidor esperando un jugador\n\n")
#el metodo listen() acepta tantas conexiones como el valor que le pasemos
s.listen(1)
(sc, adress)= s.accept()
mensaje = sc.recv(10)
if (mensaje == "juguemos") :
    print ("Turno del cliente")
    a=0
    while(a<9) :
        k = randrange(0,81)
        if (M[k]=="0"):
            M[k]=="1"
            a=a+1
minas()

while True :
    p = int(sc.recv(2))
    if (M[p]=='1'):
        k='X'
    else:
        k='*'
        M[p]='-'
        sc.send(k)
def ganar(M) :
        ganador = True
        for i in range (9) :
            if M[1] == '0' :
                ganador = False
            return ganador        
        
        gana = ganar(M)
        sc.send(str(gana))
        if (k== 'x') :
            print ("\n Le diste a una mina jaja")
            break
        elif (gana == True) :
            print ("\n Felicidades ganaste")
            break
print ("\n\n Terminamos")
sc.close()
s.close()