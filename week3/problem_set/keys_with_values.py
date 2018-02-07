def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here
    result = []
    for k in aDict.keys():
        if aDict[k] == target:
            result.append(k)
    return sorted(result)

print(keysWithValue({6: 'c', 2: 'b', 3: 'c'}, 'c'))