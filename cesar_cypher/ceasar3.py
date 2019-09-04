#Make the secret uppercase to make life easier
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
upSecret = secret.upper()

# the alphabet
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#operate on every letter in the secret and store the result in an empty string
result = ''

#conditional to get rid of spaces and punctuation.
for l in upSecret:
    if l in alphabet:   #if the letter is actually a letter
        l_index = (alphabet.find(l) + 7) % len(alphabet) #find the corresponding ciphe letter in the alphabet
                                                         #Modulo the length of the alphabet to get pass 'looparound'
        result = result + alphabet[l_index] #getting the letter itself from the index and adding it to result

    else:
        result = result + l

print(result)