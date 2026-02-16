import random
Jokes=[] # jokes list
with open("randomJokes.txt", "r") as file:  #loads jokes on list and separates setup and punchline
    for line in file:
        line = line.strip()
        parts = line.split("?", 1)
        setup = parts[0].strip() + "?"
        punchline = parts[1].strip()
        Jokes.append((setup, punchline))

while True:
    print("\nAlexa: Ask me a joke")
    Inputed=input("Say 'Alexa, tell me a joke' or 'quit': ")
    if "joke" in Inputed:
        joke = random.choice(Jokes)
        i1, i2 = joke #returns the setup and punchline

        print("Alexa: " + i1)
        input("Say someting: ")
        print("Alexa: " + i2)
    elif Inputed in "quit":
        print("Alexa: Bye-bye")
        break
    else:
        print("Alexa: I'm sorry, I didn't quite get that.")