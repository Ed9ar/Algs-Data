def selection_sort(arr):
    marker = 0
    swap = True
    while marker < len(arr):
        for i in range(marker, len(arr)):
            if arr[i] < arr[marker]:
                arr[marker], arr[i] = arr[i], arr[marker]
        print(arr)
        marker+=1

l = [6,8,1,4,10,7,8,9,3,2,5]
selection_sort(l)