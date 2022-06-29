import random

#testicles = [1, 3, 5, 7, 45]

#print( "the complete list of testes is: " + str(testicles))

#random_teste = random.choice(testicles)

#print ("The randomly selected testicle is : " + str(random_teste))

TIE = "tie!!\n"

ROCK = "Rock"
PAPER = "Paper"
SCISSORS = "Scissors"

STEVE_WINS = "STONE COLD WINS!!!\n"
ROCK_WINS = "THE ROCK WINS!!!\n"

STEVE_NAME = "Stone Cold Steve Austin"
ROCK_NAME = 'Dwayne "The Rock" Johnson'

PROMPT_USER = 'Rock, paper, or scissors baby? '
YOU_WIN = "YOU WIN!!!\n"

RPS = [ROCK, PAPER, SCISSORS]

winner = 0

while winner == 0:
    theRock = random.choice(RPS)
    stoneCold = random.choice(RPS)


    print (f"{ROCK_NAME} picked: {str(theRock)}!")
    print (f"{STEVE_NAME} picked: {str(stoneCold)}!")

    if theRock == stoneCold:
            print (TIE)
    elif theRock == PAPER:
        if stoneCold == SCISSORS:
                print (STEVE_WINS)
                winner = STEVE_NAME
        else:
                print (ROCK_WINS)
                winner = ROCK_NAME
    elif theRock == SCISSORS:
        if stoneCold == ROCK:
                print (STEVE_WINS)
                winner = STEVE_NAME
        else:
                print (ROCK_WINS)
                winner = ROCK_NAME
    elif theRock == ROCK:
        if stoneCold == PAPER:
                print (STEVE_WINS)
                winner = STEVE_NAME
        else:
                print (ROCK_WINS)
                winner = ROCK_NAME

#SECOND MATCH! THIS ONE IS FOR THE BELT
print (f"Want to square off with {str(winner)}?")
face = input(PROMPT_USER)
heel = random.choice(RPS)

print (f"You picked: {str(face)}!")
print (f"{str(winner)} picks: {str(heel)}!!!")

if heel.casefold() == face.casefold():
        print (TIE)
elif heel.casefold() == PAPER:
    if face.casefold() == SCISSORS:
            print (YOU_WIN)
            
    else:
            print (f"{str(winner)} WINS!!!")
            
elif heel.casefold() == SCISSORS:
    if face.casefold() == ROCK:
            print (YOU_WIN)
            
    else:
            print (f"{str(winner)} WINS!!!")
            
elif heel.casefold() == ROCK:
    if face.casefold() == PAPER:
            print (YOU_WIN)
            
    else:
            print (f"{str(winner)} WINS!!!")
