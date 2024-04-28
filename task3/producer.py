import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.exchange_declare(exchange='my_exchange', exchange_type='direct')

def publish(routing_key, message):
    channel.basic_publish(exchange='my_exchange', routing_key=routing_key, body=message)
    print(f" [x] Sent '{message}' with routing key '{routing_key}'")

if __name__ == '__main__':
    while True:
        publish('operation.add', '1+1')
        time.sleep(1)