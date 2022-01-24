from dataclasses import dataclass
import random

# Global variables
playAgain = True
straightUpList = []
costOfBets = []

# Defining player info dataclass
@dataclass
class playerInfo:
    name: str
    money: int
    startingMoney: int

# Defining datatype to store he number and colour ball landed on
@dataclass
class rollValue:
    number: int
    colour: str
    parity: str

# Defining the player's bet type and their bet 
@dataclass
class playerBet:
    numberOfBets: int
    typeOfBet: int
    numberBet: int
    colourBet: str
    parityBet: str
    amountBet: int

# Defning colours to be able to print coloured text to the console
class bcolours:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    RED = '\u001b[31m'


# Get a non negative integer function
def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value

# Get a valid number in lowerRange-upperRange
def get_valid_num_in_range(prompt, lowerRange, upperRange, errorMessage):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < lowerRange or value > upperRange:
            print(errorMessage)
            continue
        else:
            break
    return value

# Gets the user to choose between two defined options
def get_valid_two_option_string(prompt, option1, option2, errorMessage):
    while True:

        value = input(prompt)

        if value != option1 and value != option2:
            print(errorMessage)
        else: 
            break

    return value

# Welcoming user to the game + get their name + get their money to play with
def introduction():
    startingMoney = 0
    playerInfo.name = input("Welcome to the game of roulette! What is your name? ")
    print("Hello " + playerInfo.name + """, in this game of roulette, you're allowed to bet on up to 36 of 
the numbers and also you're able to bet on the colour or parity of the roll. 
Goodluck, play at your own risk. We are not responible for any financial losses. Please dont sue us.""")
    playerInfo.money = get_non_negative_int((playerInfo.name + ", how much money have you brought to play with today? "))
    playerInfo.startingMoney = playerInfo.money

def betTypespecification():
        # Clears list so that its ready if user decided to play again
        straightUpList.clear()
        costOfBets.clear()
        # Gets the amount of bets the user wants to make 
        playerBet.numberOfBets = get_valid_num_in_range("How many numbers would you like to bet on? (1-36)", 1, 36, "Please input a number 1-36")
        # Player makes their number bet(s)
        for i in range(playerBet.numberOfBets):
            playerBet.numberBet = get_valid_num_in_range("What number (1-36) would you like to bet on? ", 1, 36, "Please input a number 1-36")
            straightUpList.append(playerBet.numberBet)
            # Print number bet on 
            print("You are betting on: " + str(straightUpList[i]))
            playerBet.amountBet = get_valid_num_in_range("How much money would you like to bet on this number ", 0, playerInfo.money, "Please input a number greater than or equal to 0 and less than or equal to than the money you have")
            costOfBets.append(playerBet.amountBet)
            # Print amount bet on this num
            print("You are betting :$" + str(costOfBets[i]) + " on this number.")
            # Subtract this cost from balance 
            playerInfo.money -= playerBet.amountBet
            # Print new balance
            print("Your new balance is: $" + str(playerInfo.money))
            
            
        # Asks user if they want to also bet on the number and parity 
        answer = get_valid_two_option_string("Would you like to also bet on the parity or a colour? ", "yes", "no", "Please choose \"yes\" or \"no\"")
        # User only wants to bet on the number(s)
        if answer == "no": 
            playerBet.typeOfBet = 1
        # Player wants to bet on the number(s) and the parity or colour 
        else:
            parityOrColour = get_valid_two_option_string("Would you like to  bet on the parity or a colour? ", "parity", "colour", "Please choose \"parity\" or \"colour\"")
            # Player wants to be on number(s) and parity
            if parityOrColour == "parity":
                playerBet.typeOfBet = 2
            # Player wants to be on number(s) and colour
            else:
                playerBet.typeOfBet = 3

            betSpecification()


# User specifies details about their bet like, parity/colour bet on
# This only runs if the player chose to also bet on the colour and parity 
def betSpecification():
    if (playerBet.typeOfBet == 2): # Player bets on the parity + number(s)
        # Player makes their bet 
        playerBet.parityBet = get_valid_two_option_string("Will the number be even or odd? ", "even", "odd", "Please choose \"even\" or \"odd\"")
    # User specifies their bet
    elif (playerBet.typeOfBet == 3): # Player bets on colour + number(s)
        # Player makes their bet 
        playerBet.colourBet = get_valid_two_option_string("What colour would you like to bet on? ", "red", "black", "Please choose \"red\" or \"black\"")



# Simulating a ball roll on the wheel 
def ballRoll():
    # Choosing random int that ball lands on
    rollValue.number = random.randint(0,36)

    # Choosing random colour that ball lands on 
    colourPickerNum = random.randint(0,1)
    if (colourPickerNum == 0):
        rollValue.colour = "red"
    else:
        rollValue.colour = "black"

    # Storing the parity of the roll
    if (rollValue.number % 2) == 0:
        rollValue.parity = "even"
    else:
        rollValue.parity = "odd"

    print("The ball landed on: " + str(rollValue.number) + " " + str(rollValue.colour))

def playerWinningsCheck():
    # money won/lost per bet 
    moneyWon = 0
    # Loop through each of the bets 
    for i in range(0,len(straightUpList)):
        # If the number bet on is correct
        if (straightUpList[i] == rollValue.number):
            print("Your bet on " + str(straightUpList[i]) + " was correct!")
            if (playerBet.typeOfBet == 1):
                # If player only bet on the number
                moneyWon = (costOfBets[i] * 37) / playerBet.numberOfBets
                # You get back the money you bet
                playerInfo.money += costOfBets[i]
                # winnings are added to balance 
                playerInfo.money += moneyWon 
                # Printing amount won 
                print(bcolours.OKGREEN + "Money won: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)  
            # If player also chose to bet on even and odd 
            elif (playerBet.typeOfBet == 2):
                # if the number is even 
                if (straightUpList[i] % 2 == 0):
                    # if player correctly guesses
                    if (playerBet.parityBet == "even"):
                        # You get back the money you bet
                        playerInfo.money += costOfBets[i]
                        # They win double of their winnings 
                        moneyWon = ((costOfBets[i] * 37) / playerBet.numberOfBets) * 2
                        # winnings are added to balance 
                        playerInfo.money += moneyWon
                        # Printing amount won + money total
                        print(bcolours.OKGREEN + "Money won: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)  

                    # if player incorrectly guessed odd 
                    else:
                        # They win half of what they were supposed to
                        moneyWon = ((costOfBets[i] * 37) / playerBet.numberOfBets) / 2
                        # You get back the money you bet
                        playerInfo.money += costOfBets[i]
                        # winnings are added to balance 
                        playerInfo.money += moneyWon
                        # Printing amount won + money total
                        print(bcolours.OKGREEN + "Money won: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)  
                
                # If the number is odd
                else:
                    # if player correctly guesses odd
                    if (playerBet.parityBet == "odd"):
                        # They win double of their bet 
                        moneyWon = ((costOfBets[i] * 37) / playerBet.numberOfBets) * 2
                        # You get back the money you bet
                        playerInfo.money += costOfBets[i]
                        # winnings are added to balance 
                        playerInfo.money += moneyWon
                        # Printing amount won + money total
                        print(bcolours.OKGREEN + "Money won: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)  
                    
                    # if player incorrectly guessed even 
                    else:
                        # They win half of what they were supposed to
                        moneyWon = ((costOfBets[i] * 37) / playerBet.numberOfBets) / 2
                        # You get back the money you bet
                        playerInfo.money += costOfBets[i]
                        # winnings are added to balance 
                        playerInfo.money += moneyWon
                        # Printing amount won + money total
                        print(bcolours.OKGREEN + "Money won: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)     

            # If player also chose to bet on red and black 
            elif (playerBet.typeOfBet == 3):
                # if the number is red 
                if (rollValue.colour == "red"):
                    # if player correctly guesses
                    if (playerBet.colourBet == "red"):
                        # You get back the money you bet
                        playerInfo.money += costOfBets[i]
                        # They win double of their winnings 
                        moneyWon = ((costOfBets[i] * 37) / playerBet.numberOfBets) * 2
                        # winnings are added to balance 
                        playerInfo.money += moneyWon
                        # Printing amount won + money total
                        print(bcolours.OKGREEN + "Money won: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)  

                    # if player incorrectly guessed black 
                    else:
                        # They win half of what they were supposed to
                        moneyWon = ((costOfBets[i] * 37) / playerBet.numberOfBets) / 2
                        # You get back the money you bet
                        playerInfo.money += costOfBets[i]
                        # winnings are added to balance 
                        playerInfo.money += moneyWon
                        # Printing amount won + money total
                        print(bcolours.OKGREEN + "Money won: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)  
                
                # If the number is black
                else:
                    # if player correctly guesses black
                    if (playerBet.parityBet == "black"):
                        # They win double of their bet 
                        moneyWon = ((costOfBets[i] * 37) / playerBet.numberOfBets) * 2
                        # You get back the money you bet
                        playerInfo.money += costOfBets[i]
                        # winnings are added to balance 
                        playerInfo.money += moneyWon
                        # Printing amount won + money total
                        print(bcolours.OKGREEN + "Money won: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)  
                    
                    # if player incorrectly guessed red 
                    else:
                        # They win half of what they were supposed to
                        moneyWon = ((costOfBets[i] * 37) / playerBet.numberOfBets) / 2
                        # You get back the money you bet
                        playerInfo.money += costOfBets[i]
                        # winnings are added to balance 
                        playerInfo.money += moneyWon
                        # Printing amount won + money total1
                        print(bcolours.OKGREEN + "Money won: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)   

        # Number bet is incorrect               
        else:
            print("Your bet on " + str(straightUpList[i]) + " was incorrect")
            if (playerBet.typeOfBet == 1):
                # They lose everything they bet 
                # This was already subtracted when taking the balance 
                moneyWon = costOfBets[i]
                print(bcolours.RED +"Money lost: " + str(moneyWon) + " New money total: " + str(playerInfo.money) + bcolours.ENDC)  

            # If player also chose to bet on even and odd 
            elif (playerBet.typeOfBet == 2):
                # if the number is even 
                if (rollValue.parity == "even"):
                    # if player correctly guesses
                    if (playerBet.parityBet == "even"):

                        # The money they bet is added back
                        playerInfo.money += costOfBets[i] 

                        # They lose half of their bet 
                        moneyWon = costOfBets[i] / 2

                        # loses are subtracted from balance 
                        playerInfo.money -= moneyWon 
                        # Printing amount won + money total
                        print(bcolours.RED +"Money lost: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)  

                    # if player incorrectly guessed odd 
                    else:
                        # They lose double of what they were supposed to 
                        moneyWon = costOfBets[i] * 2
                        # You get back the money you bet
                        playerInfo.money += costOfBets[i]
                        # loses are subtracted from balance 
                        playerInfo.money -= moneyWon 
                        # Printing amount won + money total
                        print(bcolours.RED + "Money lost: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)  
                
                # If the number is odd
                elif (rollValue.parity == "odd"):
                    # if player correctly guesses odd
                    if (playerBet.parityBet == "odd"):
                        # They lose half of their bet 
                        moneyWon = costOfBets[i] / 2
                        # You get back the money you bet
                        playerInfo.money += costOfBets[i]
                        # loses are subtracted from balance  
                        playerInfo.money -= moneyWon 
                        # Printing amount won + money total
                        print(bcolours.RED + "Money lost: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)  

                    # if player incorrectly guessed even 
                    else:
                        # They lose double of what they were supposed to 
                        # The money was already deducted therefore cost of the bet just has to be subtracted again
                        moneyWon = costOfBets[i]
                        # loses are subtracted from balance 
                        playerInfo.money -= moneyWon
                        # Printing amount won + money total
                        print(bcolours.RED + "Money lost: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC) 

            # If player also chose to bet on red and black 
            elif (playerBet.typeOfBet == 3):

                # if the number is red 
                if (rollValue.colour == "red"):
                    # if player correctly guesses red
                    if (playerBet.colourBet == "red"):

                        # The money they bet is added back
                        playerInfo.money += costOfBets[i] 

                        # They lose half of their bet 
                        moneyWon = costOfBets[i] / 2

                        # loses are subtracted from balance 
                        playerInfo.money -= moneyWon 
                        # Printing amount won + money total
                        print(bcolours.RED + "Money lost: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)  

                    # if player incorrectly guessed black 
                    else:
                        # They lose double of what they were supposed to 
                        moneyWon = costOfBets[i] * 2
                        # You get back the money you bet
                        playerInfo.money += costOfBets[i]
                        # loses are subtracted from balance 
                        playerInfo.money -= moneyWon 
                        # Printing amount won + money total
                        print(bcolours.RED + "Money lost: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)  
                
                # If the number is black
                elif (rollValue.colour == "black"):
                    # if player correctly guesses odd
                    if (playerBet.colourBet == "black"):
                        # They lose half of their bet 
                        moneyWon = costOfBets[i] / 2
                        # You get back the money you bet
                        playerInfo.money += costOfBets[i]
                        # loses are subtracted from balance  
                        playerInfo.money -= moneyWon 
                        # Printing amount won + money total
                        print(bcolours.RED + "Money lost: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)  

                    # if player incorrectly guessed red 
                    else:
                        # They lose double of what they were supposed to 
                        # The money was already deducted therefore cost of the bet just has to be subtracted again
                        moneyWon = costOfBets[i]
                        # loses are subtracted from balance 
                        playerInfo.money -= moneyWon
                        # Printing amount won + money total
                        print(bcolours.RED + "Money lost: " + str(moneyWon)+ " New money total: " + str(playerInfo.money) + bcolours.ENDC)     

def goodbye():
    print("Thank you for playing! You are leaving the casino with $" + str(playerInfo.money))
    exit()

def playMore():
    if (playerInfo.money <= 0):
            print("Sorry, you've run out of money.")
            playAgain = False
            goodbye()
    answer = get_valid_two_option_string("Would you like to play again: (yes/no) ", "yes", "no", "Please enter \"yes\" or \"no\"")
    if (answer == "yes"):
        playAgain = True
    else: 
        playAgain = False
        goodbye()

# Main function
def main():
    introduction()
    while (playAgain == True):
        betTypespecification()
        ballRoll()
        playerWinningsCheck()
        playMore()

main()












