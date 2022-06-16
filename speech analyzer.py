# Andrew Yeh
# Speech Analyzer
# CompSci 30
# Sept 17th
# This program is my own work - A.Y.

import string

text = """Tomorrow, and tomorrow, and tomorrow,\nCreeps in this petty pace from day to day,
To the last syllable of recorded time;\nAnd all our yesterdays have lighted fools
The way to dusty death. Out, out, brief candle!\nLife's but a walking shadow, a poor player,
That struts and frets his hour upon the stage,\nAnd then is heard no more. It is a tale
Told by an idiot, full of sound and fury,\nSignifying nothing."""

text = text.translate(str.maketrans("", "", string.punctuation))
wordList = text.split()
eCount = 0
for word in wordList:
    if "e" in word:
        eCount += 1
print(text)
print(f'Your text contains {len(wordList)} words, of which {eCount} '
      f'({round(eCount/len(wordList) * 100, 2)}%) contains an "e".')
