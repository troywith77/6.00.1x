animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if len(aDict) == 0:
      return None
    valueNum = []
    for v in aDict.values():
      valueNum.append(len(v))
    maxNum = max(valueNum)
    for k in aDict.keys():
      if len(aDict[k]) == maxNum:
        return k

print(biggest(animals))