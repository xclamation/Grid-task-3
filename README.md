Prerequisites
Docker

Getting Started

Clone the repository:
```sh
git clone https://github.com/xclamation/simple-pub-sub-app.git
```sh

Change into the project directory:
```sh
cd simple-pub-sub-app
```sh

Start the RabbitMQ container:
```sh
docker-compose up -d rabbitmq
```sh

Start the producer and consumer containers:
```sh
docker-compose up
```sh
The producer will start sending messages to RabbitMQ, and the consumer will start processing them.

Stopping the Containers

To stop the producer and consumer containers, run the following command:
```sh
docker-compose down
```sh

This will also remove the containers and the network.
