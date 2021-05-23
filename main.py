import random
randNumber = random.randint(1, 100)
#print(randNumber)
user = None
guesses = 0
while (user != randNumber):
    user = int(input("Guess the Number:"))
    if user ==randNumber:
        print("Good you guess the right number")
    else:
        if (user > randNumber):
            print("You guess it wrong.Enter a smaller no!")
        else:
            print("you guess it wrong .Enter a larger no.")
        guesses += 1
print(f"You guess the number in {guesses} times")
with open("highscore.txt","r") as f:
    hiscore = int(f.read())
if hiscore<user or hiscore == None:   
    with open("highscore.txt","w") as f:
        f.write(str(user))
