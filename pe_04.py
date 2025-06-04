# Fox, G. PE 04 While, If, Random
import time
import random

# Section 1
response = int(input("How many seconds would you like for your countdown?\n> "))
while response > 0:
    print(f"Lauching in: {response}")
    response -= 1
    time.sleep(1)
print("Time is up. Launching the magic eightball now.")

# Section 2
responses = [
    "It is Certain",
    "Yes",
    "You may rely on it",
    "Ask again later",
    "Reply hazy, try again",
    "My reply is NO WAY",
    "My sources say no",
    "You've Got to be Kidding"
]
response = None
while True:
    response = input("Ask the 🎱 a question, or enter 'no' to quit.\n> ")
    if str(response).lower() == 'no':
        break
    print(random.choice(responses))
print("Goodbye, see you next time!")