# Multi-Threaded Wallet Server

## Description

This repository contains a Python-based multi-threaded wallet system designed to manage and perform resource transactions. It supports both blocking and non-blocking transaction methods and is capable of handling concurrent requests using a socket-based server for real-time resource management.

Key Features:
- Multi-threading support for handling concurrent transactions.
- Thread-safe resource management with synchronization mechanisms.
- Socket server for communication between client and server.
- Supports multiple types of transactions (blocking and non-blocking).

## Files

- `wallet-server.py`: Main server implementation handling transactions and requests.
- `wallet.py`: Contains the Wallet class and methods to interact with the wallet.
- `ping-pong.py`: Basic implementation for the ping-pong transaction.
- `ping-pong-transaction.py`: A specialized version of the ping-pong transaction with additional handling.
- `degree.py`, `gacha.py`, `hedgehog-rat.py`, `hedgehog-simple.py`: Examples of various scenarios utilizing the wallet system.
- `test_coding_rules.py`, `test_part_1.py`, `test_part_2.py`, `test_part_3.py`, `test_part_4.py`, `test_provided_files.py`: Test scripts to validate the functionality and ensure proper coding standards.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/abbasmirza10/multi-threaded-wallet-server.git
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the server:

bash
Copy code
python wallet-server.py
Usage
The server listens for incoming requests from clients to perform resource transactions. Clients can connect via sockets to request transactions, either blocking or non-blocking. The server processes each transaction and manages wallet balances in a thread-safe manner.

Contributing
Feel free to fork this repository, make changes, and create pull requests. Contributions to improve the functionality or add new features are welcome.

License
This project is licensed under the MIT License - see the LICENSE file for details.

typescript
Copy code

You can update and modify this `README.md` according to any further specifics or changes to the project.
