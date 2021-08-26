#关键点是界点，界点后都有序，界点前重新排序（寻求新界点）直到完全有序。除初始化值外，最后交换处的点等于界点，因此sort_boder = last_exchange_index

def bubble_sort_v3(array =[]):
    last_exchange_index = 0
    sort_border = len(array)-1
    for i in range(len(array)-1):
        is_sorted = True
        for j in range(sort_border):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                is_sorted = False
                last_exchange_index = j #关键步骤
        
        sort_border = last_exchange_index  
        if is_sorted:
            break
my_array = [3, 4, 2, 1, 5, -1, 6, 7, 8, -3, 10, 11, 12]
bubble_sort_v3(my_array)
print(my_array)


'''
#进一步改进思路（主要是减少参数冗余）
def bubble_sort_v3(array =[]):
    
    #1.初始值煤气作用，更换为sort_boorder初始值
    #last_exchange_index = 0
    last_exchange_index = len(array)-1

    #1.sort_border与last_exchange_index等值，顾可被取代
    sort_border = len(array)-1
    for i in range(len(array)-1):
        
        #2.标志作用，可被取代
        #s_sorted = True

        #for j in range(sort_border):
        for j in range(last_exchange_index):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                #is_sorted = False
                last_exchange_index = j
        
        #sort_border = last_exchange_index
        
        #2.使用界点替代判定
        #if is_sorted:
        if last_exchange_index == 0:
            break

'''
'''
#简化表示
def bubble_sort_v3(array =[]):
    last_exchange_index = len(array)-1
    for i in range(len(array)-1):
        for j in range(last_exchange_index):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                last_exchange_index = j #关键步骤
     
        if last_exchange_index == 0:
            break
'''
