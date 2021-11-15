def newDict(list1, list2):
    if len(list1) == len(list2):
        return dict(zip(list1, list2))
    else:
        return None

print(newDict(['liza', 'is', 'studying', 'pyhton'], [1,2,3,4]))