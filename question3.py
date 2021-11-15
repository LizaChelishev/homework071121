def compareDict(dict1, dict2):
    for k1,v1 in dict1:
        for k2,v2 in dict2:
            if k1 == k2 and v1 == v2:
                return True
    return False

compareDict({'liza':12, 'python':13, 'bibi':14}, {'liza':12, 'python':13, 'bibi':14})