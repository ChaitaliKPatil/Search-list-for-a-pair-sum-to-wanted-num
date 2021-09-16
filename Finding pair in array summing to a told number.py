arr=[]
num=int(input("number of array elements: "))
print("Enter the numbers in an array:")
for _ in range(num):
    a=int(input())
    arr.append(a)
print("Your array is:\t",arr, '\tArray size= \t',len(arr))
Y=int(input("ENter a number to find a pair which sums up to your set number: \t"))
pair=[]
i=0
while i+1<len(arr):
    for x in range(i+1,len(arr)):
        if arr[i]+arr[x]==Y:
            pair.append([arr[i],arr[x]])
    i+=1  
if len(pair)==0:
    print("Sorry, there is no such pair which sum to number ",Y) 
print(pair)
