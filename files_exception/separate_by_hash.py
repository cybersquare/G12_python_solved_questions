# Read a text file line by line and display each word separated by a #.

file = open("hash.txt","r")
doc = file.readlines()
for line in doc:
   words = line.split()
   for word in words:
       print(word + "#", end='')
   print('')
   
file.close()