from textblob import TextBlob
import pickle
import numpy as np

text = '''
    thats a dog
'''

#i could combine n-grams into one string, feed into TextBlob()
print TextBlob(text).sentiment
print TextBlob(text).tags
print TextBlob(text).noun_phrases
print "==========="
for text in TextBlob(text).tags:
    print text[1]

dictionary = {'hello': 100}
with open('Data/test.pkl', 'wb') as f:
    pickle.dump(dictionary, f, pickle.HIGHEST_PROTOCOL)

with open('Data/test.pkl', 'rb') as f:
    print pickle.load(f)
