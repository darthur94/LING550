import os 
import mimetypes
import glob
import itertools
import subprocess
import re

fileRegexp = r'[F|M][A-Z0-9]+[\/][A-Z0-9]+[\.][A-Z]+' #regexp to isolate the local path name
 
para1 = 'python' #these are the 
para2 = 'FAAValign.py' #necessary parameters to run 
para3 = '-v' #FAAValign through the command line
para4 = '-i'

para6 = 'output.TextGrid'

def FAVEALIGNLOOP(inputdirectory, workingdirectory):

	r = glob.glob(inputdirectory +'/*')



	textfiles = list()
	wavfiles = list()

	d = 'cd'
	e = '/Users/danielarthur/Downloads/FAVE-1.2.2/FAVE-align'

	for folder in r: #Outer List
		v = glob.glob(folder+'/*.TXT')
		for w in v:
			regExp = re.search(fileRegexp, w).group(0) #isolates the local file path name, adds it to a list
			textfiles.append(regExp) #appends it to a list of txt files
		p = glob.glob(folder+'/*.WAV')
		for w in p:
			regExp2 = re.search(fileRegexp, w).group(0) #isolates the local file path name, adds it to a list
			wavfiles.append(regExp2) #appends it to a list of .wav files

	###the wav and txt file must have the same names, and this way assures that while the file names
	###may be in different lists, when we iterate over those lists, the file names will match


	textfilesdoubled = [x for pair in zip(textfiles,textfiles) for x in pair]

	q = zip(range(9000), wavfiles, textfiles) # makes a tuple of a nubmer, a wave file, and a text file, this was done becuase the process was stopping at arbitrary points and it was necessary to reset the index from the place at which the process stopped. 




	base_dir = inputdirectory #base directory 


	for i,w, v in q: # i is a list of numbers, w is the list of wavfiles, and v is the list of text files in this zip (q)
		wav_file = os.path.join(base_dir, w) # finds the full path file for the wavfile, w
		txt_file = os.path.join(base_dir, v)# finds the full path file for the textfile, v
		
		proc = subprocess.Popen([str(para1), str(para2), wav_file, txt_file], cwd= workingdirectory, stdin=None, stdout=None, stderr=None, shell=False) #this executes FAAV align on a given Wav and Text file pair
		proc.communicate() # this forces the program to let subprocess.Popen finish one occurence before running it again. 


	d = 'cd'
	e = '/Users/danielarthur/Downloads/FAVE-1.2.2/FAVE-align/'







	







