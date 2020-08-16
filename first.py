import sys
def sorting(arr,n):
        start=0
        end=n-1

        while(start<n-1 and arr[start]<arr[start+1]):
                start=start+1
        
        while(end>0 and arr[end]>arr[end-1]):
                end=end-1                
        
        if(abs(start-end)==n-1):
                return -1
        else:
                minimum=sys.maxsize
                maximum=-sys.maxsize
                for i in range(start,end+1):
                        minimum=min(minimum,arr[i])
                        maximum=max(maximum,arr[i])


                i=0
                while(i<start and minimum>arr[i]):
                        i=i+1

                j=n-1
                while(j>=end and maximum<arr[j]):
                        j=j-1

                print(f"Subarray which needs to be sorted is from {i} to {j}")
                print("Minimum elements which need to be sorted is: ",j-i+1)


n=int(input("Enter number of elements "))
print("Enter elements :")
arr=[]
for i in range(0,n):
        z=int(input())
        arr.append(z)

if(sorting(arr,n)==-1):
        print("Array is already sorted")