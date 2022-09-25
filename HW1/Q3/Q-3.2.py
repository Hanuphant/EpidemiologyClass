#!/home/shrey/miniconda3/envs/cse8803e/bin/python

'''
SCRIPT: Q-3.2.py
DESCRIPTION: Script for calibration of IC Model
AUTHOR: Shreyash Gupta
USAGE: python Q-3.2.py --ratings Ratings.timed.csv --network network.txt
'''

from argparse import ArgumentParser
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def find_probability(v, u, ratings, A):
    # find the probability of v being infected by u
    # v and u are indices of the nodes
    # return a float
    
    if A[v-1,u-1] == 0:
        return 0
    elif len(ratings[ratings['userid'] == v]) == 0:
        return 0
    else:
        # merge the two dataframes such that v action  = u action and v time < u time
        df = pd.merge(ratings[ratings['userid'] == v], ratings[ratings['userid'] == u], on = 'movieid', how = 'inner')
        df = df[df['date_x'] < df['date_y']]
        # calculate the probability
        return len(df)/len(ratings[ratings['userid'] == v]) # A_vu/A_v

def main():
    
    # Argument Parser
    parser = ArgumentParser()
    parser.add_argument('--ratings', type=str, help='Path to ratings.csv')
    parser.add_argument('--network', type=str, help='Path to network file')
    args = parser.parse_args()
    networkfile = args.network
    ratingsfile = args.ratings

    # Inputs
    # networkfile = "Assignments/HW1/Q3/network.txt"
    # ratingsfile = "Assignments/HW1/Q3/Ratings.timed.csv"

    # Loading Network file
    edges = []
    with open(networkfile) as f:
        for line in f:
            edges.append([int(u) for u in line.split()])

    # Creating Adjacency Matrix
    n = max(max(u) for u in edges)
    A = np.zeros((n, n))
    for u, v in edges:
        A[u-1, v-1] = 1

    # Loading Ratings file
    ratings = pd.read_csv(ratingsfile)

    # Probabilities of the edges
    output = [[u, v, find_probability(v, u, ratings, A)] for u, v in edges]

    # Saving the output
    with open('Q-3.2-Output_file.txt', 'w') as f:
        for u, v, probability in output:
            f.write(f'{u} {v} {probability}\n')
    
    # Storing the probabilities in adjacency matrix
    P = np.zeros((n, n))
    for u, v in edges:
        P[u-1, v-1] = find_probability(u,v,ratings,A)

    # Finding node degrees
    degrees = np.sum(P, axis=1)

    # Plotting the histogram
    plt.hist(degrees, bins=100)
    plt.savefig(f"Q-3.2-Weighted_out_degree_distribution.png")
    plt.hist(degrees, bins=100, log=True)
    plt.savefig(f"Q-3.2-Weighted_out_degree_distribution_log.png")


if __name__=="__main__":
    main()

