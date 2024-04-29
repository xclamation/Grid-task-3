import pika
import time

def connect_to_rabbitmq():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
            return connection
        except pika.exceptions.AMQPConnectionError:
            print(" [x] Failed to connect to RabbitMQ, retrying in 5 seconds...")
            time.sleep(5)

connection = connect_to_rabbitmq()
channel = connection.channel()

channel.exchange_declare(exchange='my_exchange', exchange_type='direct')

def publish(routing_key, message):
    channel.basic_publish(exchange='my_exchange', routing_key=routing_key, body=message)
    print(f" [x] Sent '{message}' with routing key '{routing_key}'")

if __name__ == '__main__':
    while True:
        publish('operation.add', '1+1')
        time.sleep(1)
