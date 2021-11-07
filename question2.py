
def popByValue(_d, _v):
    result = []
    for k,v in list(_d.items()):
        if v == _v:
            result.append(_d.pop(k))
    return result

print(popByValue({'a':2, 'b':3, 'c':2}, 2))
