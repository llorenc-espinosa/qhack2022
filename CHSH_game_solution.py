#! /usr/bin/python3

import sys
import pennylane as qml
from pennylane import numpy as np


dev = qml.device("default.mixed", wires=2)


def prepare_entangled(alpha, beta):
    """Construct a circuit that prepares the (not necessarily maximally) entangled state in terms of alpha and beta
    Do not forget to normalize.

    Args:
        - alpha (float): real coefficient of |00>
        - beta (float): real coefficient of |11>
    """

    # QHACK #
    norm = np.sqrt(alpha**2 + beta**2)
    state = np.array([alpha/norm, 0, 0, beta/norm])
    qml.QubitStateVector(state,wires=range(2))

    return
    # QHACK #

@qml.qnode(dev,diff_method="parameter-shift")
def chsh_circuit(theta_A0, theta_A1, theta_B0, theta_B1, x, y, alpha, beta):
    """Construct a circuit that implements Alice's and Bob's measurements in the rotated bases

    Args:
        - theta_A0 (float): angle that Alice chooses when she receives x=0
        - theta_A1 (float): angle that Alice chooses when she receives x=1
        - theta_B0 (float): angle that Bob chooses when he receives x=0
        - theta_B1 (float): angle that Bob chooses when he receives x=1
        - x (int): bit received by Alice
        - y (int): bit received by Bob
        - alpha (float): real coefficient of |00>
        - beta (float): real coefficient of |11>

    Returns:
        - (np.tensor): Probabilities of each basis state
    """

    prepare_entangled(alpha, beta)

    # QHACK #

    if x == 0:
        qml.RY(-2*theta_A0,wires=0)
    if x == 1:
        qml.RY(-2*theta_A1,wires=0)
    if y == 0:
        qml.RY(-2*theta_B0,wires=1)
    if y == 1:
        qml.RY(-2*theta_B1,wires=1)

    # QHACK #

    return qml.probs(wires=range(2))
    

def winning_prob(params, alpha, beta):
    """Define a function that returns the probability of Alice and Bob winning the game.

    Args:
        - params (list(float)): List containing [theta_A0,theta_A1,theta_B0,theta_B1]
        - alpha (float): real coefficient of |00>
        - beta (float): real coefficient of |11>

    Returns:
        - (float): Probability of winning the game
    """

    # QHACK #
    probs_00 = chsh_circuit(theta_A0=params[0],theta_A1=params[1],theta_B0=params[2],theta_B1=params[3],x=0,y=0,alpha=alpha,beta=beta)
    probs_01 = chsh_circuit(theta_A0=params[0],theta_A1=params[1],theta_B0=params[2],theta_B1=params[3],x=0,y=1,alpha=alpha,beta=beta)
    probs_10 = chsh_circuit(theta_A0=params[0],theta_A1=params[1],theta_B0=params[2],theta_B1=params[3],x=1,y=0,alpha=alpha,beta=beta)
    probs_11 = chsh_circuit(theta_A0=params[0],theta_A1=params[1],theta_B0=params[2],theta_B1=params[3],x=1,y=1,alpha=alpha,beta=beta)

    return 1/4*(probs_00[0]+probs_00[3])+1/4*(probs_01[0]+probs_01[3])+1/4*(probs_10[0]+probs_10[3])+1/4*(probs_11[1]+probs_11[2])

    # QHACK #
    

def optimize(alpha, beta):
    """Define a function that optimizes theta_A0, theta_A1, theta_B0, theta_B1 to maximize the probability of winning the game

    Args:
        - alpha (float): real coefficient of |00>
        - beta (float): real coefficient of |11>

    Returns:
        - (float): Probability of winning
    """

    def cost(params):
        """Define a cost function that only depends on params, given alpha and beta fixed"""

    # QHACK #

    #Initialize parameters, choose an optimization method and number of steps
    init_params = np.array([0,0,0,0],requires_grad=True)
    #opt = 
    steps = 300

    # QHACK #
    
    # set the initial parameter values
    params = init_params
    #print(winning_prob(params,alpha,beta))
    for i in range(steps):
        # update the circuit parameters 
        # QHACK #
        
        cost = (winning_prob(params,alpha,beta) - 1)**2
        grad = 2*(winning_prob(params,alpha,beta) - 1)*qml.grad(winning_prob)(params,alpha,beta)[:4]
        params = params - grad
        
        # QHACK #

    return winning_prob(params, alpha, beta)


if __name__ == '__main__':
    inputs = sys.stdin.read().split(",")
    output = optimize(float(inputs[0]), float(inputs[1]))
    print(f"{output}")