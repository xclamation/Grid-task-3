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

# Testing
To test the application, you can send a message to RabbitMQ using the rabbitmqadmin tool. For example, to send a message with the routing key add and the payload {"x": 1, "y": 2}, run the following command:
```bash
rabbitmqadmin publish exchange=my_exchange routing_key=add payload='{"x": 1, "y": 2}'
```
The consumer should receive the message and write the result of the calculation (3 in this case) to the log.

If you send a message with an invalid payload or a nonexistent routing key, the consumer should reject the message and send it to the DLQ.

# Stopping the Containers

To stop the producer and consumer containers, run the following command:
```sh
docker-compose down
```

This will also remove the containers and the network.
