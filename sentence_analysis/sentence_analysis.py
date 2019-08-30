# Sentence Analysis Tool

#import punctuation module from library 'string'
from string import punctuation
print('Hello and welcome to sentence analysis tool! Please enter a sentence below for me to look at!')

#take input from user and make it into an iterable list
sentence = input('Please input your sentence here: ')
list(sentence)

#store totals in a variable for testing
count_total = 0
count_u = 0
count_l = 0
punc_count = 0

count_totals = {'total': , 'upper': ,'lower': ,'punct': , }

# iterate through the list and each time search for a different target character
# increment the count each time you find a target character
for s in sentence:
    count_total += 1

for s in sentence:
    if s.islower():
        count_l += 1

for s in sentence:
    if s.isupper():
        count_u += 1

for s in sentence:
    if s in punctuation:
        punc_count += 1

# Tell the user the tally for their query
print('\n')
print('Thank you for your input!\n')
print('The total number of characters entered is: ' + str(count_total))
print('The number of lowercase character is: ' + str(count_l))
print('The number of uppercase characters is: ' + str(count_u))
print('The number of punctuation character is: ' + str(punc_count))

#TODO: Add the part that puts it in a dictionary






