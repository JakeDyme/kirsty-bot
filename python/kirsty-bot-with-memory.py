import time, ast, os
memoryMode = 'r' if os.path.isfile('kirsties-memory.txt') else 'w+' 
with open('kirsties-memory.txt', mode=memoryMode) as f: memory = f.read()
responseTo = {} if memory == '' else ast.literal_eval(memory)
whatKirstySaid = 'Hello'
while True:
    whatYouSaid = input(f'Kirsty: um, {whatKirstySaid}\nYou: ').lower()
    responseTo[whatKirstySaid] = whatYouSaid
    kirstyKnows = whatYouSaid in responseTo
    whatKirstySaid = responseTo[whatYouSaid] if kirstyKnows else whatYouSaid
    with open('./kirsties-memory.txt', mode='w') as f: f.write(str(responseTo))
    time.sleep(1)