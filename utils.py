from datetime import datetime

def messageFormat(s):
    sub = 36 - len(s)
    just = ''
    for i in range(sub):
        just += "--"
    return f"{s}{just}"


def getCurrentTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time