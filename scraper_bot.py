from telethon import TelegramClient, events, sync
import env, time, json

api_id = env.API_ID
api_hash = env.API_HASH
chat = env.CHAT
log_chat = env.LOG_CHAT
SLEEP_MINUTES = 60 * 10

with open('info.json','r') as info_file:
    MIN_MSG_ID_json = json.load(info_file)
    MIN_MSG_ID = json.loads(MIN_MSG_ID_json)['MIN_MSG_ID']

KEYWORDS = ['#monaco', '#boyeroycamagüey', '#boyerosycamaguey', '#boyerosycamagüey', '#camagüeyyboyeros',
            '#camagüeyyboyero', '#boyero', '#camagüey', '#boyeros', '#ventoysantacatalina', '#split', '#splits',
            '#freezer','#refrigerador']
SECONDARY_KEYWORDS = ['refrigerador','split','refrigeradores','splits']

client = TelegramClient('session1', api_id, api_hash)
client.start(phone=env.PHONE, password=env.PASSWORD)


def detect_relevantinfo(messages,keywords):
    print("Checking messages\n")

    for message in messages:
        try:
            message_lower = message.message.lower()
            print(message_lower)
        except AttributeError as e:
            print("El mensaje no era valido\n")
            message_lower = ''

        for keyword in keywords:
            if keyword in message_lower:
                print(f'mensaje enviado: {message_lower}\n')
                message.forward_to(chat)


while 1:
    print('start')
    # client.send_message(entity=log_chat,
    #                     message=f'start')


    messages = client.get_messages('DondeHayEnLaHabana', limit=500,min_id=int(MIN_MSG_ID))

    if len(messages) > 0:
        MIN_MSG_ID = messages[0].id
        with open('info.json','w') as info_file:
            json_string = "{'MIN_MSG_ID': '" + str(MIN_MSG_ID) + "'}"
            json_string = {"MIN_MSG_ID": str(MIN_MSG_ID)}
            json_string = json.dumps(json_string)
            json.dump(json_string, info_file)
        # client.send_message(entity=log_chat,
        #                     message=f'Min message id: {MIN_MSG_ID}, {messages[0].message}\n')
        # print(f'Min message id: {MIN_MSG_ID}, {messages[0].message}\n')
        detect_relevantinfo(messages,KEYWORDS)

    print(f'Sleeping for {SLEEP_MINUTES} minutes\n')
    # client.send_message(entity=log_chat,
    #                     message=f'Sleeping for {SLEEP_MINUTES} minutes\n')
    time.sleep(SLEEP_MINUTES)
