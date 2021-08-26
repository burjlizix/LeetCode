# optimization for bubble. 
def bubble_sorted_v2(array = []):
    for i in range(len(array)-1):
        is_sorted = True
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                is_sorted = False

        if is_sorted: #判定整个j循环是否都没有交换，如果整轮都没有交换则已经有序；而非j中是否有一次没有交换
            break

my_array = [5, 8, 6, 3, 9, 2, 1, 7]
bubble_sorted_v2(my_array)
print(my_array)
