import threading
import socket
from wallet import Wallet

wallet = Wallet() # the only global variable you should use

def process_request(request):
    command = request.split()
    if command[0] == 'GET':
        return str(wallet.get(command[1]))
    elif command[0] == 'MOD':
        return str(wallet.change(command[1], int(command[2])))
    elif command[0] == 'TRY':
        return str(wallet.try_change(command[1], int(command[2])))
    elif command[0] == 'TRAN':
        transaction = {command[i]: int(command[i+1]) for i in range(1, len(command), 2)}
        return str(wallet.transaction(**transaction))
    elif command[0] == 'EXIT':
        return None
    else:
        return 'Invalid command'

def handle_client(client_socket):
    while True:
        request = client_socket.recv(1024).decode('utf-8').replace('\r', '').strip()
        if not request:
            break
        response = process_request(request)
        if response is None:
            break
        client_socket.send((response + '\n').encode('utf-8'))
    client_socket.close()

def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

def create_wallet_server(local_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', local_port))
    server_socket.listen(100)
    try:
        while True:
            accept_connection(server_socket)
    except KeyboardInterrupt:
        print('Server shutdown')
    finally:
        server_socket.close()

if __name__ == '__main__':
  # parses command-line arguments, ensuring all implementations are invoked the same way
  import getopt
  import sys
  
  local_port = 34000
  optlist, args = getopt.getopt(sys.argv[1:], 'p:')
  for arg in optlist:
    if arg[0] == '-p': local_port = int(arg[1])
  print("Launching wallet server on :"+str(local_port))
  create_wallet_server(local_port)
