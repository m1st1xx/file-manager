def sum_par(arr,tarsum):
    arr.sort()
    pairs=[]
    left=0
    right=len(arr)-1
    while left<right:
        sum=arr[left]+arr[right]
        if sum==tarsum:
            pairs.append((arr[left],arr[right]))
            left+=1
            right-=1
        if sum<tarsum:
            left+=1
        if sum>tarsum:
            right-=1

    return pairs
print(sum_par([1,2,3,4,5,6],7))