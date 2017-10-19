#This script turns a nq file to a nt file by deleting the respective graph of each quad
def convert(file):
	total = 0
	tripleFile = open("btc2014.nt","w") 
	with open(file) as f:
		print "Start Converting"
		for line in f:
			quad = line
			triple = quad.rsplit("<",1)[0] + ". \n"
			tripleFile.write(triple)
			total = total +1
			if total % 50000 == 0:
				print str(total) + " triples processed"
	tripleFile.close



#replaces blank nodes with unique uri
def replaceBlankNodes(file):
	blankNodes = {} #holds blank node identifier as key and unique uri as value
	total = 0
	currentBlanknode = 0
	replaceFile = open("btc2014preProcessed.nt", "w")
	with open(file) as f:
		print "Start replacing blank nodes"
		for line in f:
			triple = line.split(" ",2)
			if triple[0].startswith("_:"):
				if triple[0] in blankNodes:
					triple[0] = blankNodes[triple[0]]
				else:
					blankNodes.update({triple[0]:"<http://blankNodePropertyPathBenchmark/"+str(currentBlanknode)+">"})
					triple[0] = "<http://blankNodePropertyPathBenchmark/"+str(currentBlanknode)+">"
					currentBlanknode = currentBlanknode + 1
			if triple[2].startswith("_:"):
				triple[2] = triple[2].replace(".","")
				triple[2] = triple[2].replace(" ","")
				triple[2] = triple[2].replace("\n","")
				if triple[2] in blankNodes:
                                        triple[2] = blankNodes[triple[2]]
                                else:
                                        blankNodes.update({triple[2]:"<http://blankNodePropertyPathBenchmark/"+str(currentBlanknode)+">"})
                                        triple[2] = "<http://blankNodePropertyPathBenchmark/"+str(currentBlanknode)+"> . \n"
                                        currentBlanknode = currentBlanknode + 1

			line = triple[0] + " " + triple[1] + " " + triple[2] + "\n"
			replaceFile.write(line)
			total = total +1
                        if total % 50000 == 0:
                                print str(total) + " triples processed"


