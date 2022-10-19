from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         api_version=(0,11,3),
                         value_serializer=lambda x:dumps(x).encode('utf-8'))
print('Processing...')
for num in range(1000):
    data={'number': num}
    # send message
    producer.send('numbertest', data)
    print('send data: ' + str(data))
    # sleep 2s
    sleep(2)