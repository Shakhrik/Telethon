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
start = "08:00:00"
end = "22:05:00"



def main():
    current_time = u.getCurrentTime()
    print("Current time: ",current_time)
    if (current_time >= start and current_time <= end) or (current_time == "22:00:00" or current_time == "08:00:00" or current_time == "10:00:00"):
        rows = postgres.dbReader(connection)
        message = f''
        for row in rows:
            message += u.messageFormat(row[0]) + f'{row[1]}\n'

        message += f"**UMUMIY REGISTRATSIYADAN O'TGAN USERLAR SONI:** {rows[0][3]}"

        entity = client.get_entity(PeerChannel(config.GROUP_ID))
        message = client.send_message(entity, message)
        print("Jo'natildi soat:", current_time)
        return True
    return False

while True:
    res = main()
    if res:
        time.sleep(7200)
client.run_until_disconnected()
