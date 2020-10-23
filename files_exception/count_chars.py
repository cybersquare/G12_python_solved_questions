
# Read a text file and display the number of vowels/ consonants/uppercase/ lowercase 
# characters in the file. 

file = open('hash.txt', "r")

vowels = set("AEIOUaeiou")
cons = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
upper = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lower = set('abcdefghijklmnopqrstuvwxyz')

text = file.read()
countV = 0
countC = 0
countU = 0
countL = 0

for c in text:
    if c in vowels: # Check vowel
        countV += 1
    elif c in cons: # Check consonant
        countC += 1
    if c in upper: # Check upper case
        countU += 1
    elif c in lower: # Check lower case
        countL += 1
    
print('The number of Vowels is: ',countV)
print('The number of consonants is: ',countC)
print('The number of uppercase letters is: ',countU)
print('The number of lowercase letters is: ',countL)