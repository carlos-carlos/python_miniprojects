#Put the secret into a list
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
upSec = list(secret.upper())

#Ceasar Cipher of 7 == TUVWXYZABCDEFGHIJKLMNOPQRS
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cipher = alphabet[19:32] + alphabet[0:19]

result = []
for l in secret:
    result.append(str.find(cipher))

print(result)