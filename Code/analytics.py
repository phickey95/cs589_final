import pickle
import numpy as np
import pandas as pd
import ast

#s = pd.Series({'a':1, 'b':2, 'c':3})
#print s.values # a numpy array

emoticons_list = [';D', ':D', ';)', ':)', ';]' ':]', ':|', ':/', ':(', ':[', ':p', ':P', ':o', ':O', '=)', '=]', '=(', '=[',
                    ':-]', ':-[',':-D',':-0', ':-o', ':-O', ':-P', ':-p', ':-|', ':-/', ';-]', ';-P', ';-p', ":'(", ":'[", "='(", "='[" ]

pos_emot = {}
pos_filtered_features = {}
pos_above_one_ct = 0

print "The following data is about the positive class: "
#load pos_bof pickle file
with open('Data/pickles/pos_bof.pkl', 'rb') as f:
    #dictionary = ast.literal_eval(pickle.load(f))
    for key,val in pickle.load(f).iteritems():
        if key in emoticons_list:
            pos_emot[key] = val
        if val > 1 and key not in emoticons_list:
            pos_filtered_features[key] = val
            pos_above_one_ct += 1
        if key in emoticons_list:
            #always add emoticon counts, even if zero
            pos_filtered_features[key] = val
            if val > 1:
                pos_above_one_ct += 1
    print '   above_one_ct: ' + str(pos_above_one_ct)
    print pos_emot

with open('Data/pickles/pos_bof.pkl', 'rb') as f:
    print '   unfiltered #features: ' + str(len(pickle.load(f)) )
    print '   filtered #features: ' + str(len(pos_filtered_features) )

print "+=+=+=+=+=+=+=+=+="

neg_emot = {}
neg_filtered_features = {}
neg_above_one_ct = 0

print "The following data is about the negative class: "
#load neg_bof pickle file
with open('Data/pickles/neg_bof.pkl', 'rb') as f:
    #dictionary = ast.literal_eval(pickle.load(f))
    for key,val in pickle.load(f).iteritems():
        if key in emoticons_list:
            neg_emot[key] = val
        if val > 1 and key not in emoticons_list:
            neg_filtered_features[key] = val
            neg_above_one_ct += 1
        if key in emoticons_list:
            #always add emoticon counts, even if zero
            neg_filtered_features[key] = val
            if val > 1:
                neg_above_one_ct += 1
    print '   above_one_ct: ' + str(neg_above_one_ct)
    print neg_emot

with open('Data/pickles/neg_bof.pkl', 'rb') as f:
    print '   unfiltered #features: ' + str(len(pickle.load(f)) )
    print '   filtered #features: ' + str(len(neg_filtered_features) )

#GET OVERLAPPING FEATURE INFO.
print "+=+=+=+=+=+=+=+=+="
print "The following data is about thier overlap: "
intersection = {}
for n_key, n_val in neg_filtered_features.iteritems():
    for p_key, p_val in pos_filtered_features.iteritems():
        if p_key == n_key:
            intersection[n_key] = (n_val, p_val)
print "   intersection length: " + str(len(intersection))
#following comes from printed output & is hardcoded since im lazy
print "   unique #pos. filtered~features: " + str(30132-17027)
print "   unique #neg. filtered~features: " + str(27601-17027)
print "+=+=+=+=+=+=+=+=+="
print "   writing filtered data to pickle files..."
#write BOFs to files
with open('Data/pickles/pos_filtered_features.pkl', 'wb') as f:
    pickle.dump(pos_filtered_features, f, pickle.HIGHEST_PROTOCOL)

with open('Data/pickles/neg_filtered_features.pkl', 'wb') as f:
    pickle.dump(neg_filtered_features, f, pickle.HIGHEST_PROTOCOL)

with open('Data/pickles/intersection_filtered_features.pkl', 'wb') as f:
    pickle.dump(intersection, f, pickle.HIGHEST_PROTOCOL)
print "done."
