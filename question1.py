def isDictKeysAllAlpha(d):
    for k in d.keys():
        if not str(k).isalpha():
            return False
    return True

print(isDictKeysAllAlpha({'a':2, 'b':3}))