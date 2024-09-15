def arr_reverse(arr):
    reversed=[]
    index = len(arr)
    if not arr:
        return None
    while index >= 0:
        reversed.append(arr[index-1])
        index-=1
    return reversed
        
arr = [7,7,5,5,67,7,6,7,0]
print(arr_reverse(arr))
