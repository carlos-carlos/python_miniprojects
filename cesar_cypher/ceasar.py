'''
Replicate one of the oldest known encryption in code.

Apply a [Cesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) of 7 to the 'secret' variable.

P.S.: <http://www.montypython.net/scripts/dentist.php> ;)

You can start with the following code:
'''

#Put the secret into a list
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
upSec = list(secret.upper())

#Ceasar Cipher of 7 == TUVWXYZABCDEFGHIJKLMNOPQRS
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
cipher = list(alphabet[19:32] + alphabet[0:19])


#print(cipher) #To see if it works so far

#compare the item in the secret list to the item in the cipher list and get the index of the item in the cipher list
result = []
for x in upSec:
    if x in upSec and x in cipher:
        upSec.index(x) == cipher.index(x)
        result.append(cipher.index(x))

#print(type(result[1]))
#This should be the index of each letter in cipher ordered as it is in secret
#print(result) #Test to see if it works so far

# Now compare the value in result to the corresponding index in cipher and print that item
crypt = []
for x in result:
    if x == cipher.index(x):
        crypt.append(cipher.item())

print(str(crypt))










