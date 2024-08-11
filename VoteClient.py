from socket import *
import random

canidates = ["JohnD", "JaneD"]
serverName = "localhost"

serverPort = 5555

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

for i in range(10):
    selection = random.choice(canidates)
    clientSocket.send(selection.encode('utf-8'))
    print(selection + " - Vote Sent to VoteServer")
    response = clientSocket.recv(1024).decode('utf-8')
    print ("Received from VoteServer: ",response)

print("End of Voting")


response = clientSocket.recv(1024).decode('utf-8')
print ("Received from VoteServer: ",response)

# close the TCP connection
clientSocket.close()
