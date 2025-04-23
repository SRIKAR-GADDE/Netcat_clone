import socket

# Prompt the user for the IP address of the attacking machine
server_ip = input("Enter the IP address of the attacking machine: ")
port = 6969  # The port can stay the same, or you can also prompt for it.

# Create a socket object and connect to the attacking machine's IP address
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Attempt to connect to the server (attacking machine)
    client.connect((server_ip, port))
    print(f"Connected to {server_ip} on port {port}")

    while True:
        msg = input("You (client): ")
        client.send(msg.encode())

        if msg.lower() == "exit":
            print("Disconnected from server")
            break

        # Receive the server's response and print it
        response = client.recv(1024).decode()
        print("Server:", response)

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
