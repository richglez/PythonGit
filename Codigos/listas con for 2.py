lst = [0,1,2,3]
x=1 
#   0,1,2,3
for elem in lst:
    x*=elem  #1*0 = 0*1 = 0*2 = 0*3 = 0
print(x)


lst = [1,2,3,4]
x=1 
#   0,1,2,3
for elem in lst:
    x*=elem  #1*1 = 1*2 = 2*3 = 6*4 = 24
print(x)