__author__ = 'Peter'
import csv
import random
import math
import operator
from collections import Counter
import numpy
import re
import pickle

class KMC():
	def __init__(self,data,no_cl,ctype):
		self.K=no_cl
		self.examples=data
		self.centers=[]
		if re.match(ctype,'FK'):
			for x in range(self.K):
				##PROBLEM THAT WHEN CENTER IS MODIFIED, EVEN EXAMPLES ARE MODIFIED
				self.centers+=[self.examples[x]]
		else:

			for i in range(self.K):
				cent=[]
				for j in range(len(self.examples[i])):
					cent.append(random.random())
				self.centers.append(cent)
		

	def cluster2(self):
		groups=[]
		changed_group=True
		for e in range(len(self.examples)):
			groups.append(math.inf)
		
		
		print("Initial centers "+str(self.centers))
		print("Initial Group Matrix "+str(groups))
		while changed_group:
			changed_group=False
			for ex in range(len(self.examples)):
				least=math.inf
				for cent in range (len(self.centers)):
					dist=self.distance(self.centers[cent], self.examples[ex],2)
					if dist<least:
						groupNo=cent
						least=dist
					#print(dist)
				if groups[ex]!=groupNo:
					groups[ex]=groupNo
					changed_group=True
			print("Group Matrix "+str(groups))
			self.calculateNewCenters(groups)
		print(str(groups)+"\n")

	def save_object(self, obj,filename):
		with open(filename, 'wb') as output:  # Overwrites any existing file.
			pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)			
			
	def calculateNewCenters(self,groups):
		cent=[]
		print("Old Centers "+str(self.centers))
		print("Examples b4 "+str(self.examples))
		for cc in range(len(self.centers)):
			cent.append([0,0])
		print("Examples afterzeroing "+str(self.examples))
		for g in range(len(groups)):
			countmember=groups.count(groups[g])
			groupNo=groups[g]
			cent[groupNo][0]=self.examples[g][0]
			cent[groupNo][1]+=self.examples[g][1]
			#print(self.examples)	
		self.centers=cent
		print(self.centers)
		for cc in range(len(self.centers)):
			self.centers[cc][0]=self.centers[cc][0]/groups.count(cc)
			self.centers[cc][1]=self.centers[cc][1]/groups.count(cc)
			pass
		print("New Centers "+str(self.centers))		
		print('\n')


	def distance(self,instance1, instance2, length):
		distance = 0
		for x in range(length):
			distance += pow((instance1[x] - instance2[x]), 2)
		return math.sqrt(distance)

	def open_binfile(self):
		with open('kmsmodel.pkl', 'rb') as input:
			company1=pickle.load(input)
			print(company1.name)  # -> banana
			print(company1.value)  # -> 40




data=[
	[1,1],
	[2,1],
	[4,3],
	[5,4]
]
model=KMC(data,2,'FK')
model.cluster2()
#model.save_object(model,'kmcmodel.n3c')



















