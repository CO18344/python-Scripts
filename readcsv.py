import csv

def getColumn(column,dictionaryList):
	for x in dictionaryList:
		yield float(x[column])

if __name__ == '__main__':

	with open('gendata.csv') as file:
		data = list(csv.DictReader(file)) 
		#list of dictionaries where each dictionary is a row

	print(sum(getColumn('age',data)))

	#own list of dictionary
	dl = [{'no':24},{'no':26},{'no':50},{'no':100},{'no':200}]
	print(sum(getColumn('no',dl)))