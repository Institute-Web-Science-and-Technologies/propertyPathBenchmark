import sys

queryResultDir     = str(sys.argv[1])
referenceResultDir = str(sys.argv[2])


#Returns a touple (x,y) Where x is the completeness of results and y is the soundness
def CalculateSoundComp(queryResultDir, referenceResultDir):
	resultSet = set()
	referenceResultSet = set()
	#turn reference and result set in set 
	with open(queryResultDir) as result:
		for line in result:
			resultSet.add(str(line).rstrip())

	with open(referenceResultDir) as reference:
		for line in reference:
			referenceResultSet.add(str(line).rstrip())
	if len(resultSet) == 0:
		return (0,0)

	intersection = float(len(resultSet & referenceResultSet))

	print intersection
	print len(resultSet)


	soundness    = intersection / len(referenceResultSet)
	completeness = intersection / len(resultSet)
	return (completeness,soundness)

print CalculateSoundComp(queryResultDir,referenceResultDir)
