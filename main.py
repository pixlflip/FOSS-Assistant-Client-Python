import socket

# input for connecting to server
# profileInput = input("Enter Your User Profile: ")
# profilePassword = input("Enter Your Password: ")
# Now infinite loop with basic commands from FOSS Assistant Main instance
end = False
while not end:

    # init connection to server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('0.0.0.0', 8080))
    # V2 Format     usr,pass,device:commandID:commandArg1,commandArg2,etc.
    client.send(b'testUser,none,A Laptop:testCommand:testCommandArgs:')
    from_server = client.recv(4096)
    client.close()
    print(from_server)
    end = True
