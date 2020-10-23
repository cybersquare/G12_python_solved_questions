# Take a sample of ten phishing e-mails (or any text file) and find most
# commonly occurring word(s)

import re

file = open("hash.txt","r")
text = file.read()

# Split words into a list
words = re.findall(r'\w+', text) 

# wordDict stores word as key and count as value
wordDict = dict() 
mostWord = ''
mostCount = 1

# Add words and update count to wordDict
for word in words:
    if word in wordDict.keys():
        wordDict[word] += 1
    else:
        wordDict[word] = 1

# Check the count in wordDict to find most occuring word
for word, count in wordDict.items():
    if count > mostCount:
        mostCount = count
        mostWord = word

# Print most occuring word
if mostCount > 1:
    print('Most occured word is %s, occurs %d time'%(mostWord, mostCount))
else:
    print('All the words occurs single time only')
