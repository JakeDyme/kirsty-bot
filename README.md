# kirsty-bot
 
A tiny chat bot written in under 10 lines of code.

This was just a fun experiment to see how many lines of code I could squeeze a chat bot into. Its very basic, just enough to have some novelty value. It emulates what might be considered "coffee conversation", that is, routine responses to routine questions, with some built-in awkwardness. There's no persistence beyond the process in the main code, but there is a variant "-with-memory" that does create a file for learnt response mappings. The bot should theoretically get better over time after many conversations with different people. A measure of improvement could be: how many responses it can solicit from a user.

## How to use it
Just keep talking to it. As it learns appropriate responses, it will start responding in more interesting ways. You should restart the conversation often. To restart a conversation, just say hello and go from there.

## The coffee-chat algorithm:
-----------------------------
```
Loop  
    Get the new input from the user.
    Store the previous output and the new input as a response mapping.  
    If the new input has a response mapping,   
        then output the mapped response.  
    Otherwise,   
        output the new input.
```

## The Code (Python, no memory)
You can paste this into any [online python interpreter](https://replit.com/languages/python3) to see it in action...
This version is only persisted in-memory (closing the app will lose any learnt behavior)
```Python
import time
responseTo = {}
whatKirstySaid = 'Hello'
while True:
    whatYouSaid = input(f'Kirsty: um, {whatKirstySaid}\nYou: ')
    responseTo[whatKirstySaid] = whatYouSaid
    kirstyKnows = whatYouSaid in responseTo
    whatKirstySaid = responseTo[whatYouSaid] if kirstyKnows else whatYouSaid
    time.sleep(1)
```

## Example conversation:
``` BASH
(--- Conversation 1 -------------------------------------)
Kirsty: "um, hello"                           <-- Init
You: "Hi"
Kirsty: "um, hi"                              <-- Repeated
You: "how are you"        
Kirsty: "um, how are you"                     <-- Repeated
You: "i'm good, thanks, how are you?"
Kirsty: "um, i'm good, thanks, how are you?"  <-- Repeated
You: "good thanks"
Kirsty: "um, good thanks"                     <-- Repeated
You: "ok"
Kirsty: "um, ok"                              <-- Repeated
You: "bye"
Kirsty: "um, bye"                             <-- Repeated
(--- Conversation 2 -------------------------------------)
You: "hello"
Kirsty: "um, hi"                              <-- LEARNT Behavior
You: "how are you"                        
Kirsty: "um, i'm good, thanks, how are you?"  <-- LEARNT Behavior
You: "how was your weekend?"
Kirsty: "um, how was your weekend?"           <-- Repeated
You: "very busy"            
Kirsty: "um, very busy"                       <-- Repeated
You: "ok"
Kirsty: "um, bye"                             <-- LEARNT Behavior
You: "bye"            
```

