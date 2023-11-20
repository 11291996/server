from socket import * 

HOST = str(gethostbyname(gethostname()))
PORT = 1234

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM) #creating a socket for call-ins 
    try :
        serversocket.bind((HOST, PORT)) #assigning an address to the serversocket  
        serversocket.listen(5) #holding up the next browsers 
        while(1): #creating a clientsocket that will block the loop before receiving the browser
            (clientsocket, address) = serversocket.accept() 
            
            rd = clientsocket.recv(5000).decode() #after the call, changing UTF-8 to Unicode
            pieces = rd.split("\n")
            if ( len(pieces) > 0 ) : print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body><p style='font-size:200%'>Noa is cute</p><p style='font-size:15px'>hi noa nice to meet you :)</p></body></html>\r\n\r\n"
            clientsocket.sendall(data.encode()) #sending the data again as UTF-8
            clientsocket.shutdown(SHUT_WR) #shutting down the browser first, then goes back to the while loop
    # extra options which terminates the server
    except KeyboardInterrupt :
        print("\nShutting down...\n");
    except Exception as exc :
        print("Error:\n");
        print(exc)

    serversocket.close() 

print('Access http://' + HOST + ':' + str(PORT))
createServer()

