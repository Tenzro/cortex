import flwr as fl

# This code initializes and starts the Flower server, which acts as the central coordinator for Federated Learning in Cortex.

# Start Flower server
fl.server.start_server(
  server_address="0.0.0.0:8080",  # Cortex: Flower server listens on all available network interfaces at port 8080
  config=fl.server.ServerConfig(num_rounds=3),  # Cortex: Configure Flower server to run for 3 rounds of federated learning
)
