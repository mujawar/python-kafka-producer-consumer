from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'numbertest', # topic
     group_id=None,
     bootstrap_servers=['localhost:9092'], # bootstrap server
     api_version=(0,11,3),
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

print('Receiving message...')
for message in consumer:
    print('Message: ' + str(message.value))