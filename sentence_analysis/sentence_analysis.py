# Sentence Analysis Tool

#import punctuation module from library 'string'
from string import punctuation
print('Hello and welcome to sentence analysis tool! Please enter a sentence below for me to look at!')

#take input from user and make it into an iterable list
sentence = input('Please input your sentence here: ')
list(sentence)

#Store the count in a dictionary
count_dict = { 'total':0 ,'lower': 0, 'upper': 0, 'punct':0,}

# iterate through the list and each time search for a different target character
# increment the count each time you find a target character
for s in sentence:
    count_dict['total'] += 1

for s in sentence:
    if s.islower():
        count_dict['lower'] += 1

for s in sentence:
    if s.isupper():
        count_dict['upper'] += 1

for s in sentence:
    if s in punctuation:
        count_dict['punct'] += 1

# Tell the user the tally for their query
print('\n')
print('------Thank you for your input!------\n')
print('The total number of characters entered is: ' + str(count_dict['total']))
print('The number of lowercase characters is: ' + str(count_dict['lower']))
print('The number of uppercase characters is: ' + str(count_dict['upper']))
print('The number of punctuation marks is: ' + str(count_dict['punct']) + '\n')
print('Thank you for using the sentence anaylsis tool! See you next time!')








