#Guessing Game! 
#Game will pick a number 1-100, User will have to find the number
#Game will interact with the user telling them to guess higher or lower

 
#Import the module to allow us to gen random numbers
import random

#GTN:Guess The Number
def GtN():
    print("I'm going to think of a number...")
    print("Right ive got one, see if you can guess it")

    #Generate a random number and assign it to: Generated_Number
    Generated_Number = random.randint(1,100)
    #Set the Guess counter to 0
    Gcount = 0

    while True:
        #Get user guess, as an integer
        UserGuess=int(input("What's your guess?"))
        Gcount += 1
        #Check Gcount
        if UserGuess == Generated_Number:
            print(f"You've only gone and bloody done it! It was {Generated_Number} 
                  and it only took you {Gcount} tries.")
            break
        elif UserGuess < Generated_Number:
            print("Computer says no. Too Low!")
        else:
            print("Computer says no, Too High!")

#Main Block
#Trigger the GtN function
if __name__ == "__main__":
    GtN()


    