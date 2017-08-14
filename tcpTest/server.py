#server
import socket


try:
  ip = '127.0.0.1'
  port = 10102
  socket.inet_aton(ip)
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(5)
  
  sock.bind((ip, port))
  sock.listen(1)
  
  print 'waiting for connection'
  while 1:
    try:
      connection, client_address = sock.accept()
      break
    except socket.error:
      pass
  print 'connected'
  while 1:
    try:
      message = connection.recv(32)
      if not message: break
      print message
      import time
      time.sleep(1)
      connection.sendall(message + 'loop')
    except socket.error:
      pass
    
  print message
  
  #sock.connect((ip, port))
  #sock.sendall ('client test')
  
except socket.error as msg:
  print msg
except KeyboardInterrupt:
  print 'Closed by user'
finally:
  sock.close()