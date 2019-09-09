import random

#take in a number 0-2 from the user that represents their hand
player_input = int(input('Please enter a number between 0 - 2: '))

#Generate a random number 0-2 to use for the computer's hand

computer = random.randint(0,3)

# Make string representation of the player's hand
def getPlayerHand(hand):
    if hand == 0:
        return 'scissor'

    elif hand == 1:
        return 'rock'

    elif hand == 2:
        return 'paper'

    else:
        pass

# Make string representation of the computer's hand
def getCompHand(hand):
    if hand == 0:
        return 'scissor'
    elif hand == 1:
        return 'rock'
    elif hand == 2:
        return 'paper'
    else:
        pass

def winning(player, comp):
	'''Checks to see who won'''
	if player > comp:
		return 'Congratulations Computer! You won!'

	elif comp > player:
		return 'Congratulations Player! You won!'

	else:
		return 'Hmmm, it appears we have  tie!'

#check if the input is with the specified range
if player_input not in range(0, 3):
    print('Thats not a number between 0 and 2')

else:

    # call the function `get_hand` to get the string representation of the user's hand
    a = getPlayerHand(player_input)

    # call the function `get_hand` to get the string representation of the computer's hand
    b = getCompHand(computer)

    # call the function `determine_winner` to figure out who won
    winning(player_input,computer)

    # print out the player hand and computer hand
    print('Player threw ' + getPlayerHand(player_input) + ' and Computer threw ' + getCompHand(computer) + '\n')

    # print out the winner
    print(winning(getPlayerHand(player_input), getCompHand(computer)))
