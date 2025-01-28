import socket

# Konfigurace serveru
server_inet_address = ("127.0.0.1", 65532)

# Vytvoření socketu
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Nastavení socketu na opětovné použití portu
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind na IP adresu a port
    server_socket.bind(server_inet_address)
    # Naslouchání na příchozí připojení
    server_socket.listen(1)
    print(f"Server běží na {server_inet_address[0]}:{server_inet_address[1]}")

    try:
        while True:
            # Přijetí spojení
            connection, client_address = server_socket.accept()
            with connection:
                print(f"Klient připojen: {client_address[0]}:{client_address[1]}")
                # Příprava zprávy
                message = "HELLO\n"
                message_as_bytes = bytes(message, "utf-8")
                # Odeslání zprávy klientovi
                connection.sendall(message_as_bytes)
                print("Zpráva odeslána: HELLO")
    except KeyboardInterrupt:
        print("\nServer ukončen klávesovou zkratkou.")
    except Exception as e:
        print(f"Došlo k chybě: {e}")
    finally:
        print("Server je zavřen.")
