def quiksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[len(array)/2]
        less = [i for i in array[1:] if i <= pivot]
        more = [i for i in array[1:] if i > pivot]
        return quiksort(less)+[pivot]+quiksort[more]
