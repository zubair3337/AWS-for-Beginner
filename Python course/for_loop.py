# in for loop 3 fundamental need to understand
# 1- start : 1
# 2- stop : 10
# 3- step : 

# for i in range(1,10): #1 is include and 10 is exclude
#     print(i)

m=int(input("Enter start Number :"))
n=int (input("Enter stop number :"))
z= n + 1 # this for include & exclude

for i in range(m, z, +1):
    print(m) #if we print till here it will print only 1,1,1,1
    m += 1 #now it will add +1