def rec(y, z):
 return 108 - ((815-1500/z)/y)
 
def floatpt(N):
 x = [4, 4.25]
 for i in range(2, N+1):
  x.append(rec(x[i-1], x[i-2]))
 return x
 
def fixedpt(N):
 x = [Decimal(4), Decimal(17)/Decimal(4)]
 for i in range(2, N+1):
  x.append(rec(x[i-1], x[i-2]))
 return x
N = 20 
flt = floatpt(N)
fxd = fixedpt(N)
for i in range(N):
 print str(i) + ' | '+str(flt[i])+' | '+str(fxd[i])