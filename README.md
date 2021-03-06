# LING550
LING550 Final Project

Saul Backer and Daniel Arthur

# Description
This program aims to predict the regional dialect of a given speaker from a given test set of data by using a KNN classifier which has been trained to the average F1 and F2 values for each vowel for each speaker in a given training set.  

# Installation
To run these programs effectively, you will need to have **[FAVE Align](https://github.com/JoFrhwld/FAVE/tree/master/FAVE-align)** and **[FAVE Extract](https://github.com/JoFrhwld/FAVE/tree/master/FAVE-extract)** successfully installed. 

# Usage
## TextEdit

takes a directory containing TIMIT speaker text files at (AddTextDirectory(inputdirectory)), and formats them so that they are able to be processed by FAVE align and FAVE extract.  At line 52, the function addTxt is called, which asks for two strings and a text file.  The two strings will be two tab delimited labels at the begininning of the text file.   

## FAVEAlignLoop

In FAVEAlignLoop, the function FAVEALIGNLOOP takes a directory containing (correctly formatted) speaker text files and their corresponding WAV files (inputdirectory) and the working directory of FAVE Alin (workingdirectory) and loops the files through FAVEAlign, creating an output TextGrid for each .TXT, .WAV file pair. 


## FAVEExtractLoop 
Takes a directory containing speaker WAV files and their corresponding aligned TextGrid files (inputdirectory).  This program must then be run on the command line with the directory for FAVE extract set as the working directory.

In the directory 'FAVE-Extract', type:

    python FAVEExtractloop.py

This program outputs a text file containing information detailing the formant values for each vowel uttered by the speaker. 

## ConcatenateText
Takes a directory containing multiple output text files corresponding to one speaker from FAVE extract (Basedirectory) and concatenates them so that each speaker has one text file detailing formant information.  The program also saves these fiiles to a given output directory (outputdirectory).

## vowelaverage

In line 254, VowelAverageKnn takes a train directory containing concatenated text files for each speaker in every region (Directory)  , and a test directory containing the concatenated text file for one speaker from a given region (TestDirectory) and a vowel for the KNN classifier to predict a label for (desiredvowel).  The variable truevowel allows for VowelAverageKnn to test on all vowels.  This program trains a KNN classifier with the data from the train directory and outputs the regional dialect label predicted by the KNN classifier for the given test speaker and also prints the accuracy of the KNN for the given test/train data set.  

## Writeup
Writeup is our final writeup for the project.

## Roles
Discusses our roles for the project.


## TestDirectory.zip and TrainDirectory.zip
These were used in vowelaverage.py to train the KNN classifier and to test the KNN classifier.  

## TIMIT Example Files
These are files that can be used to test TextEdit.py, FAVEAlignLoop.py, FAVEExtractLoop.py, and ConcatenateText.py.
