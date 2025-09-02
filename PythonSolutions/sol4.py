from datetime import datetime

def print_current_time():
    now = datetime.now()
    print(now.strftime("%I:%M:%S %p"))

print_current_time()