from kafka import KafkaProducer
import time
import json

def connect_kafka_producer():
    _producer = None
    try:
        # Connect to Kafka - assuming local host but in prod this will have to be configured, and should come from config file or KV.
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], 
                                  value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer

def publish_message(producer_instance, topic_name, data):
    try:
        producer_instance.send(topic_name, value=data)
        producer_instance.flush()
        print(f'Message published successfully. Data: {data}')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))

if __name__ == '__main__':
    topic = 'your_kafka_topic'
    print('Initializing Kafka producer')
    producer = connect_kafka_producer()
    
    if producer is not None:
        for data in generate_data():
            publish_message(producer, topic, {'number': data})
            time.sleep(2)  # Send data every 2 seconds
    else:
        print('Producer connection failed')
