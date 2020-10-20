#冒泡排序
def bubble(List):
    if len(List)<=1:
        return List
    for i in range(1,len(List)):
        for j in range(0,len(List)-i):
            if List[j]>List[j+1]:
                List[j],List[j+1]=List[j+1],List[j]
    return List


#选择排序
def Select(List):
    if len(List)<=1:
        return List
    for i in range(len(List)):
        min=i
        for j in range(i,len(List)):
            if List[min]>List[j]:
                min=j
        List[min],List[i]=List[i],List[min]
    return List


#希尔排序
def shellsort(List):
    if len(List)<=1:
        return List
    step=len(List)//2
    while step>0:
        for i in range(step,len(List)):
            while i>=step and List[i]<List[i-step]:
                List[i],List[i-step]=List[i-step],List[i]
                i-=step
        step//=2
    return List


#插入排序
def insert(List):
    if len(List)<=1:
        return List
    for right in range(len(List)):
        target=List[right]
        for left in range(right):
            if target<=List[left]:
                List[left+1:right+1]=List[left:right]
                List[left]=target
                break
    return List


#归并排序
def mergesort(List):
    if len(List)<=1:
        return List
    mid=len(List)//2
    left,right=List[:mid],List[mid:]
    return mergelist(mergesort(left),mergesort(right))


def mergelist( left, right):
    iList = []
    while left and right:
        if left[0]<=right[0]:
            iList.append(left.pop(0))
        else:
            iList.append(right.pop(0))
    while left:
        iList.append(left.pop(0))
    while right:
        iList.append(right.pop(0))
    return iList


#快速排序
def quicksort(List):
    if len(List)<=1:
        return List
    left,right=[],[]
    for i in List[1:]:
        if i <=List[0]:
            left.append(i)
        else:
            right.append(i)
    return quicksort(left)+[List[0]]+quicksort(right)


#计数排序
def countsort(List):
    if len(List)<=1:
        return List
    iList=[None]*len(List)
    for i in range(len(List)):
        small=0
        same=0
        for j in range(len(List)):
            if List[j]<List[i]:
                small+=1
            if List[j]==List[i]:
                same+=1
        for k in range(small,small+same):
            iList[k]=List[i]
    return iList


#堆排序
def heaprify(List,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and List[largest]<List[l]:
        largest=l
    if r<n and List[largest]<List[r]:
        largest=r
    if largest!=i:
        List[largest],List[i]=List[i],List[largest]
        return heaprify(List,n,largest)


def heapsort(List):
    n=len(List)
    for i in range(n,-1,-1):
        heaprify(List,n,i)
    for i in range(n-1,0,-1):
        List[i],List[0]=List[0],List[i]
        heaprify(List,i,0)
    return List


#二分查找
def binarysearch(List,A):
    left=0
    right=len(List)-1
    while right-left>1:
        middle=(left+right)//2
        if A<List[middle]:
            right=middle
        elif A>List[middle]:
            left=middle
        else:
            return middle
    if A==List[right]:
        return right
    elif A==List[left]:
        return left
    else:
        return -1


# 斐波那契查找
def fibsearch(List,A):
    left=0
    right=len(List)-1
    k=1
    while fib(k)<len(List):
        k+=1
    while right-left>1:
        mid=(left+fib(k-1))
        if A<List[mid]:
            right=mid-1
            k-=1
        elif A>List[mid]:
            left=mid+1
            k-=2
        else:
            return mid
    if A==List[left]:
        return left
    elif A==List[right]:
        return right
    else:
        return-1


def fib(n):
    List=[1,1]
    while n>1:
        List.append(List[-1]+List[-2])
        n-=1
    return List[-1]
