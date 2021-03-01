from telethon import TelegramClient, events, sync
import config
import postgres
import utils as u
import time
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

client = TelegramClient('anon', config.API_ID, config.API_HASH)
connection =  postgres.dbConnection();
print(connection)
client.start()
start = "10:10:00"
end = "22:00:00"


def main():
    current_time = u.getCurrentTime()
    print("current time:", current_time)
    if current_time >= start and current_time <= end:
        rows = postgres.dbReader(connection)
        message = ''
        for row in rows:
            message += u.messageFormat(row[0]) + f'{row[1]}\n'

        message += f"**UMUMIY REGISTRATSIYADAN O'TGAN USERLAR SONI:** {rows[0][3]}"

        entity = client.get_entity(PeerChat(config.GROUP_ID))
        message = client.send_message(entity, message)
        print("Jo'natildi soat:", current_time)
print("kevoti")
while True:
    time.sleep(1)
    main()
    # time.sleep(15)
    time.sleep(7200)
client.run_until_disconnected()
