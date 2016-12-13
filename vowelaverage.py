

from __future__ import division
import os 
import numpy as np
import sys
import csv
import itertools
import re

import glob
vowels = ['AE', 'AO', 'AA','IH','ER', 'OW','AW','AH','EH','EY','OY', 'IY', 'UH', 'UW']

blah = list()

NEM = 0
NEF = 0 #this is a list of counters for the different regions
WestM = 0
NMM = 0
SMM = 0
NorthM = 0
SouthM = 0
NYM = 0
WestF = 0
NMF = 0
SMF = 0
NorthF = 0
SouthF = 0
NYF = 0

def read_file(filepath):
	parsed = []
	with open(filepath, 'r') as f:
		reader = csv.reader(f, delimiter = '\t')
		for line in reader:
			parsed.append((line[0],float(line[3]),float(line[4])))
	return parsed


def VowelAverageandKnnTestLabels(DirectoryTest1):
	vowels = ['AE', 'AO', 'AA','IH','ER', 'OW','AW','AH','EH','EY','OY', 'AY', 'IY', 'UH', 'UW']
	speaker_averages = {}
	dialects = {}
	TrueLabels = []

	for root, dirs, files in os.walk(DirectoryTest1):
		#
		FILEZ = []

		q = glob.glob(root + '/*.txt')

	
		


		for i in q:
			#print(i)
			parsed = read_file(i)
			all = {k: [] for k in vowels}
		



		#vowel is the list of vowels in the Text file, F1 is the list of F1 values, F2 is the list of F2 values.  


		#vowelvector produces a triplet consisting of : (vowel, F1 value, F2 value)

		# VOWELS THAT ARE NOT WORKING: AW, UH, OY, AY

		#regexIY finds all triplets in vowelvector for the vowel IY.  IY must be changed for all vowels, everything else can stay the same.  

			for k in all.keys():
				all[k] = [x for x in parsed if x[0] == k]

			#print(all)


		#iyall is now a list of triplets consisting of: (IY, F1 value for IY, F2 value for IY)


			averages = {k: (sum(x[1] for x in v)/ len(v), sum(x[2] for x in v)/ len(v)) for k, v in all.items() if v}


			
			speaker_name = os.path.splitext(os.path.basename(i))[0]
			dialect_region = os.path.basename(root)
			#print(speaker_name)
			speaker_averages[speaker_name] = averages
			if dialect_region not in dialects:
				dialects[dialect_region] = []
			dialects[dialect_region].append(speaker_name)

	
	#print(dialects)

	for k,v in dialects.items():
		for speaker in v:
			for vow in vowels:
				if vow not in speaker_averages[speaker]:
					continue
			try:		

							
				TrueLabels.append(k)
			except KeyError:
				continue
		return TrueLabels

				

def VowelAverageandKnnTest(DirectoryTest):
	vowels = ['AE', 'AO', 'AA','IH','ER', 'OW','AW','AH','EH','EY','OY', 'AY', 'IY', 'UH', 'UW']
	speaker_averages = {}
	dialects = {}
	TrueLabels = []

	for root, dirs, files in os.walk(DirectoryTest):
		#
		FILEZ = []

		q = glob.glob(root + '/*.txt')

	
		


		for i in q:
			#print(i)
			parsed = read_file(i)
			all = {k: [] for k in vowels}
		



		#vowel is the list of vowels in the Text file, F1 is the list of F1 values, F2 is the list of F2 values.  


		#vowelvector produces a triplet consisting of : (vowel, F1 value, F2 value)

		# VOWELS THAT ARE NOT WORKING: AW, UH, OY, AY

		#regexIY finds all triplets in vowelvector for the vowel IY.  IY must be changed for all vowels, everything else can stay the same.  

			for k in all.keys():
				all[k] = [x for x in parsed if x[0] == k]

			#print(all)


		#iyall is now a list of triplets consisting of: (IY, F1 value for IY, F2 value for IY)


			averages = {k: (sum(x[1] for x in v)/ len(v), sum(x[2] for x in v)/ len(v)) for k, v in all.items() if v}


			
			speaker_name = os.path.splitext(os.path.basename(i))[0]
			dialect_region = os.path.basename(root)
			#print(speaker_name)
			speaker_averages[speaker_name] = averages
			if dialect_region not in dialects:
				dialects[dialect_region] = []
			dialects[dialect_region].append(speaker_name)

	
	#print(dialects)

	for k,v in dialects.items():
		for speaker in v:
			for vow in vowels:
				if vow not in speaker_averages[speaker]:
					continue
			
				return(speaker_averages[speaker])
				

			
				




				# taveragemasterlist = []
				# a_list = []


				# #print(testaverages)




				# for k in testaverages.values():
				# 	a_list.append([k[0], k[1]])
				#print( speaker_averages[speaker])
				#print(a_list)


def VowelAverageandKnn(Directory, desiredvowel, testdirectory):
	vowels = ['AE', 'AO','UH', 'UW', 'AA','IH','ER', 'OW','AW','AH','EH','EY','OY', 'AY', 'IY']
	speaker_averages = {}
	dialects = {}
	predlabels = []
	NEM = 0
	NEF = 0 #this is a list of counters for the different regions
	WestM = 0
	NMM = 0
	SMM = 0
	NorthM = 0
	SouthM = 0
	NYM = 0
	WestF = 0
	NMF = 0
	SMF = 0
	NorthF = 0
	SouthF = 0
	NYF = 0
	for root, dirs, files in os.walk(Directory):
		#
		FILEZ = []

		q = glob.glob(root + '/*.txt')
	
		# for i in q:
		# 	print(i)


		for i in q:
			#print(i)
			parsed = read_file(i)
			all = {k: [] for k in vowels}
		



		#vowel is the list of vowels in the Text file, F1 is the list of F1 values, F2 is the list of F2 values.  


		#vowelvector produces a triplet consisting of : (vowel, F1 value, F2 value)

		# VOWELS THAT ARE NOT WORKING: AW, UH, OY, AY

		#regexIY finds all triplets in vowelvector for the vowel IY.  IY must be changed for all vowels, everything else can stay the same.  

			for k in all.keys():
				all[k] = [x for x in parsed if x[0] == k]

			#print(all)


		#iyall is now a list of triplets consisting of: (IY, F1 value for IY, F2 value for IY)


			averages = {k: (sum(x[1] for x in v)/ len(v), sum(x[2] for x in v)/ len(v)) for k, v in all.items() if v}


			
			speaker_name = os.path.splitext(os.path.basename(i))[0]
			dialect_region = os.path.basename(root)
			#print(speaker_name)
			speaker_averages[speaker_name] = averages
			if dialect_region not in dialects:
				dialects[dialect_region] = []
			dialects[dialect_region].append(speaker_name)

	
	#print(dialects)

	from sklearn.neighbors import KNeighborsClassifier
	for wantedvowel in vowels:
		if desiredvowel == wantedvowel:
			X = []
			Y = []
			for k,v in dialects.items():
				for speaker in v:
					for vow in vowels:
						if vow not in speaker_averages[speaker]:
							continue
							
					try:		

						Y.append(k)
						X.append(speaker_averages[speaker][vow])
					except KeyError:
						continue

					#Y.append(k)

					#print(desiredvowel)	
					#print(speaker_averages[speaker][desiredvowel])
					#Y.append(k)
			#print(Y)
			#print(X)
			neigh = KNeighborsClassifier(n_neighbors=2, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='minkowski', metric_params=None, n_jobs=1)
			neigh.fit(X, Y) 

			taveragemasterlist = []
			a_list = []

			#print((VowelAverageandKnnTest('/Users/danielarthur/Downloads/FAVE-1.2.2/ConcatenatedSpeakerFIles').items()))

		



			for k, v in VowelAverageandKnnTest(testdirectory).items(): #Test Data
				if k == desiredvowel:
					print(k)

					#print(v)
					a_list.append([v[0], v[1]])
					

	
			#print(a_list)

			


			try :
				purpdictor = neigh.predict(a_list)
			except ValueError:
				continue
			# array = list(VowelAverageandKnnTestLabels('/Users/danielarthur/Downloads/FAVE-1.2.2/ConcatenatedSpeakerFIles/WesternFemale'))
			# print(array)

			labels = purpdictor
			# print(len(a_list))
			# neigh.score(a_list, array)
			print(labels)
			
			blah.append(str(labels))
		
			NEM = 0
			NEF = 0 #this is a list of counters for the different regions
			WestM = 0
			NMM = 0
			SMM = 0
			NorthM = 0
			SouthM = 0
			NYM = 0
			WestF = 0
			NMF = 0
			SMF = 0
			NorthF = 0
			SouthF = 0
			NYF = 0
			lab = []


			# for l in labels:
			# 	#print(l)
				
			

			# 	if l == 'WesternMale':
			# 		WestM +=1
			# 	elif purpdictor == 'WesternFemale':
			# 		WestF += 1
			# 	elif purpdictor == 'NorthMidlandMale':
			# 		NMM += 1
			# 	elif purpdictor == 'SouthMidlandMale':
			# 		SMM += 1
			# 	elif purpdictor == 'NorthernMale':
			# 		NorthM += 1	
			# 	elif purpdictor == 'SouthernMale':
			# 		SouthM += 1	
			# 	elif purpdictor == 'NewYorkCityMale':
			# 		NYM +=1
			# 	elif purpdictor == 'NewEnglandMale':
			# 		NEM +=1
			# 	elif purpdictor == 'NewEnglandFemale':
			# 		NEF +=1
				
			# 	elif purpdictor == 'NorthMidlandFemale':
			# 		NMF += 1
			# 	elif purpdictor == 'SouthMidlandFemale':
			# 		SMF += 1
			# 	elif purpdictor == 'NorthernFemale':
			# 		NorthF += 1	
			# 	elif purpdictor == 'SouthernFemale':
			# 		SouthF += 1	
			# 	elif purpdictor == 'NewYprintorkCityFemale':
			# 		NYF += 1
			# 	#print(SouthF)
			# 	lab.append(SouthF)
			# 	regionVal = {'NewEnglandMale': NEM, 'WesternMale': WestM, 'NorthMidlandMale': NMM, 'SouthMidlandMale': SMM, 'NorthernMale': NorthM, 'SouthernMale': SouthM, 'NewYorkCityFemale': NYF, 'NewEnglandFemale': NEF, 'WesternFemale': WestF, 'NorthMidlandFemale': NMF, 'SouthMidlandFemale': SMF, 'NorthernFemale': NorthF, 'SouthernFemale': SouthF, 'NewYorkCityMale': NYM}
		
			
			#print(blah)
				
				#print(predlabels)
				#(max(set(blah), key = blah.count))
			return blah
			#array = list(VowelAverageandKnnTestLabels('/Users/danielarthur/Downloads/FAVE-1.2.2/ConcatenatedSpeakerFIles/NewYorkCityFemale'))
			#print(array)



			#return(neigh.score(a_list, [['WesternFemale']]))


x = list()


for truevowel in vowels:
	x = (VowelAverageandKnn('/Users/danielarthur/Downloads/FAVE-1.2.2/ConcatenatedSpeakerFIles', truevowel, '/Users/danielarthur/Downloads/FAVE-1.2.2/ConcatenatedTest/NorthMidlandMale/1')) #From ConcatenatedSpeakerFIles - trains the KNN

accuracy = 0
print(x)

for i in x:
	if i == "['Western']":
		accuracy += 1
trueaccuracy = accuracy/len(x)
print(trueaccuracy)
#print(VowelAverageandKnnTestLabels('/Users/danielarthur/Downloads/FAVE-1.2.2/ConcatenatedSpeakerFIles/WesternFemale'))

# def predictor(predictedlabel):
# 	for truevowel in vowels:
# 		predictedlabel = (VowelAverageandKnn('/Users/danielarthur/Downloads/FAVE-1.2.2/ConcatenatedSpeakerFIles', truevowel))

	


		# print('Average for IY F1 :' + str(IYF1avg))
		# print('Average for IY F2 :' +str(IYF2avg))
		# print('AO F1: ' + str(AOF1avg))
		# print('AO F2: ' + str(AOF2avg))
		# #print('AW F1' + str(AWF1avg))
		# #print('AW F2 : ' +str(AWF2avg))
		# print('EY F1:' +str(EYF1avg))
		# print('EY F2:' +str(EYF2avg))
		# print('AH F1:' +str(AHF1avg))
		# print('AH F2:' +str(AHF2avg))
		# #print('OY F1' + str(OYF1avg))
		# #print('OY F2' +str(OYF2avg))
		# print('Average for AE F1 :' + str(AEF1avg))

		
		# # print(AWF2avg)
		# # print(EYF2avg)
		# # print(AHF2avg)
		# # print(OYF2avg)
		# print('Average for AE F2 :' + str(AEF2avg))


	# IYF2avg = 'Average for AO F1 :' + (sum(F2iylist)/len(F2iylist))
	# 	AOF2avg = 'Average for AO F1 :' + (sum(F2aolist)/len(F2aolist))
	# 	AWF2avg = 'Average for AW F1 :' +	(sum(F2awlist)/len(F2awlist))
	# 	EYF2avg = 'Average for EY F1 :' +	(sum(F2eylist)/len(F2eylist))
	# 	AHF2avg = 'Average for AH F1 :' +	(sum(F2ahlist)/len(F2ahlist))
	# 	OYF2avg = 'Average for OY F1 :' +	(sum(F2oylist)/len(F2oylist))
	# 	AEF2avg = 'Average for AE F1 :' +	(sum(F2aelist)/len(F2aelist))

	#average of F2