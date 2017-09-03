#!venv/bin/python
'''
calssify item based on weight & surface
work with apple and orange only
'''
from sklearn import tree
import csv

with open('data/apple-orange.csv') as data_file:
  next(data_file,None)
  rows = csv.reader(data_file,delimiter=',')
  features = []
  labels = []
  for row in rows:
    isBumpy = 1 if row[1] == "Bumpy" else 0
    isOrange = 1 if row[2] == "Orange" else 0
    features.append([int(row[0]),isBumpy])
    labels.append(isOrange)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
try:
  weight  = int(input('please enter item weight ex:150\n'))
except:
  print("please enter integer only. exiting now")

surface = input('please enter what the surface look like Bumpy or Smooth:\n')
surface = 1 if surface == "Bumpy" else 0
prediction = clf.predict([[weight,surface]])
result = "Orange" if prediction == 1 else "Apple"
print("based on your input the item is: "+result)
