#Execute queries 5 times to warm up store
for i in 1 2 3 4 5; 
do
	for j in 1 2 3 4 5 6 7 8;
	do
		./executeQueries/query${j}.sh
	done
done


for i in 1 2 3 4 5 6 7 8 9 10;
do
	for j in 1 2 3 4 5 6 7 8;
	do 
		./executerQueries/query${j} > ./results/run${j}/result${i}
	done
done
