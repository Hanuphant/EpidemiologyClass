#!/home/shrey/miniconda3/envs/cse8803e/bin/python

'''
SCRIPT: Q-1.3.2.py
DESCRIPTION: SIR model on a network
AUTHOR: Shreyash Gupta
USAGE: python Q-1.3.2.py -n <Number of cliques> -f <Edge list file> -p <beta> <delta> -i <S0> <I0> <R0> -t <Time Steps> -e <Iterations>
'''

# Imports 
import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import random
from argparse import ArgumentParser

# Parse the file 
def edgeExtract(file):
  edges = []
  with open(file, "r") as f:
    for line in f:
      line = line.strip()
      line = line.split(" ")
      edges.append((int(line[0]),int(line[2])))
  return edges

# Edge creator from the nodes 
def edgesFromNodes(N):
  edges = []
  for i in range(2, N+1):
    for j in range(1, i):
      edges.append((i, j))
  return edges

# Plotter function
def plotpdDataFrame(df):
  fig, ax = plt.subplots(figsize=(8,5))
  ax.plot(df['Time'], df['Susceptible'], linewidth=2)
  ax.plot(df['Time'], df['Infected'], linewidth=2)
  ax.plot(df['Time'], df['Recovered'], linewidth=2)
  ax.set_title(f'Plot of SIR in Network')
  ax.set_xlabel('Time')
  ax.set_ylabel('Population')
  ax.legend()
  plt.savefig('SIRNetworkPlot')

def main():
  parser = ArgumentParser()
  parser.add_argument("--N","-n", type=int, default=1000, help="Number of nodes")
  parser.add_argument("--file","-f", type=str, default=0.1, help="Edge-list file")
  parser.add_argument("--param","-p", type=float, default=[0.1, 0.05], help="Parameters", nargs=2)
  parser.add_argument("--inits","-i", type=float, default=[0.95, 0.05, 0.0], help="SIR initializations", nargs=3)
  parser.add_argument("--maxTime","-t", type=int, default=200, help="Number of time-steps")
  parser.add_argument("--iter","-e", type=int, default=50, help="Maximum Iterations")
  args = parser.parse_args()
  b, d = args.param
  s0, i0, r0 = args.inits
  N = args.N
  maxTime = args.maxTime
  maxIter = args.iter
  edgefile = args.file

  # Create the graph
  if edgefile:
    edges = edgeExtract(edgefile)
  else:
    edges = edgesFromNodes(N)
  G = nx.from_edgelist(edges)
  N = G.number_of_nodes()

  # Source = http://physics.bu.edu/~pankajm/PY571/Notes/Network-Simulations.html

  dfs = []
  for iter in tqdm(range(0,maxIter)):
    # print(f"Iteration: {iter}")
    data = pd.DataFrame({'Time':[], 'Susceptible':[], 'Infected':[], 'Recovered':[]})
    times = range(1, maxTime+1)
    # Nodes which are infected
    susceptible = []
    infected = []
    recovered = []
    # Nodes which recovered 
    t = 0
    tmax_running = 0
    generation = 0
    # Total pop set
    Npop = np.arange(1, N, 1)
    infected = random.sample(set(Npop), round(N*i0))
    if r0 == 0:
      susceptible = set(Npop) - set(infected)
      recovered = set()
    else:
      susceptible = random.sample(set(Npop) - set(infected), round(N*s0))
      recovered = set(Npop) - set(susceptible) - set(infected)
    # print(f'Initialization\nInfected:\t{len(infected)}\t{round(N*i0)}\nRecovered:\t{len(recovered)}\t{round(N*r0)}')

    for t in times:

      # At each time all the susceptible nodes sample a random neighbor 
      new_infected = set()
      for node in susceptible:
        neighbors = G.neighbors(node)
        # Sample a random neighbor
        sampledNeighbor = random.sample(set(neighbors),1)
        # Check if the neighbor is infected
        if len(set(sampledNeighbor).intersection(set(infected))):
          # Check if the node gets infected
          if random.random() < b:
            new_infected.add(node)
      susceptible = set(susceptible) - set(new_infected)
      infected = set(infected).union(set(new_infected))
      new_recovered = random.sample(infected, round(d*len(infected)))
      recovered = set(recovered).union(set(new_recovered))
      infected = set(infected) - set(new_recovered)
      data.loc[len(data.index)] = [t, len(susceptible)/N, len(infected)/N, len(recovered)/N]
    dfs.append(data)

  averages = pd.concat([each.stack() for each in dfs],axis=1)\
              .apply(lambda x:x.mean(),axis=1)\
              .unstack()
  plotpdDataFrame(averages)
  print(averages)


if __name__=="__main__":
    main()