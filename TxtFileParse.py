# Author: Arnav Aggarwal
# Purpose: read text files of several stories and deliver an analysis on them
import re
sampleTxt = ["The", "founders", "of", "a", "new", "colony", "whatever", "Utopia", "of", "human", "virtue","and"]
palindrome = []
fullTxt1 = []

with open("GreatGatsby.txt","r") as f:
	for line in f:
		line = re.sub('[!@#$.,"?]', '', line)
		line = re.sub('[-]', ' ', line)
		for word in line.split():
			fullTxt1.append(word)

#print(fullTxt1)

sortWordsLength = sorted(fullTxt1, key=len)

print ("The number of words in the text is: %s" % (len(fullTxt1),))
print ("The shortest word in the list is: %s" % (sortWordsLength[0],))
print ("The longest word in the text is: %s" % (sortWordsLength[-1],))

for index in fullTxt1:
	if str(index) == str(index)[::-1]:
		if index not in palindrome:
			if len(index) > 1:
				palindrome.append(index)
print("The number of palindromes are: %s" % len(palindrome))
print("The palindromes are: %s" % palindrome)






