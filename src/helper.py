#*** mencari nilai maksimum dalam suatu array ***#
def max_array(array):
    max = array[0]
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
    return max

#*** find index ***#
def find_index(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i+1
    return -1