#Python program that matches a word containing 'z or Z', not at start or end of the word. (Example : Aaazwwwiiii is valid and zAswiz is invalid)

import re

pat = '\Bz|Z\B'
word=raw_input("Enter a string :")

def text_match(text):
		if re.search(pat, text):
			return "Found a match!"
		else:
			return "Not matched!"
print text_match(word)
