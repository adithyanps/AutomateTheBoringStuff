import time
def calcProd():
 prdct=1
 for i in range(1,100000):
  prdct=prdct * 2
 return prdct
starttime=time.time()
prod = calcProd()
endtime = time.time()
print("the result is %s digits long." % (len(str(prod))))
print("took %s seconds to calculate." % (endtime - starttime))
