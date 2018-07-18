
# coding: utf-8

# In[8]:

a = [3,1,5,7,9,8,4,2]


# In[5]:


# 1.冒泡: 时间复杂度：O(n²); 空间复杂度：O(1); 稳定性：稳定
def bubble_sort(a):
    n = len(a)
    for i in reversed(range(n)):
        for j in range(1, i+1):
            if a[j-1]>a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a

# 2.简单选择排序: 时间复杂度：O(n²); 空间复杂度：O(1); 稳定性：不稳定
# 选择待排序队列中最小的数放到已排序队列的最后
def select_sort(array):
    for i in range(len(array)):
        x = i
        for j in range(i+1, len(array)):
            if array[j] < array[x]:
                x = j
        array[i], array[x] = array[x], array[i]
    return array

# 3.直接插入排序: 时间复杂度：O(n²); 空间复杂度：O(1); 稳定性：稳定
# 将一个待排序的数插入到已排序的队列
def insert_sort(array):
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            temp = array[i]
            j = i-1
            while array[j]>temp and j>=0:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = temp
    return array

# 4.希尔排序: 时间复杂度：O(n); 空间复杂度：O(n√n); 稳定性：不稳定
# 希尔排序（Shell Sort）是插入排序的改进版本，其核心思想是将原数据集合分割成若干个子序列，
# 然后再对子序列分别进行直接插入排序，使子序列基本有序，最后再对全体记录进行一次直接插入排序。
def shell_sort(array):
    increment = len(array)
    while increment > 1:
        increment = int(increment/3)+1
        for i in range(increment, len(array)):
            if array[i] < array[i - increment]:
                temp = array[i]
                j = i - increment
                while j >= 0 and temp < array[j]:
                    array[j+increment] = array[j]
                    j -= increment
                array[j+increment] = temp 
    return array
                
# 5.堆排序: 时间复杂度：O(nlog₂n); 空间复杂度：O(1); 稳定性：不稳定
# 堆是具有下列性质的完全二叉树：每个分支节点的值都大于或等于其左右孩子的值，称为大顶堆；
# 每个分支节点的值都小于或等于其做右孩子的值，称为小顶堆；因此，其根节点一定是所有节点中最大（最小）的值。
# 其核心思想是：将待排序的序列构造成一个大顶堆。此时，整个序列的最大值就是堆的根节点。
# 将它与堆数组的末尾元素交换，然后将剩余的n-1个序列重新构造成一个大顶堆。反复执行前面的操作，最后获得一个有序序列。
def heap_sort(array):
    def heap_adjust(parent, m):
        child = 2 * parent + 1  # left child
        while child < m:
            if child + 1 < m:
                if array[child + 1] > array[child]:
                    child += 1  # right child
            if array[parent] >= array[child]:
                break
            array[parent], array[child] =                 array[child], array[parent]
            parent, child = child, 2 * child + 1  # 下移，继续调整

    i = int(len(array)/2)
    while i >=0:
        heap_adjust(i, len(array))
        i -= 1
    j = len(array)
    while j> 0:
        array[0], array[j-1] = array[j-1], array[0]
        heap_adjust(0, j-1)
        j -= 1
    return array

# 6.快速排序: 时间复杂度：O(nlog₂n); 空间复杂度：O(nlog₂n); 稳定性：不稳定
def quick_sort(array):
    def partition(low, high):
        if low>=high:
            return
        l = low
        r = high
        pivot = array[l]
        while l < r:
            while l<r and array[r]>=pivot:
                r -= 1
            array[l], array[r] = array[r], array[l]
            while l<r and array[l]<=pivot:
                l += 1
            array[l], array[r] = array[r], array[l]
        partition(low, l-1)
        partition(l+1, high)
    
    partition(0, len(array)-1)
    return array
    

# 7.归并排序: 时间复杂度：O(nlog₂n); 空间复杂度：O(1); 稳定性：稳定
def merge_sort(array):
    def merge_arr(arr_l, arr_r):
        array = []
        while len(arr_l) and len(arr_r):
            if arr_l[0] <= arr_r[0]:
                array.append(arr_l.pop(0))
            else:
                array.append(arr_r.pop(0))
        if len(arr_l):
            array += arr_l
        else:
            array += arr_r
        return array
    def recursive(array):
        if len(array)==1:
            return array
        mid = len(array)//2
        arr_l = recursive(array[:mid])
        arr_r = recursive(array[mid:])
        return merge_arr(arr_l, arr_r)
    return recursive(array)

# 8.基数排序: 时间复杂度：O(d(r+n)); 空间复杂度：O(rd+n); 稳定性：稳定
def radix_sort(array):
    bucket, digit = [[]], 0
    while len(bucket[0]) != len(array):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(array)):
            num = (array[i] // 10 ** digit) % 10
            bucket[num].append(array[i])
        array = []
        for i in range(len(bucket)):
            array += bucket[i]
        digit += 1
    return array

arr = [3,1,5,7,9,8,4,2, 6]
a = radix_sort(arr)
print a


# In[ ]:




# In[ ]:



