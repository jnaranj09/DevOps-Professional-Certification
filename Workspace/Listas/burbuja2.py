array = [4,3,2,1]
length = len(array)
for j in range(length-1):
    print(j)
    for i in range(length-1):
        if array[i] > array[i+1]:
            temp=array[i]
            array[i] = array[i+1]
            array[i+1] = temp
            print(array)
