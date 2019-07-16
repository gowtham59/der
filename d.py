lo11,lo12=map(int,input().split())
p13=lo11*lo12
for i in range(0,p13+1):
 if(i**2==0):
  print("yes")
  break
else:
  print("no")
