import random

#testicles = [1, 3, 5, 7, 45]

#print( "the complete list of testes is: " + str(testicles))

#random_teste = random.choice(testicles)

#print ("The randomly selected testicle is : " + str(random_teste))

RPS = ["Rock", "Paper", "Scissors"]

winner = 0

while winner == 0:
    theRock = random.choice(RPS)
    stoneCold = random.choice(RPS)


    print ("Dwayne the Rock Johnson picked: " +str(theRock)+"!")
    print ("Stone Cold Steve Austin picked: " +str(stoneCold)+"!")

    if theRock == stoneCold:
            print ("tie!!")
    elif theRock == "Paper":
        if stoneCold == "Scissors":
                print ("STONE COLD WINS!!!")
                winner = "Stone Cold Steve Austin"
        else:
                print ("THE ROCK WINS!!!")
                winner = 'Dwayne "The Rock" Johnson'
    elif theRock == "Scissors":
        if stoneCold == "Rock":
                print ("STONE COLD WINS!!!")
                winner = "Stone Cold Steve Austin"
        else:
                print ("THE ROCK WINS!!!")
                winner = 'Dwayne "The Rock" Johnson'
    elif theRock == "Rock":
        if stoneCold == "Paper":
                print ("STONE COLD WINS!!!")
                winner = "Stone Cold Steve Austin"
        else:
                print ("THE ROCK WINS!!!")
                winner = 'Dwayne "The Rock" Johnson'

#SECOND MATCH! THIS ONE IS FOR THE BELT
print ('want to square off with '+str(winner)+' ?')
face = input('Rock, paper, or scissors baby?')
heel = random.choice(RPS)
print (str(winner)+' picks: '+str(heel)+'!!!')

if heel.casefold() == face.casefold():
        print ("tie!!")
elif heel.casefold() == "Paper":
    if face.casefold() == "Scissors":
            print ("YOU WIN!!!")
            
    else:
            print (str(winner)+"WINS!!!")
            
elif heel.casefold() == "Scissors":
    if face.casefold() == "Rock":
            print ("YOU WIN!!!")
            
    else:
            print (str(winner)+"WINS!!!")
            
elif heel.casefold() == "Rock":
    if face.casefold() == "Paper":
            print ("YOU WIN!!!")
            
    else:
            print (str(winner)+" WINS!!!")
            

            




