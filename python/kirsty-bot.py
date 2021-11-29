import time
responseTo = {}
whatKirstySaid = 'hello'
while True:
    whatYouSaid = input(f'Kirsty: um, {whatKirstySaid}\nYou: ').lower()
    responseTo[whatKirstySaid] = whatYouSaid
    kirstyKnows = whatYouSaid in responseTo
    whatKirstySaid = responseTo[whatYouSaid] if kirstyKnows else whatYouSaid
    time.sleep(1)