from textblob import TextBlob
import unicodedata
import pickle
import os
#textblob eliminates emoticons when tagging.
#textblob stuff: https://textblob.readthedocs.io/en/dev/quickstart.html#part-of-speech-tagging

#must get emoticon counts manually
#11466 emoticons using this list. add regex?
emoticons_list = [';D', ':D', ';)', ':)', ';]' ':]', ':|', ':/', ':(', ':[', ':p', ':P', ':o', ':O', '=)', '=]', '=(', '=[',
                    ':-]', ':-[',':-D',':-0', ':-o', ':-O', ':-P', ':-p', ':-|', ':-/', ';-]', ';-P', ';-p', ":'(", ":'[", "='(", "='[" ]

#different verb forms & adjective
important_pos = ['VB', 'VBP', 'VBD', 'VBG', 'JJ']

pos_files = os.listdir('Data/train/pos')
neg_files = os.listdir('Data/train/neg')

pos_bof, neg_bof = {}, {}
ct = 0

#build pos. bof
for f in pos_files:
    fo = open('Data/train/pos/%s' % f, 'r')
    #handle emoticons first
    #normalize text
    text = fo.read().lower()
    for token in text.split(' '):
        if token in emoticons_list:
            if token not in pos_bof:
                pos_bof[token] = 1
            else:
                pos_bof[token] += 1

    #call TextBlob(text) to get POS tags for each tweet
    tagz = TextBlob(text).tags
    for word_tuple in tagz:
        #check if verb or adj
        if word_tuple[1] in important_pos:
            if word_tuple[0] not in pos_bof:
                pos_bof[word_tuple[0]] = 1
            else:
                pos_bof[word_tuple[0]] +=1
    if ct%100000 == 0:
        print ct
    ct+=1

print "pos_files scanned"
#build neg. bof
for f in neg_files:
    fo = open('Data/train/neg/%s' % f, 'r')
    #handle emoticons first
    #normalize text
    text = fo.read().lower()
    for token in text.split(' '):
        if token in emoticons_list:
            if token not in neg_bof:
                neg_bof[token] = 1
            else:
                neg_bof[token] += 1

    #call TextBlob(text) to get POS tags for each tweet
    for word_tuple in TextBlob(text).tags:
        #check if verb or adj
        if word_tuple[1] in important_pos:
            if word_tuple[0] not in neg_bof:
                neg_bof[word_tuple[0]] = 1
            else:
                neg_bof[word_tuple[0]] +=1
    if ct%100000 == 0:
        print ct
    ct +=1

#write BOFs to files
with open('Data/pickles/pos_bof.pkl', 'wb') as f:
    pickle.dump(pos_bof, f, pickle.HIGHEST_PROTOCOL)

with open('Data/pickles/neg_bof.pkl', 'wb') as f:
    pickle.dump(neg_bof, f, pickle.HIGHEST_PROTOCOL)

###

#process test data
#240000 pos/neg files each
# X & Y must have same shape as train data
X, Y = [], []
ct = 0
pos_files = os.listdir('Data/test/pos')
neg_files = os.listdir('Data/test/neg')

for f in pos_files:
    fo = open('Data/test/pos/%s' % f, 'r')
    curr_bof = {}
    text = fo.read().lower()
    #add features to curr_bof

    #first emoticons
    for token in text.split(' '):
        if token in emoticons_list:
            if token not in curr_bof:
                curr_bof[token] = 1
            else:
                curr_bof[token] += 1

    #then verb/adj
    for word_tuple in TextBlob(text).tags:
        #check if verb or adj
        if word_tuple[1] in important_pos:
            if word_tuple[0] not in curr_bof:
                curr_bof[word_tuple[0]] = 1
            else:
                curr_bof[word_tuple[0]] +=1
    if ct%100000 == 0:
        print ct
    ct +=1

    #append cur_bof to X
    X.append(curr_bof)
    #append class label to Y
    Y.append(0)

#same for neg
for f in neg_files:
    fo = open('Data/test/neg/%s' % f, 'r')
    curr_bof = {}
    text = fo.read().lower()
    #add features to curr_bof

    #first emoticons
    for token in text.split(' '):
        if token in emoticons_list:
            if token not in curr_bof:
                curr_bof[token] = 1
            else:
                curr_bof[token] += 1

    #then verb/adj
    for word_tuple in TextBlob(text).tags:
        #check if verb or adj
        if word_tuple[1] in important_pos:
            if word_tuple[0] not in curr_bof:
                curr_bof[word_tuple[0]] = 1
            else:
                curr_bof[word_tuple[0]] +=1
    if ct%100000 == 0:
        print ct
    ct +=1

    #append cur_bof to X
    X.append(curr_bof)
    #append class label to Y
    Y.append(1)

#save relevent data structures
with open('Data/pickles/test_X.pkl', 'wb') as f:
    pickle.dump(X, f, pickle.HIGHEST_PROTOCOL)

with open('Data/pickles/test_Y.pkl', 'wb') as f:
    pickle.dump(Y, f, pickle.HIGHEST_PROTOCOL)
