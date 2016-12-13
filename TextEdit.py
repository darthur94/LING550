import os 
import mimetypes
import glob
import itertools
v = (glob.glob('/Users/danielarthur/Desktop/textD1/*.TXT'))

for i in v:
	print(i)


for dirpath, dirnames, filenames in os.walk('/Users/danielarthur/Desktop/textD1'):
	#print(filenames)
	for filename in filenames:
		if mimetypes.guess_type(filename)[0] == 'text/plain':
			q = (os.path.join(dirpath, filename))
			with open(q) as f:
				r = f.read()
				#print(r)
			


def addTxt(speaker, region, textFile): #this function takes two strings and a text file as inputs
	import re 						# the string correspond to the speaker and region, and the text file
	dimple = open(textFile)			#is the file that we wish to change
	frumple = (dimple.read())

	wantTime =r'[0-9]{3,}'
	gettingTime = re.search(wantTime, frumple).group(0) #targets the regexp we want saves it to group 0
	gotTime = str((float(gettingTime))/16000) #casts to float, divides number, casts back to string

	wantNom = r'^[0-9]' #finding that first initial digit in the sentence
	gettingNom = str(re.search(wantNom, frumple).group(0))

	wantWords = r'[A-Za-z][\w \W]+[.?!]' #finding all the words in the sentence
	gettingWords = re.search(wantWords, frumple).group(0) 

	file = open(textFile,'w') #opens new file with the same file name
	file.write(speaker+'\t'+region+'\t'+gettingNom+'\t'+gotTime+'\t'+gettingWords) #adds whatever text that you specify
	file.close() #closes the new file, saving it under the same name as the file we originally opened




def AddTextDirectory(inputdirectory:)
	q = glob.glob(inputdirectory +'/*') 
#finds all folders under the subgroup 'Female' with in the TIMIT directory


	for folder in q:
		v = glob.glob(folder+'/*.TXT') #this finds all the files ending in txt in the subfolders within "Female"
		for item in v:
			addTxt('F', 'WesternFemale', item) #calls the addTxt function on the specific file targeted by the for loop



#One can run addTxt() on other files, but because of the regular expressions it will give a 'object NoneType doesn't have attribute group'
#unless the file looks like this:

# "0 57754 She had your dark suit in greasy wash water all year. "

#This is an example of how the TIMIT files looked, and because we needed to divide the second number by 16000, we had to us regexps 





	







