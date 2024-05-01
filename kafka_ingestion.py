from kafka import KafkaConsumer
import json

def kafka_ingestion():
    consumer = KafkaConsumer('ad_data_topic', bootstrap_servers='localhost:9092')
    for msg in consumer:
        data = json.loads(msg.value)
        # Process the data further

if __name__ == "__main__":
    kafka_ingestion()
