def partition(arr,min,max):
    i= min-1
    pivot= arr[max]
    for j in range(min,max):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[max]=arr[max],arr[i+1]
    return i+1
def quicksort(arr,min,max):
    if min<max:
        pi=partition(arr,min,max)
        quicksort(arr,min,pi-1)
        quicksort(arr,pi+1,max)

arr=[10,7,8,9,1,5]
n=len(arr)
quicksort(arr,0,n-1)
print("Sorted Array")
for i in range(n):
    print(arr[i])


