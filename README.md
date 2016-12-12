# LING550
LING550 Final Project

# Description
This program aims to predict the regional dialect of a given speaker from a given test set of data by using a KNN classifier which has been trained to the average F1 and F2 values for each vowel for each speaker in a given training set.  

# Installation
To run these programs effectively, you will need to have **[FAVE Align](https://github.com/JoFrhwld/FAVE/tree/master/FAVE-align)** and **[FAVE Extract](https://github.com/JoFrhwld/FAVE/tree/master/FAVE-extract)** successfully installed. 

# Usage
TextEdit takes a directory containing TIMIT speaker text files, and formats them so that they are able to be processed by FAVE align and FAVE extract.

FAVEAlignLoop takes a directory containing (correctly formatted) speaker text files and their corresponding WAV files and loops them through FAVEAlign, creating an output TextGrid for each .TXT, .WAV file pair. 

FAVEExtractLoop takes a directory containing speaker WAV files and their corresponding aligned TextGrid files and outputs a text file containing information detailing the formant values for each vowel uttered by the speaker. 

ConcatenateText takes a directory containing multiple output text files corresponding to one speaker from FAVE extract and concatenates them so that each speaker has one text file detailing formant information.

VowelAverage takes a train directory containing concatenated text files for each speaker in every region  , and a test directory containing the concatenated text file for one speaker from a given region and trains a KNN classifier with the data from the train directory and outputs the regional dialect label predicted by the KNN classifier for the given test speaker and also prints the accuracy of the KNN for the given test/train data set.  