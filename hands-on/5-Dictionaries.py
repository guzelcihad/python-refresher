# Actually this is hashtable
# Keys have to be immutable and unique

firstDict = {"key1": 1, "key2": 2, "key3": 3}
firstDict
print(type(firstDict))

firstDict["key1"]

firstDict[(0,1)]

firstDict.keys()

firstDict.values()

firstDict['key1'] = 2
firstDict

del(firstDict['key1'])
firstDict

# verify the key is in dict
'key1' in firstDict
'key2' in firstDict