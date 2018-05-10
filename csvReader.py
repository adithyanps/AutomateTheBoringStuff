import csv
a=open('ex.csv')
b=csv.reader(a)
c=list(b)
print c
