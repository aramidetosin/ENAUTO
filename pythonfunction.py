import datetime

def greet(name):
    dt = datetime.datetime.now()
    if dt.hour <= 11:
        greeting = "morning"
    elif dt.hour <= 17:
        greeting = "afternoon"
    else:
        greeting = "evening"
    
    return greeting, name

username = greet('tosin')
print(f"Hello {username[1].capitalize()}, Good {username[0].capitalize()}")