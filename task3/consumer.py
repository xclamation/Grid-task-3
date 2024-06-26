import pika
import traceback
import time
import json

def on_message(channel, method_frame, header_frame, body):
    try:
        routing_key = method_frame.routing_key
        message = json.loads(body.decode())
        print(f" [x] Received '{message}' with routing key '{routing_key}'")

        # Process the message and apply operations
        if routing_key == 'operation.add':
            result = message['x'] + message['y']
            print(f" [x] Result: {result}")
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        else:
            print(f" [x] Unknown routing key '{routing_key}'")
            channel.basic_reject(delivery_tag=method_frame.delivery_tag, requeue=True)
    except Exception:
        print(f" [x] Error processing message: {traceback.format_exc()}")
        channel.basic_reject(delivery_tag=method_frame.delivery_tag, requeue=False)

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
channel.queue_declare(queue='my_queue', auto_delete=False)
channel.queue_bind(exchange='my_exchange', queue='my_queue', routing_key='operation.#')

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='my_queue', on_message_callback=on_message, auto_ack=False)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
