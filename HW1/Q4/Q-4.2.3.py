#!/home/shrey/miniconda3/envs/cse8803e/bin/python

'''
SCRIPT: Q-4.2.3.py
DESCRIPTION: Script for solving the Lotka-Volterra Model 2
AUTHOR: Shreyash Gupta
USAGE: python Q-4.2.3.py -p <a> <b> <p> <g> <d> <r> <e> -i <x0> <y0> <z0> -t <time-steps>
'''


# Imports
from argparse import ArgumentParser
from numpy import linspace
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import pandas as pd

def LVM2ode(t, x, y, z, a, b, p, g, d, r, e):
    """
    Function for computing odes for solve_ivp function
    """
    dx = a*x - b*x*y - p*x*z
    dy = g*x*y - d*y
    dz = r*x*z - e*z
    return dx, dy, dz

def LVM2solver(a, b, p, g, d, r, e, x0, y0, z0, T):
    """
    Function for solving the LVM ODEs
    """
    # Solver
    t = linspace(0, T, 1001)
    result = solve_ivp(fun=lambda t, y: LVM2ode(t, y[0], y[1], y[2], a, b, p, g, d, r, e), t_span=[min(t), max(t)], y0=[x0, y0, z0], t_eval=t)
    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(result.t, result.y[0], label='x', linewidth=2)
    ax.plot(result.t, result.y[1], label='y', linewidth=2)
    ax.plot(result.t, result.y[2], label='z', linewidth=2)
    ax.set_title('Lotka-Volterra Model 2 with a = {}, b = {}, p = {}, g = {}, d = {}, r = {}, e = {}, x0 = {}, y0 = {}, z0 = {}'.format(a, b, p, g, d, r, e, x0, y0, z0))
    ax.set_xlabel('Time')
    ax.set_ylabel('Population')
    ax.legend()
    plt.savefig(f"Q-4.2.3-Lotka-Volterra-Model2-a_{a}_b_{b}_p_{p}_g_{g}_d_{d}_r_{r}_e_{e}_x0_{x0}_y0_{y0}_z0_{z0}.png")
    return result

def main():
        
    # Argument Parser
    parser = ArgumentParser()
    parser.add_argument('--parameter','-p', type=float, help='Parameters', nargs=7)
    parser.add_argument('--inits','-i', type=float, help='Initial Conditions', nargs=3)
    parser.add_argument('--time','-t', type=float, help='Time')
    args = parser.parse_args()
    a, b, p, g, d, r, e = args.parameter
    x0, y0, z0 = args.inits
    T = args.time

    # Inputs
    # a, b, p, g, d, r, e = 1, 1, 1, 1, 1, 1, 1
    # x0, y0, z0 = 5, 2, 3
    # T = 100

    res = LVM2solver(a, b, p, g, d, r, e, x0, y0, z0, T)
    print(res)

if __name__ == '__main__':
    main()