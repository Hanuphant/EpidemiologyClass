#!/home/shrey/miniconda3/envs/cse8803e/bin/python

'''
SCRIPT: Q-4.2.1.py
DESCRIPTION: Script for solving the Lotka-Volterra Model
AUTHOR: Shreyash Gupta
USAGE: python Q-4.2.1.py --parameter 1 1 1 1 --inits 5 2 --time 100
'''

# Imports
from argparse import ArgumentParser
from numpy import linspace
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import pandas as pd

# LVM ODEs
def LVMode(t, x, y, a, b, c, d):
    """
    Function for computing odes for solve_ivp function
    """
    dx = a*x - b*x*y
    dy = c*x*y - d*y
    return dx, dy

def LVMsolver(a, b, c, d, x0, y0, T):
    """
    Function for solving the LVM ODEs
    """
    # Solver
    t = linspace(0, T, 1001)
    result = solve_ivp(fun=lambda t, y: LVMode(t, y[0], y[1], a, b, c, d), t_span=[min(t), max(t)], y0=[x0, y0], t_eval=t)
    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(result.t, result.y[0], label='x', linewidth=2)
    ax.plot(result.t, result.y[1], label='y', linewidth=2)
    ax.set_title('Lotka-Volterra Model with a = {}, b = {}, c = {}, d = {}, x0 = {}, y0 = {}'.format(a, b, c, d, x0, y0))
    ax.set_xlabel('Time')
    ax.set_ylabel('Population')
    ax.legend()
    plt.savefig(f"Q-4.2.1-Lotka-Volterra-Model-a_{a}_b_{b}_c_{c}_d_{d}_x0_{x0}_y0_{y0}.png")
    df = pd.DataFrame({'t': result.t, 'x': result.y[0], 'y': result.y[1]})
    # df['x'] = df['x']/(df['x'] + df['y'])
    # df['y'] = df['y']/(df['x'] + df['y'])
    return df

def main():
    
    # Argument Parser
    parser = ArgumentParser()
    parser.add_argument('--parameter','-p', type=float, help='Parameters', nargs=4)
    parser.add_argument('--inits','-i', type=float, help='Initial Conditions', nargs=2)
    parser.add_argument('--time','-t', type=float, help='Time')
    args = parser.parse_args()
    a, b, c, d = args.parameter
    x0, y0 = args.inits
    T = args.time

    # Inputs
    # a, b, c, d = 1, 1, 1, 1
    # x0, y0 = 5, 2
    # T = 100

    dat = LVMsolver(a, b, c, d, x0, y0, T)
    print(dat)

if __name__ == "__main__":
    main()