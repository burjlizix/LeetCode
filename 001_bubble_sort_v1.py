# 001 bubble_sort
def bubble_sort_v1(array = []):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
my_array = [-4, -1, 0, 3, 9, 9, 29, 30, 42]
bubble_sort_v1(my_array)
print(my_array)


