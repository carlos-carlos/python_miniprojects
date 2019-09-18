import random

#take in a number 0-2 from the user that represents their hand
player_input = int(input('Please enter a number between 0 - 2: '))

#Generate a random number 0-2 to use for the computer's hand

computer = random.randint(0,2)

#make string representaitons of the hands
def makeHand(hand):
    if hand == 0:
        return 'scissor'

    elif hand == 1:
        return 'rock'

    elif hand == 2:
        return 'paper'

    else:
        pass
#print(makeHand(player_input))
#print(makeHand(computer))

def winning(player, comp):
	'''Checks to see who won'''
	if player == 'scissor' and comp == 'paper' or player == 'rock' and comp == 'scissor' or player == 'paper' and comp == 'rock':
		return 'Glory to the Humans! Player Wins!'

	elif comp == 'scissor' and player == 'paper' or comp == 'rock' and player == 'scissor' or comp == 'paper' and player == 'rock':
		return 'Glory to the Machines! Computer Wins!'

	else:
		return 'Hmmm, it appears we have  tie!'

if player_input not in range(0, 3):
    print('Thats not a number between 0 and 2')

else:

    # call the function `get_hand` to get the string representation of the user's hand
    a = makeHand(player_input)

    # call the function `get_hand` to get the string representation of the computer's hand
    b = makeHand(computer)

    # call the function `determine_winner` to figure out who won
    c = winning(makeHand(player_input),makeHand(computer))

    # print out the player hand and computer hand
    print('Player threw ' + makeHand(player_input) + ' and Computer threw ' + makeHand(computer) + '\n')

    # print out the winner
    print(winning(makeHand(player_input), makeHand(computer)))