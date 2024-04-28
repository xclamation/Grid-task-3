# Prerequisites
Docker

# Getting Started

1. Clone the repository:
```bash
git clone https://github.com/xclamation/Grid-task-3.git
```

2. Navigate to the project directory where docker-compose.yml is located:

```bash
cd /project/directory
````

3. Start the RabbitMQ container:
```bash
docker-compose up -d rabbitmq
```

4. Start the producer and consumer containers:
```bash
docker-compose up
```
The producer will start sending messages to RabbitMQ, and the consumer will start processing them.

# Stopping the Containers

To stop the producer and consumer containers, run the following command:
```sh
docker-compose down
```

This will also remove the containers and the network.
