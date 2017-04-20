from textblob import TextBlob
import os
'''
#This is just a simple test :)
text =
    @ninjen I'm sure you're right...    I need to start working out with you and the Nikster... Or Jared at least!


blob = TextBlob(text)
print blob.tags
print '+++++++'
print text.split()
'''
#textblob eliminates emoticons when tagging.
#must get emoticon counts manually
sigma = 0
#11466 emoticons using this list. add regex?
emoticons_list = [';D', ':D', ';)', ':)', ';]' ':]', ':|', ':/', ':(', ':[', ':p', ':P', ':o', ':O', '=)', '=]', '=(', '=[' ]

pos_files = os.listdir('Data/train/pos')
neg_files = os.listdir('Data/train/neg')

pos_bof, neg_bof = {}, {}

for f in pos_files:
    fo = open('Data/train/pos/%s' % f, 'r')
    #handle emoticons first
    text = fo.read().split(' ')
    for token in text:
        if token in emoticons_list:
            if token not in pos_bof:
                pos_bof[token] = 1
            else:
                pos_bof[token] += 1
            sigma +=1

print "pos_files scanned"

for f in neg_files:
    fo = open('Data/train/neg/%s' % f, 'r')
    #handle emoticons first
    text = fo.read().split(' ')
    for token in text:
        if token in emoticons_list:
            if token not in neg_bof:
                neg_bof[token] = 1
            else:
                neg_bof[token] += 1
            sigma +=1

print sigma
print "+++++++++++++"
print pos_bof
print "+++++++++++++"
print neg_bof
