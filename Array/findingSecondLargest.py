# using Sorting 
def getSecondLargest(arr):
    n =len(arr)
    arr.sort()

    for i in range(n-2,-1,-1):
        if arr[i]!=arr[n-1]:
            return arr[i]
        
    return -1

if __name__=="__main__":
    arr = [12, 34,10,9,13,90]

    print(getSecondLargest(arr))
