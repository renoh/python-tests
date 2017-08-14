#client
import socket


try:
  ip = '127.0.0.1'
  port = 10101
  socket.inet_aton(ip)
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(5)
  
  #sock.bind((ip, port))
  #sock.listen(1)
  #connection, client_address = sock.accept()
  #sock.recv(HEADER_SIZE)
  print 'connecting'
  sock.connect((ip, port))
  while 1:
    print 'sending'
    sock.sendall ('client test')
    msg = sock.recv(32)
    print msg
    import time
    time.sleep(5)
  
except socket.error as msg:
  print msg
finally:
  sock.close()