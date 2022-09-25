We are using simplified datasets in the HW1.
you can access the original data here:
COV19_US: https://raw.githubusercontent.com/midas-network/COVID-19/master/data/cases/united%20states%20of%20america/nytimes_covid19_data/20200831_us-states.csv
Network: http://konect.cc/files/download.tsv.flixster.tar.bz2
Cascades/Action log: https://sites.google.com/view/mohsenjamali/flixter-data-set





COV19_GA.csv:
This is the tracking data of cases and death of COVID-19 in Georgia from July to November 2021.
The meaning of the columns:
cases: cases of COVID-19 in GA, in fraction.
deaths:deaths of COVID-19 in GA, in fraction.

example.txt:
This is one example graph-edge-list for Question 1.7, which is a clique of size 100. You can use this file as an example of the graph-edge-list, but you can also generate your own graph-edge-list. (We will not test results on this example network)

network.txt: 
This is the social network of Flixster, a movie rating site on which people can meet others with a similar movie taste.  
The network is directed and unweighted.
The meaning of the columns in network.txt are: 
First column: ID of from node 
Second column: ID of to node


Ratings.timed:
Records of rating of movies from users in Flixster.
The meaning of the columns in network.txt are: 
userid: ID of users, which is consistent with the ID in network.txt
moviedid: ID of movies,
rating: users' rating about movie,
date: the rating date.
