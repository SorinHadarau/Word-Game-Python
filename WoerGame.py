## This is just a tentative a a game that I still have to perfect, test and modify to meet fully the envisioned requirements
import collections
from PyDictionary import PyDictionary

sourceword = "exampleword"
sourceword = sourceword.lower() # convert sourceword to lowercase

# Create a frequency dictionary for the sourceword
freq_dict = collections.Counter(sourceword)

# Create an empty list to store the words
seven_words = []
dictionary=PyDictionary()

# Iterate through a dictionary of words
with open("words_dictionary.txt") as f:
    for word in f:
        word = word.strip()
        word = word.lower() # make word case-insensitive
        if (len(word) >= 4) and (word != sourceword) and (collections.Counter(word) <= freq_dict):
            if dictionary.meaning(word):
                seven_words.append(word)

# Remove duplicate words from the list
seven_words = list(set(seven_words))

print(seven_words)


