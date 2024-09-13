def maxminnum(arr):
    if not arr:
        return "list id empty"
    small_num_cont=arr[0]
    big_num_cont=arr[0]
    for index in range(1,len(arr)):
        if arr[index] < small_num_cont:
            small_num_cont= arr[index]
        elif arr[index] > big_num_cont:
            big_num_cont = arr[index]
    return big_num_cont,small_num_cont   

arr=[5,7,30,9,-3,7,-88]
print(maxminnum(arr))

