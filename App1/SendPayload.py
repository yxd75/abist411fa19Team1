# Project: Project Diamond
# Purpose Details: Send Payload using TLS
# Course: IST 411
# Author: Team 1
# Date Developed: 10/11/19
# Last Date Changed: 10/16/19
# Rev: 2
import socket, ssl, json, datetime
from mongo import MongoDB
from pymongo import MongoClient

# To send payload
class SendPayload:

   # Connect to server and send payload
   def sendPayload(self, payload):
      try:
         print("App 1 connecting on port 8080 using TLS")
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         ssl_sock = ssl.wrap_socket(s,
            ca_certs="team1Server.crt",
            cert_reqs=ssl.CERT_REQUIRED)
         ssl_sock.connect(('localhost',8080))
         ssl_sock.sendall(payload)
         print("JSON payload sent to _______ using TLS")
         ssl_sock.close()
         print(ssl_sock.cipher())
         # Logging
         MongoDB.mongoInstance("Test","Sent to app2")
         return True

      except Exception as e:
         client = MongoClient('localhost', 27017)
         db = client.Team1
         collection = db.logs

         print(e)

         #Logging
         MongoDB.mongoInstance("Test","Failed to send to app2")
         return False
