#分制思想；关键是找到每轮左右交换后left，left指针是分治界点，left指针指向的数值需要与基准元素交换位置
#两次交换的是值而非指针，指针唯一赋值为基准
def partition_v1(start_index, end_index, array = []):
    
    #初始状态
    pivot = array[start_index]  #基准 
    left = start_index 
    right = end_index

    #判定大小和交换
    while left != right:
        while left < right and array[right] > pivot:
            right -= 1
        while left < right and array[left] < pivot:
            left += 1
        if left < right:
            p = array[left]
            array[left] = array[right]
            array[right] = p

    array[start_index] = array[left]
    array[left] = pivot
    return left


#递归求解
def quick_sort(start_index, end_index, array = []):
    if start_index >= end_index:
        return

    pivot_index = partition_v1(start_index, end_index, array)
    quick_sort(start_index, pivot_index-1, array)
    quick_sort(pivot_index+1, end_index, array)
    
my_array = [3, 4, 2, 1, 5, -1, 6, 7, 8, -3, 10, 11, 12]
quick_sort(0, len(my_array)-1, my_array)
print(my_array)


