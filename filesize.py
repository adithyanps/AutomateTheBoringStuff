import os
totalSize = 0
for filename in os.listdir('/home/adhi/automatetheboringstuff/chapter7'):
 totalSize = totalSize + os.path.getsize(os.path.join('/home/adhi/automatetheboringstuff/chapter7',filename))
print(totalSize)
