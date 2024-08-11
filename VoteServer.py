##########################################################################
""" VoteServer.py
  STUDENT NAME: Amrutha Ginkala
  COURSE NAME and SEMESTER: COMP 2602 -COMPUTER NETWORKING, SEMESTER 1
  DATE 17/11/18
  DOCUMENTATION: My program executed fairly well. I think I completed 100% of
  the requirements
"""

from socket import *
host = ''
port =5555
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind((host,port))

candidate1 = 0
candidate2 = 0
count = 1

server_socket.listen(1)
print("Awaiting connection on port " + str(port) + " to tally votes...")

while True:
    con_socket, addr = server_socket.accept()

    while count <=10:
        vote = con_socket.recv(1024).decode('utf-8')
        print("RECEIVED from the client (" + addr[0] + " : " + str(addr[1]) + ") = " + vote)
        if vote == "JohnD":
            candidate1 += 1
            count += 1
        if vote == "JaneD":
            candidate2 += 1
            count += 1

        con_socket.send("Vote Successful".encode('utf-8'))

    if candidate1 > candidate2:
        winner = "JohnD is the winner"
    if candidate2 > candidate1:
        winner = "JaneD is the winner"
    if candidate1 == candidate2:
        winner = "there has been TIE"

    print("JohnD got " + str(candidate1) + " votes and JaneD got " + str(candidate2) + " votes " + winner)
    con_socket.send(("JohnD got " + str(candidate1) + " votes and JaneD got " + str(candidate2) + " votes " + winner).encode('utf-8'))

    con_socket.close()
    # resetting so it can be run again while server has already been used
    # when run again varying results can be seen
    count = 1

