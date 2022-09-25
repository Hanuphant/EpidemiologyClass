#!/home/shrey/miniconda3/envs/cse8803e/bin/python

'''
SCRIPT: Q-1.3.1.py
DESCRIPTION: Script for SIR ODE model
AUTHOR: Shreyash Gupta
USAGE: python Q-1.3.1.py --beta <beta> --delta <delta> --maxTime <time> --s0 <S0> --i0 <I0> --r0 <R0>
'''

from argparse import ArgumentParser
from numpy import linspace
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def plotter(result, b, d, s0, i0, r0):
    """
    Function for plotting the results from the solve_ivp function
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(result.t, result.y[0], label='S', linewidth=2)
    ax.plot(result.t, result.y[1], label='I', linewidth=2)
    ax.plot(result.t, result.y[2], label='R', linewidth=2)
    ax.set_title('SIR Model with beta = {}, delta = {}, s0 = {}, i0 = {}, r0 = {}'.format(b, d, s0, i0, r0))
    ax.set_xlabel('Time')
    ax.set_ylabel('Population')
    # legend = plt.legend(loc='upper right', shadow=True, title = 'Population')
    ax.legend()
    plt.show()
    plt.savefig('Assignments/HW1/SIR_Model_b{}d_{}s_{}i_{}r_{}.png'.format(b, d, s0, i0, r0))


def sirODE(t, b, d, s, i, r):
    """
    Function for computing odes for solve_ivp function
    """
    ds = -b*s*i
    di = b*s*i - d*i
    dr = d*i
    return ds, di, dr

def main():
    # Argument Parser
    parser = ArgumentParser()
    parser.add_argument('--beta', '-b', type=float, default=0.5)
    parser.add_argument('--delta', '-d',  type=float, default=0.1)
    parser.add_argument('--maxTime', '-t', type=float, default=0.1)
    parser.add_argument('--s0', '-s', type=int, default=100)
    parser.add_argument('--i0', '-i', type=int, default=1)
    parser.add_argument('--r0', '-r',type=int, default=0)
    args = parser.parse_args()

    beta = args.beta
    delta = args.delta
    maxTime = args.maxTime
    s0 = args.s0
    i0 = args.i0
    r0 = args.r0

    # Default parameters
    # beta = 0.05
    # delta = 0.1
    # maxTime = 200
    # s0 = 0.95
    # i0 = 0.05
    # r0 = 0
    t = linspace(0, maxTime, 1001)

    result = solve_ivp(fun=lambda t, y: sirODE(t, beta, delta, y[0], y[1], y[2]), t_span=[min(t), max(t)], y0=[s0, i0, r0], t_eval=t)
    plotter(result, beta, delta, s0, i0, r0)
    print(result)

if __name__ == "__main__":
    main()