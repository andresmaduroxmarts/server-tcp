import socket
print("Wii")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dirección_del_servidor = ("70.35.203.160", 3000)
sock.bind(dirección_del_servidor)
sock.listen(5)
direccion = ('213.177.195.114', 29959)
while True:
    connection, dirección_del_cliente = sock.accept()
    print("Conexion",connection)
    while True:
        data = connection.recv(16)
        if data:
            print(data)
            connection.sendto(b"Hello",direccion)

    connection.close()
