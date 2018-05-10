import os
import sys
myfiles=['a.txt','b.txt','c.txt']
for f in myfiles:
  print(os.path.join('/home/adhi/automatetheboringstuff/chapter8',f))
