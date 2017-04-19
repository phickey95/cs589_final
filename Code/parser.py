#data from http://help.sentiment140.com/for-students

#parse csv file for tweets
    #split training file 70/30 train/test
    #put into pos/neg directories based on polarity value in .csv

import csv
with open('../Data/training.1600000.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #first 800000 are positive, last 800000 are negative tweets
    for j, row in enumerate(reader):
        #print "row[0] is polarity"
        #print "row[5] is tweet~text"
        if (int(row[0]) == 0 and j< 560000):
            #add tweet files to neg. training directory
            file_name = "../Data/train/neg/tr" + str(j) + ".txt"
        elif (int(row[0]) == 0 and j>= 560000):
            #add tweet files to neg. test directory
            file_name = "../Data/test/neg/te" + str(j) + ".txt"
        elif (int(row[0]) == 4 and j< 1360000):
            #add tweet files to pos. training directory
            file_name = "../Data/train/pos/tr" + str(j) + ".txt"
        else:
            #add tweet files to pos. test directory
            file_name = "../Data/test/pos/te" + str(j) + ".txt"
        text_file = open(file_name, "w")
        text_file.write(row[5])
        text_file.close()
