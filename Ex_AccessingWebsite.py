import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #.encode converts to utf-8
mysock.send(cmd) #file handle

while True:
    data = mysock.recv(512) #receive up to 512 characters
    if len(data) < 1:
        break #to quit the loop
    print(data.decode(),end='') #converts to unicode

mysock.close() #close the connection
