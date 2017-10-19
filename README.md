# propertyPathBenchmark
Property path benchmark created during Adrian Skubella's bachelor thesis

This benchmark evaluates the support of SPARQL 1.1 property paths.

To run it just copy all folders and files to any directory you like.


The benchmark can be executed in several steps.

1. Dataset preprocessing
	-Turning quads to triples
	-Replacing blank nodes with unique uri
	Use the dataPreprocessor.py in pythonScripts for this task.
	Execute python dataPreprocessor.py path/to/your/dataset
	It returns the preprocessed file in the same folder.

2. Create queries from Template
	-Create benchmark queries with grounding queries and templates
	Execute the queries in grounding queries and add the respective results to 
	the queries in the query templates

3. Execute benchmark
	-Execute the resulting benchmark queries
	Execute the executeBenchmark.sh in benchmarkExecuter
	Returns query results and average execution time for each query	


4. Create reference result Set
	-Creates a reference result set 


5. Result Comperator
	-Returns Soundness and Completeness of results
	Execute queryComparator.py path/to/result path/to/reference in pythonScripts
	Returns a tuple of completeness and soundness
