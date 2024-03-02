# Cortex

The Cortex is a framework by Tenzro designed to facilitate Federated Learning across distributed devices securely and privately. This framework enables the training of machine learning models across multiple devices while preserving user privacy by keeping data decentralized.

## Getting Started

To get started with Cortex, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/tenzro/cortex.git

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

3. Run the server:
    
    ```bash
    python server.py

4. Run the client:

    ```bash
    python client.py

## Features

- Federated Learning: Train machine learning models across distributed devices while preserving user privacy.
- Flower Integration: This initial version of Cortex is integrated with the Flower framework for implementing Federated Learning algorithms.
- Simple CNN Model: Includes a simple Convolutional Neural Network (CNN) model for training on the CIFAR-10 dataset.
- Token Issuance: Users can contribute training data and receive tokens in return.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the Mozilla Public License Version 2.0.