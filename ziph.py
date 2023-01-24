# imports regular expressions
import re

# opens textfile to examine
alice_txt = open("alice_in_wonderland.txt")

# this block of code creates a list of unique words in the text file and counts how many times each word occurs
listofwords = {}
# splits document into lines
for line in alice_txt:
    line = line.split()
    # splits lines into individual words
    for word in line:
        # changes all charcters to lowercase
        word = word.lower()
        # substituting every nonalphanumeric character into an empty string
        word = re.sub('\W', '', word)
        # adding word to list if it has not been seem before and mark as seen once
        if word not in listofwords:
            listofwords[word] = 1
        # if word is recognised update the count of times observed
        else:
            listofwords[word] += 1

# lambda function which sorts out word list by key in reverse order
res = {key: val for key, val in sorted(listofwords.items(), key = lambda ele: ele[1], reverse = True)}

# creates a list of of powers of 10 for verifying Ziph's law'
powers_of_10 = []
for i in range(6):
    powers_of_10.append(10**i)

# this block of code prints out a word and it's key if it happens to be the 1st, 10th, 100th, 1000th ,etc word
count = 0
for i in res:
    count +=1
    if count in powers_of_10:
        print(i, res[i])
