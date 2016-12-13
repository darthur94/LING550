

from __future__ import division
import os 






import sys
import csv
import itertools
import re




def concatenatefiles(Basedirectory, outputdirectory):

	filenames = []
	outputnames = []
	basedirectories = []
	base_dir = Basedirectory
	for root, dirs, files in os.walk(base_dir):
		for d in dirs:
			outputname = d
			outputnames.append(outputname)

	for root, dirs, files in os.walk(base_dir):
		newbase_dir =root
		#print(newbase_dir)
		basedirectories.append(newbase_dir)
		#for root, dirs, files in os.walk(newbase_dir):
			#for f in files:
				#if f.endswith('_norm.txt'):
					#print(f)
					#filepath = os.path.join(root, f)
					#filenames.append(filepath)


	#print(outputnames)
	truebasedir = basedirectories[1:]

	REG = r'[F|M][A-Z]+[0-9]'
	#print(truebasedir)

	do_header = True
	for i in truebasedir:
		for root, dirs, files in os.walk(i):
			n = os.path.basename(root)
			filenames = []
			print(n)
			with open(outputdirectory + n + '.txt', 'w') as outfile:
				for f in files:
					if f.endswith('_norm.txt'):
						print(f)
						filepath = os.path.join(root, f)
						with open(filepath) as infile:
							for i, line in enumerate(infile):
								if not do_header and i < 3:
									continue
								outfile.write(line)
						do_header = False
			







				
	
# outputname = 'DR1Female.txt'
# with open('/Users/danielarthur/Downloads/FAVE-1.2.2/FAVE-extract/'+outputname, 'w') as outfile:
# 	for fname in filenames:
# 		with open(fname) as infile:
# 			for line in infile:
# 				outfile.write(line)



	



	
	



#print(true[8:])
				

			