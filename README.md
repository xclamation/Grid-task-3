# Prerequisites
Docker

# Getting Started

Clone the repository:
```bash
git clone https://github.com/xclamation/simple-pub-sub-app.git
```

Change into the project directory:
```bash
cd simple-pub-sub-app
```

Start the RabbitMQ container:
```bash
docker-compose up -d rabbitmq
```

Start the producer and consumer containers:
```bash
docker-compose up
```
The producer will start sending messages to RabbitMQ, and the consumer will start processing them.

# Stopping the Containers

To stop the producer and consumer containers, run the following command:
```sh
docker-compose down
```sh

This will also remove the containers and the network.
