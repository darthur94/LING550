import os 
import mimetypes
import glob
import itertools
import subprocess
import re

fileRegexp = r'[F|M][A-Z0-9]+[\/][A-Z0-9]+[.][\w\W]+'
 
soundName = ''
textName = ''
space = ' '
para1 = 'python'
para2 = 'bin/extractFormants.py'
para3 = '-v'
para4 = '-i'

para6 = 'output.TextGrid'

q = glob.glob('/Users/danielarthur/Downloads/FAVE-1.2.2/FAVE-extract/TRAINEXTRACT/DR1//*')

qqq = list()


regexfilename = r'[/][S][A-Z0-9]+'

textfiles = list()
wavfiles = list()
names = list()

d = 'cd'
e = '/Users/danielarthur/Downloads/FAVE-1.2.2/FAVE-extract'



def FAVEEXTRACTLOOP(inputdirectory):


base_dir = inputdirectory


q = zip(range(9000), wavfiles, textfiles)






for root, dirs, files in os.walk(base_dir):
	print(root)
	for f in files:
		if not f.endswith('.WAV'):
			continue
		#print(f)
		wav_file = os.path.join(root, f)
		txtgrid_file = os.path.join(root, f.replace('.WAV','.TextGrid'))
		if not os.path.exists(txtgrid_file):
			continue
		outputname, _ = os.path.splitext(f)
		outputname = os.path.join(root, outputname+'.txt')

		subprocess.call([str(para1), str(para2), wav_file, txtgrid_file, outputname])
		#proc.communicate()

print('all done!')