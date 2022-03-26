import wordList
import sys
from operator import itemgetter

# Create a list to store the frequency of the letters
letterFreq = [0] * 26

# Figure out the frequency of each letter
for word in wordList.words:
	for letter in word:
		# Convert to ascii, reset index
		letterIndex=ord(letter) - 97
		letterFreq[letterIndex] = letterFreq[letterIndex] + 1

# Assign the letter to the letter frequency
i = 0
letterList = []
for letter in letterFreq:
	# print(chr(i+97)+": "+str(letter))
	letterTemp=[chr(i+97),letter]
	letterList.append(letterTemp)
	i = i+1

# Stort the list by frequency
letterList = sorted(letterList, key=itemgetter(1), reverse=False)
print("Letter Frequency: ")
print(*letterList, sep="\n")
print()

# Remove the frequency
letterList = [row[0] for row in letterList]

# Create list of words and their score
wordScore = [0] * len(wordList.words)
wordScoreList = []

# Calculate the word score
i = 0
for word in wordList.words:

	# Filter letters with duplicates
	duplicateLetter=False
	for letter in word:
		if(word.count(letter) > 1):
			duplicateLetter=True

	# Calculate the score
	if(not duplicateLetter):
		for letter in word:
			wordScore[i] = wordScore[i] + letterList.index(letter)

		# Add list of words and score
		wordScoreList.append([word,wordScore[i]])

	i = i + 1

# Sort the list of scores
wordScoreList = sorted(wordScoreList, key=itemgetter(1), reverse=True)

wordScoreList = wordScoreList[:1500]

print("Best guesses: ")
print(*wordScoreList[:10], sep="\n")
print()

wordScoreList = [row[0] for row in wordScoreList]

# Figure out the best first 2 guesses
bestGuesses = ""
lowestScore = 2*len(wordScoreList)
for word0 in wordScoreList:
	for word1 in wordScoreList:

		duplicate = False
		combinedWord = word0 + word1
		for letter in combinedWord:
			if(combinedWord.count(letter) > 1):
				duplicate = True

		if(duplicate):
			continue

		score = wordScoreList.index(word0) + wordScoreList.index(word1)

		if(score < lowestScore):
			lowestScore = score
			bestGuesses = word0+ " " + word1

print("Best first 2 guesses: ")
print(bestGuesses)
