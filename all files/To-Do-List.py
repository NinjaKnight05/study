# from plyer import notification
# from datetime import datetime, date, time
# notification.notify(
#     title="Alert",
#     message="kive aa singh",
#     timeout=3
# )
# print(datetime.now())


from plyer import notification
from datetime import datetime
import time

target_time=input('Enter Time like (13:00):')
message1=input('write Message: ')
while True:
    now=datetime.now().strftime("%H:%M")
    if now ==target_time :
        notification.notify(
            title="Time Alert!",
            message=message1,
            timeout=5
        )
    time.sleep(1)

        

