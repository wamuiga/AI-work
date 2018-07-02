import csv
import random
import math
import operator
from collections import Counter
import numpy

class KNN():
	def __init__(self,data,no_nn):
		self.K=no_nn
		self.examples=data

	def classify(self,queryinstance):
		no_columns=len(queryinstance)
		distances=[]
		for x in range(len(self.examples)):
			dist=self.distance(queryinstance,self.examples[x],no_columns)
			distances.append((self.examples[x], dist))
		distances.sort(key=operator.itemgetter(1))
		print(distances)

		neighbors = []
		for x in range(self.K):
			neighbors.append(distances[x][no_columns-2][no_columns])
		print("Nearest :"+str(neighbors))

		#Use simple majority of the category of nearest neighbours as the prediction value of the query instance
		cnt = Counter(neighbors)
		print(cnt.most_common(1)[0][0])


	def distance(self,instance1, instance2, length):
		distance = 0
		for x in range(length):
			distance += pow((instance1[x] - instance2[x]), 2)
		return distance
