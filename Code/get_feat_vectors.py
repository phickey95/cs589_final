import pickle
import numpy as np
from sklearn.feature_extraction import DictVectorizer

train_X = []
train_Y = []

pos_bof, neg_bof, intersection = {}, {}, {}

with open('Data/pickles/pos_filtered_features.pkl', 'rb') as f:
    pos_bof = pickle.load(f)

with open('Data/pickles/neg_filtered_features.pkl', 'rb') as f:
    neg_bof = pickle.load(f)

with open('Data/pickles/intersection_filtered_features.pkl', 'rb') as f:
    intersection = pickle.load(f)

#update pos_bof with features not in intersection
pos_final = pos_bof
print len(pos_final)
for n_key, n_val in neg_bof.iteritems():
    if n_key not in intersection.iteritems():
        pos_final[n_key] = 0
print len(pos_final)
#update X
train_X.append(pos_final)
#update Y
train_Y.append(0)

print "+=+=+=+="

#update neg_bof with features not in intersection
neg_final = neg_bof
print len(neg_final)
for p_key, p_val in pos_bof.iteritems():
    if p_key not in intersection.iteritems():
        neg_final[p_key] = 0
print len(neg_final)
#update X
train_X.append(neg_final)
#update Y
train_Y.append(1)

#vectorize -- http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html
v = DictVectorizer(sparse=False)
tr_x = v.fit_transform(train_X)
tr_y = np.asarray(train_Y)

#problem reading in vectors as .pkl files -- EOFError
'''
with open('Data/feature_vectors/tr_x.pkl', 'wb') as f:
    pickle.dump(tr_x, f, pickle.HIGHEST_PROTOCOL)

with open('Data/feature_vectors/tr_y.pkl', 'wb') as f:
    pickle.dump(np.asarray(train_Y), f, pickle.HIGHEST_PROTOCOL)
'''
print "processing training data is done"
