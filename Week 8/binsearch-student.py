
def binsearch(mylist, key):
    left=0
    right=len(mylist) - 1
    while right > left:
        mid = (right + left) // 2
        print("left = ", str(left), ",right = ", str(right), "mid = ", str(mid))
        if mylist[mid] == key:
            return mid
        elif mylist[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    if mylist[left]==key:
        return left
    else:
        raise Exception



