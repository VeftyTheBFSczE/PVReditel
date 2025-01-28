import socket
import datetime
import random


# -------------------------
# 1) Definice příkazových funkcí
# -------------------------
def cmd_help(conn):
    text = (
        "Dostupné příkazy:\n"
        "  help               - Zobrazí tuto nápovědu.\n"
        "  quote              - Vrátí zajímavý (náhodný) citát.\n"
        "  date               - Vrátí aktuální datum a čas.\n"
        "  exit               - Ukončí spojení s klientem (server zůstává běžet).\n"
        "  shutdown-server    - Ukončí spojení a vypne server.\n"
    )
    conn.sendall(text.encode('utf-8'))


def cmd_quote(conn):
    quotes = [
        "Všechno, co si dokážeš představit, je skutečné. (Pablo Picasso)",
        "Život je to, co se děje, když jsi zaneprázdněn jinými plány. (John Lennon)",
        "Vzdělání je to, co zůstane, když zapomeneme vše, co jsme se naučili ve škole. (Albert Einstein)",
        "Život je příliš krátký na to, abychom pili špatné víno. (Johann Wolfgang von Goethe)"
    ]
    random_quote = random.choice(quotes)
    conn.sendall((random_quote + "\n").encode('utf-8'))


def cmd_date(conn):
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M:%S")
    response = f"Aktuální datum a čas: {date_str}\n"
    conn.sendall(response.encode('utf-8'))


def cmd_exit(conn):
    msg = "Ukončuji spojení s klientem...\n"
    conn.sendall(msg.encode('utf-8'))
    # Vrací False pro signalizaci, že máme klienta odpojit
    return False


def cmd_shutdown(conn):
    msg = "Server se vypíná...\n"
    conn.sendall(msg.encode('utf-8'))
    # Vrací speciální řetězec, abychom mohli server vypnout
    return "SHUTDOWN"


def cmd_unknown(conn, command):
    msg = f"Neznámý příkaz '{command}'. Zadejte 'help' pro seznam příkazů.\n"
    conn.sendall(msg.encode('utf-8'))


# -------------------------
# 2) Mapování příkazů na funkce
# -------------------------
COMMANDS = {
    "help": cmd_help,
    "quote": cmd_quote,
    "date": cmd_date,
    "exit": cmd_exit,
    "shutdown-server": cmd_shutdown,
}


# -------------------------
# 3) Obsluha jednoho klienta
# -------------------------
def handle_client(conn, address):
    """
    Čte od klienta řádky přes makefile('r') a zpracovává příkazy, dokud není
    zadán 'exit' nebo 'shutdown-server' nebo dokud klient neukončí spojení.
    """
    print(f"[INFO] Klient {address} se připojil.")

    # Pro čtení řádků (v textové podobě) si vytvoříme "file-like" objekt:
    f = conn.makefile('r')

    while True:
        line = f.readline()
        if not line:
            # EOF (klient zavřel spojení)
            print(f"[INFO] Klient {address} se odpojil.")
            break

        # Odstraníme konce řádků a mezery:
        line = line.strip()

        # Pokud je řádek prázdný, ignorujeme ho:
        if line == "":
            continue

        print(f"[RECV] Příkaz od {address}: '{line}'")

        # Najdeme a zavoláme příslušnou funkci:
        func = COMMANDS.get(line, None)
        if func is None:
            # Neznámý příkaz
            cmd_unknown(conn, line)
        else:
            # Voláme vybranou funkci
            result = func(conn)
            # Pokud funkce vrátí False, ukončujeme komunikaci s tímto klientem
            if result is False:
                print(f"[INFO] Příkaz 'exit' od {address} -> Ukončuji spojení.")
                break
            # Pokud funkce vrátí "SHUTDOWN", vypneme celý server
            elif result == "SHUTDOWN":
                print(f"[INFO] Příkaz 'shutdown-server' od {address} -> Vypínám server.")
                # Zavřeme spojení s klientem
                conn.close()
                return "SHUTDOWN"

    # Zavřeme spojení pro tohoto klienta
    conn.close()
    return None


# -------------------------
# 4) Hlavní server smyčka
# -------------------------
def main():
    SERVER_HOST = "127.0.0.1"  # Nebo konkrétní IP, např. "192.168.x.x"
    SERVER_PORT = 50970

    # Vytvoříme TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))

    server_socket.listen(5)
    print(f"[INFO] Server naslouchá na {SERVER_HOST}:{SERVER_PORT}")

    server_running = True
    while server_running:
        print("[INFO] Čekám na nového klienta...")
        conn, addr = server_socket.accept()

        # Obsloužíme klienta
        shutdown_signal = handle_client(conn, addr)

        if shutdown_signal == "SHUTDOWN":
            server_running = False

    print("[INFO] Server se vypíná.")
    server_socket.close()


if __name__ == "__main__":
    main()
