#//向下取整，/浮点运算
def cocktail_sort(array=[]):
    for i in range(len(array)//2):
        is_sorted = True
        for j in range(i,len(array)-1-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                is_sorted = False
        if is_sorted:
            break

        is_sorted = True  #初始化
        for j in range(len(array)-1-i,i,-1):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp

                is_sorted = False
        if is_sorted:
            break

my_array = [3, 4, 2, 1, 5, -1, 6, 7, 8, -3, 10, 11, 12]
cocktail_sort(my_array)
print(my_array)   
            


     