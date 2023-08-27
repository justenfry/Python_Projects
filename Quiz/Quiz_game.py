# Quiz game

play = input("Do you want to play a game? ")

if play.lower() != "yes":
    quit()
print("Lets have some fun!!!")

score = 0
count = 0
answer = input("What symbol is used for addition? ")
count += 1
if answer == "+":
    print("You are correct!")
    score += 1
else:
    print("Sorry, that was incorrect.")

answer = input("What symbol is used for subtraction? ")
count += 1
if answer == "-":
    print("You are correct!")
    score += 1
else:
    print("Sorry, that was incorrect.")

answer = input("What symbol is used for division? ")
count += 1
if answer == "/":
    print("You are correct!")
    score += 1
else:
    print("Sorry, that was incorrect.")

answer = input("What symbol is used for multiplication? ")
count += 1
if answer == "*":
    print("You are correct!")
    score += 1
else:
    print("Sorry, that was incorrect.")

answer = input("What symbol is used for equals? ")
count += 1
if answer == "=":
    print("You are correct!")
    score += 1
else:
    print("Sorry, that was incorrect.")

answer = input("What symbol is used for greater than? ")
count += 1
if answer == ">":
    print("You are correct!")
    score += 1
else:
    print("Sorry, that was incorrect.")

answer = input("What symbol is used for greater than or equal to? ")
count += 1
if answer == ">=":
    print("You are correct!")
    score += 1
else:
    print("Sorry, that was incorrect.")

answer = input("What symbol is used for less than? ")
count += 1
if answer == "<":
    print("You are correct!")
    score += 1
else:
    print("Sorry, that was incorrect.")

answer = input("What symbol is used for less than or equal to? ")
count += 1
if answer == "<=":
    print("You are correct!")
    score += 1
else:
    print("Sorry, that was incorrect.")

answer = input("Did you enjoy the quiz? ")
count += 1
if answer.lower() == "yes":
    print("You are correct!")
    score += 1
else:
    print("Sorry, that was incorrect.")

print("Your score is", score, "out of", count)
