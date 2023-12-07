from pyrogram import Client

import schedule
import time
import random



user = [7336704]
user_hash = ["8ea5bf9c0112677e42565f45f375a9b2"]
from telethon import TelegramClient
import schedule
import time
import random

api_id = user[0]
api_hash = user_hash[0]

clients = [TelegramClient(str(i), api_id=api_id, api_hash=api_hash) for i in range(1, 52)]

for client in clients:
    client.start()

with open("ShillingSentence.txt", encoding="utf8") as file:
    sentences = file.readlines()

def get_random_number():
    return random.randint(0, 100)

def send_message(client):
    chat_name = 'CHAT_NAME'
    random_number = get_random_number()
    
    with client:
        client.join_chat(chat_name)
        client.send_message(chat_name, sentences[random_number])

def job():
    random_client = random.choice(clients)
    send_message(random_client)

time_send = random.randint(5, 20)
schedule.every(time_send).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

