#spy
import socket
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
  '''send message from client to server'''
  def __init__(self, sockInput, sockOutput, msg):
    threading.Thread.__init__(self)
    self.sockInput = sockInput
    self.sockOutput = sockOutput
    self.msg = msg
    
  def run(self):
    print "Starting " + self.msg
    while 1:
      try:
        message = self.sockInput.recv(32)
        if message:
          print self.msg, ':', message
          self.sockOutput.sendall(message)
        else:
          break
      except socket.error as msg:
        pass
        
    print "Exiting " + self.msg

try:
  ip = '127.0.0.1'
  portClient = 10102
  portServer = 10101
  
  
  socket.inet_aton(ip)
  sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sockServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sockClient.settimeout(5)
  sockServer.settimeout(5)
  
  # try to connect to the server 1st
  print 'Connecting to server'
  while 1:
    try:
      sockClient.connect((ip, portClient))
      break
    except socket.error as msg:
      pass
  print 'Connected!'
  print
  
  # if connected to server, waits for connection from client
  sockServer.bind((ip, portServer))
  sockServer.listen(1)
  print 'waiting for connection'
  while 1:
    try:
      Connection, client_address = sockServer.accept()
      Connection.settimeout(5)
      break
    except socket.error:
      pass
      
      
  # Create two threads as follows
  try:
  # Create new threads
    thread1 = myThread(sockClient, Connection, 'Client > Server')
    thread2 = myThread(Connection, sockClient, 'Server > Client')
    
    threads = [thread1, thread2]
    for t in threads: t.start()
    for t in threads: t.join()
    
  except:
     print "Error: unable to start thread"
     
except socket.error as msg:
  print msg
finally:
  sockClient.close()
  sockServer.close()
  