import socket
import pickle
import rsa
import binascii


if __name__  == "__main__":

    public, private = rsa.generate_keypair(64) # For longer words use more bits here instead of 64
    msg=pickle.dumps(public)

    ip = input("Input the IP: ")
    port = input("Input the Port: ")

    # Define Client and connect to server:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, int(port)))

    
    client.send(msg)
    rmsg=client.recv(1024)
    pkey=pickle.loads(rmsg)

    while True:
        text = input("Enter the message: ")

        if str(text).strip() != "":
            message = str.encode(text)
            #converting it into number
            hex_data   = binascii.hexlify(message)
            print(f'hex data: {hex_data}')
            plain_text = int(hex_data, 16)
            print(f'plain text: {plain_text}')
            ctt=rsa.encrypt(plain_text,pkey)
            print(f'ctt: {ctt}')
            client.send(str(ctt).encode())

    

