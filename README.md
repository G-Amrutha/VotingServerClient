# Voting System

This project consists of a simple client-server voting system implemented using Python's socket programming. The system allows a client to send votes to a server, which tallies the votes and determines a winner between two candidates.

## Files

- `VoteClient.py`: The client script that simulates voting by sending votes for two candidates to the server.
- `VoteServer.py`: The server script that receives votes from the client, counts them, and determines the winner.

## Requirements

- Python 3.x

## Usage

### Running the Server

1. Open a terminal and navigate to the directory containing `VoteServer.py`.
2. Run the server script:

   ```bash
   python VoteServer.py
   ```

   The server will start and listen for incoming connections on port 5555.

### Running the Client

1. Open another terminal and navigate to the directory containing `VoteClient.py`.
2. Run the client script:

   ```bash
   python VoteClient.py
   ```

   The client will connect to the server, send 10 random votes, and print the server's responses.

### How It Works

- The client randomly selects one of the two candidates ("JohnD" or "JaneD") and sends the vote to the server.
- The server receives each vote, updates the vote count, and sends a confirmation message back to the client.
- After receiving 10 votes, the server calculates the winner and sends the results to the client.
- The server can handle multiple sessions of voting by resetting the vote count after each session.

## Note

- Ensure that both the server and client are running on the same machine or adjust the `serverName` in `VoteClient.py` to the appropriate IP address if running on different machines.
- The server resets the voting counts after each session, allowing for repeated testing without restarting the server.
