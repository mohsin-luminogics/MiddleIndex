# Time Complexity O(n)


def middleIndex(arr, i, j):
    if arr[i] == arr[j]:
        if i+1 == j-1:
            print(i+1)
            return
        if i+1 > j-1:
            print("NO Index Found")
            return
        if arr[i+1] == arr[j-1]:
            arr[j-1] = arr[j] + arr[j-1]
            j = j-1
            arr[i + 1] = arr[i] + arr[i + 1]
            i = i+1
        elif arr[i+1] > arr[j-1]:
            arr[j - 1] = arr[j] + arr[j - 1]
            j = j - 1
        elif arr[i+1] < arr[j-1]:
            arr[i + 1] = arr[i] + arr[i + 1]
            i = i + 1
    elif arr[i] > arr[j]:
        arr[j-1] = arr[j] + arr[j-1]
        j = j-1
    elif arr[i] < arr[j]:
        arr[i + 1] = arr[i] + arr[i + 1]
        i = i+1
    middleIndex(arr, i, j)


def main():
    arr = [1, 2, 1, 0]
    j = len(arr) - 1
    i = 0
    middleIndex(arr, i, j)


main()
