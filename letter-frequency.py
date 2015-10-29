#!/usr/bin/python

import string
import matplotlib.pyplot as plt

# String charaters to be eliminated from text
pd = string.punctuation + string.digits

# Empty dictionary to store
lettersDict = {}
  
# User input text file
text = raw_input("Enter the file name: ")

with open(text, 'r') as textfile:
	for line in textfile:
		line = line.strip()
		line = line.translate(None, pd)
		line = line.lower()
		letters = list(line)
		for letter in letters:
			if not " " in letter and not "\t" in letter:
				lettersDict[letter] = lettersDict.get(letter, 0) + 1

# Some empty lists for storing tuples
lettersCount = []
countLetters = []
totalCount = 0

# Appending to list for sorting
for l, c in lettersDict.items():
	lettersCount.append((l, float(c)))
	countLetters.append((float(c), l))
	totalCount = totalCount + c

# Sorting lists	
lettersCount.sort()
countLetters.sort(reverse=True)

# Some more empty lists
relCount = []
relCountReverse = []
labels = []
labelsReverse = []
values = []

# Sorted list for plotting labels
# alphabetical order
for L, C in lettersCount:
	relCount.append((float(C) / totalCount) * 100)
	labels.append(L)

# decending order of percentage
for Cr, Lr in countLetters:
	relCountReverse.append((float(Cr) / totalCount) * 100)
	labelsReverse.append(Lr)

# Plots
# alphabetical order
figure1 = plt.figure(1)
width = 1/1.25
plt.title("Text frequency in percentage")
plt.bar(range(len(lettersCount)), relCount, width, color="blue", align="center")
plt.xticks(range(len(lettersCount)), labels)
plt.xlim(-1, 26)
plt.xlabel("Alphabets")
plt.ylabel("Percentage")

# decending order of percentage
figure2 = plt.figure(2)
plt.title("Text frequency in percentage")
plt.bar(range(len(countLetters)), relCountReverse, width, color="green", align="center")
plt.xticks(range(len(countLetters)), labelsReverse)
plt.xlim(-1, 26)
plt.xlabel("Alphabets")
plt.ylabel("Percentage")


plt.show()
