from kafka_util import consumer


def main():
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            print('Waiting...')
        elif msg.error():
            print(f'ERROR: {msg.error()}')
        else:
            print(f'Consumed event from topic {msg.topic()} value = {msg.value().decode("utf-8")}')


if __name__ == '__main__':
    main()