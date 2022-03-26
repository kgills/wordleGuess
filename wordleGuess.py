import wordList
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
	letterTemp=[chr(i+97),letter]
	letterList.append(letterTemp)
	i = i+1

# Stort the list by frequency
letterList = sorted(letterList, key=itemgetter(1), reverse=True)
print("Letter Frequency: ")
print(*letterList, sep="\n")
print()

# Remove the frequency
letterList = [row[0] for row in letterList]

# Select only the first 15 letters
letterList = letterList[:15]

# Create list of words with the top letters
topWordList = []
for word in wordList.words:
	filterWord=False
	for letter in word:
		# Filter words with duplicates
		if(word.count(letter) > 1):
			filterWord=True

		# Filter words with letters not in the most frequent
		if(not letter in letterList):
			filterWord=True

	# Add the word to the list
	if(not filterWord):
		topWordList.append(word)

# Figure out the best first 3 guesses
found = False
combinedWord = ""
for word0 in topWordList:
	if found:
		break
	for word1 in topWordList:
		if found:
			break

		# Filter if the words have common letters
		duplicate = False
		combinedWord = word0 + word1
		for letter in combinedWord:
			if(combinedWord.count(letter) > 1):
				duplicate = True

		if(duplicate):
			continue

		for word2 in topWordList:
			if found:
				break

			# Filter if the words have common letters
			duplicate = False
			combinedWord = word0 + word1 + word2
			for letter in combinedWord:
				if(combinedWord.count(letter) > 1):
					duplicate = True

			if(not duplicate):
				combinedWord = word0+" "+word1+" "+word2
				found = True

print("Best first 3 guesses: ")
print(combinedWord)
