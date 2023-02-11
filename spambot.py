from pyrogram import Client

import schedule
import time
import random



user = [7336704]
user_hash = ["8ea5bf9c0112677e42565f45f375a9b2"]

app = Client("1", api_id=user[0], api_hash=user_hash[0])
app1 = Client("2", api_id=user[0], api_hash=user_hash[0])
app2 = Client("3", api_id=user[0], api_hash=user_hash[0])
app3 = Client("4", api_id=user[0], api_hash=user_hash[0])
app4 = Client("5", api_id=user[0], api_hash=user_hash[0])
app5 = Client("6", api_id=user[0], api_hash=user_hash[0])
app6 = Client("7", api_id=user[0], api_hash=user_hash[0])
app7 = Client("8", api_id=user[0], api_hash=user_hash[0])
app8 = Client("9", api_id=user[0], api_hash=user_hash[0])
app9 = Client("10", api_id=user[0], api_hash=user_hash[0])
app10= Client("11", api_id=user[0], api_hash=user_hash[0])
app11= Client("51", api_id=user[0], api_hash=user_hash[0])
app12= Client("12", api_id=user[0], api_hash=user_hash[0])
app13= Client("13", api_id=user[0], api_hash=user_hash[0])
app14= Client("14", api_id=user[0], api_hash=user_hash[0])
app15= Client("15", api_id=user[0], api_hash=user_hash[0])
app16= Client("16", api_id=user[0], api_hash=user_hash[0])
app17= Client("17", api_id=user[0], api_hash=user_hash[0])
app18= Client("18", api_id=user[0], api_hash=user_hash[0])
app19= Client("19", api_id=user[0], api_hash=user_hash[0])
app20= Client("20", api_id=user[0], api_hash=user_hash[0])
app21= Client("21", api_id=user[0], api_hash=user_hash[0])
app22= Client("22", api_id=user[0], api_hash=user_hash[0])
app23= Client("23", api_id=user[0], api_hash=user_hash[0])
app24= Client("24", api_id=user[0], api_hash=user_hash[0])
app25= Client("25", api_id=user[0], api_hash=user_hash[0])
app26= Client("26", api_id=user[0], api_hash=user_hash[0])
app27= Client("27", api_id=user[0], api_hash=user_hash[0])
app28= Client("28", api_id=user[0], api_hash=user_hash[0])
app29= Client("29", api_id=user[0], api_hash=user_hash[0])
app30= Client("30", api_id=user[0], api_hash=user_hash[0])
app31= Client("31", api_id=user[0], api_hash=user_hash[0])
app32= Client("32", api_id=user[0], api_hash=user_hash[0])
app33= Client("33", api_id=user[0], api_hash=user_hash[0])
app34= Client("34", api_id=user[0], api_hash=user_hash[0])
app35= Client("35", api_id=user[0], api_hash=user_hash[0])
app36= Client("36", api_id=user[0], api_hash=user_hash[0])
app37= Client("37", api_id=user[0], api_hash=user_hash[0])
app38= Client("38", api_id=user[0], api_hash=user_hash[0])
app39= Client("39", api_id=user[0], api_hash=user_hash[0])
app40= Client("40", api_id=user[0], api_hash=user_hash[0])
app41= Client("41", api_id=user[0], api_hash=user_hash[0])
app42= Client("42", api_id=user[0], api_hash=user_hash[0])
app43= Client("43", api_id=user[0], api_hash=user_hash[0])
app44= Client("44", api_id=user[0], api_hash=user_hash[0])
app45= Client("45", api_id=user[0], api_hash=user_hash[0])
app46= Client("46", api_id=user[0], api_hash=user_hash[0])
app47= Client("47", api_id=user[0], api_hash=user_hash[0])
app48= Client("48", api_id=user[0], api_hash=user_hash[0])
app49= Client("49", api_id=user[0], api_hash=user_hash[0])
app50= Client("50", api_id=user[0], api_hash=user_hash[0])
app51= Client("51", api_id=user[0], api_hash=user_hash[0])
    
    


f = open("ShillingSentence.txt",  encoding="utf8")
f = f.readlines()
user_app = [app,app1,app2,app3,app4,app5,app6,app7,app8,app9,app10,app11,app12,app13,app14,app15,app16,app17,app18,app19,app20,app21,app22,app23,app24,app25,app26,app27,app28,app29,app30
,app31,app32,app33,app34,app35,app36,app37,app38,app39,app40,app41,app42,app43,app44,app45,app46,app47,app48,app49,app50]


def num():
    answer = set()
    sampleSize = 10
    answerSize = 0
    i = 0
    while (i != 100):
        r = random.randint(0,100)
        if r not in answer:
            answerSize += 1
            answer.add(r)
        i +=1

        return r

def send():

    num_app = (random.randint(1, 50))
    print(num_app)
    num_app = int(num_app)
    print(num_app)
    with user_app[num_app]:
        r = num()
        user_app[num_app].join_chat('ElephantTokenBSC')
        user_app[num_app].send_message("ElephantTokenBSC",f[r])

time_send = (random.randint(5, 20))
schedule.every(time_send).seconds.do(send)
while True:
    schedule.run_pending()
    time.sleep(1)

