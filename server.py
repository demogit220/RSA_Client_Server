import socket
import pickle
import rsa


if __name__ == "__main__":

    public, private = rsa.generate_keypair(64)
    msg=pickle.dumps(public)

    ip = input("Input the IP: ")
    port = input("Input the Port: ")

    # Define Server:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, int(port)))
    server.listen(1)

    while True:
        conn, addr = server.accept()
        print(f'Connection Established - {addr[0]}:{addr[1]}')

        # ---------------sending details-------------
        conn.send(msg)#sending public key
        rmsg=conn.recv(1024)#recv pub key
        pkey=pickle.loads(rmsg)
        #print("public key of other is :",pkey[0])
        connected = True
        while True:
            response_message = int(conn.recv(1024).decode())
            decrypted_msg = rsa.decrypt(response_message, private)
            if(decrypted_msg == "quit"): connected = False
            print(decrypted_msg)


