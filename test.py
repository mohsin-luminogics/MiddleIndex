
arr=[1,2,1,2,1]
def solution():
    for i in range(1,len(arr)):
        if i == len(arr)-1:
            print("NO Index Found")
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
index = solution()
print(index)