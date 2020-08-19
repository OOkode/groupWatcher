from telethon import TelegramClient, events, sync
import env,time

api_id = env.API_ID
api_hash = env.API_HASH
chat = env.CHAT
SLEEP_MINUTES = 60*3
MIN_MSG_ID = float('-inf')
KEYWORDS = ['#monaco','#boyeroycamagüey','#boyerosycamaguey','#boyerosycamagüey','#camagüeyyboyeros','#camagüeyyboyero','#boyero','#camagüey','#boyeros','#ventoysantacatalina','#split','#splits']

# telethon_client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

client = TelegramClient('session1', api_id, api_hash)
client.start(phone=env.PHONE,password=env.PASSWORD)


def detect_relevantinfo(messages):

    print("Checking messages\n")
    for message in messages:
        for keyword in KEYWORDS:
            message_lower = message.message.lower()
            if keyword in message_lower:
                message.forward_to(chat)
                

while 1:
    print('start')

    messages = client.get_messages('DondeHayEnLaHabana',limit=50,min_id=MIN_MSG_ID)

    if len(messages) > 0:
        MIN_MSG_ID = messages[0].id
        print(f'Min message id: {MIN_MSG_ID}, {messages[0].message}\n')
        detect_relevantinfo(messages)

    print(f'Sleeping for {SLEEP_MINUTES} minutes\n')
    time.sleep(SLEEP_MINUTES)

