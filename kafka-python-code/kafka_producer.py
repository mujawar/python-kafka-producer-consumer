from time import sleep
from json import dumps
from kafka import KafkaProducer
import json
import pandas as pd

df = pd.read_csv('./2016_US_election_tweets_100k.csv')
josndata =df.to_dict('records')
# print(josndata)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         api_version=(0,11,3),
                         value_serializer=lambda x:dumps(x).encode('utf-8'))
print('Processing...')
for row_data in josndata:
    # print("data----------->",row_data)
    # send message
    producer.send('numbertest1', row_data)
    print('send data: ' + str(row_data))
    # sleep 2s
    sleep(2)