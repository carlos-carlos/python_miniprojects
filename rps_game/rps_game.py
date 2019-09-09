import random

#take in a number 0-2 from the user that represents their hand
player_input = int(input('Please enter a number between 0 - 2: '))

#Generate a random number 0-2 to use for the computer's hand

computer = random.randint(0,3)

# Make string representation of the player's hand
def getPlayerHand(hand):
	'''generates a string of the player's hand'''
	strung = str(hand)
	return strung

# Make string representation of the computer's hand
def getCompHand(hand):
	'''generates a string of the computer's hand'''
	strung = str(hand)
	return strung

def winning(player, comp):
	'''Checks to see who won'''
	if player > comp:
		return 'Congratulations Player! You won!'

	elif comp > player:
		return 'Congratulations Computer! You won!'

	else:
		return 'Hmmm, it appears we have  tie!'

#check if the input is with the specified range
if player_input not in range(0, 3):
    print('Thats not a number between 0 and 2')
else:
    #Continue if its good
	#Call the function get_hand to get the string representation of the user's hand
	a = getPlayerHand(player_input)

	#Call the function get_hand to get the string representation of the computer's hand
	b = getCompHand(computer)

	#call the function determine_winner to figure out who won then print out the winner
	print(winning(player_input,computer))

	#Print out the player hand and computer hand
	print('\nPlayer threw a ' + a + ' while Computer threw a ' + b + '.')



