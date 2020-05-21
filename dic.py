def getKeysValues(dicObj):
	return list(dicObj.keys()),list(dicObj.values())

def getItemsFromDic(dicObj):
	return list(dicObj.items())

if __name__ == '__main__':
	x ={'name':'satvik',
	'gender':'male'}
	print(x)
	keys,values = getKeysValues(x)
	print(keys)
	print(values)