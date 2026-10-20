sum =0
for i in range(10+1):
    sum+=i

print(sum)

for i in range(0,10,2):
    print(i)
print("==============")
for i in range(10,0,-1):
    print(i)
print("===============")
color =["red","gree","yellow"]
for i in range(len(color)):
    print(color[i])
print("=============")
bangchucai=["A","B","C","D"]

for i in bangchucai:
    print(i)

# bảng cửu chương 
for i in range(10):
    for j in range(10+1):
        print("{0} x{1} ={2} ".format(i,j,i*j))
    print("===========")



# vong lap while 
n =-1

while (n<0):
    n=int(input("nhap vao so n "))

i =0
tong =0
while(i<n):
    tong +=i
    i+=1


