#! /usr/bin/python3

import sys
import pennylane as qml
from pennylane import numpy as np

dev = qml.device("default.qubit", wires=1, shots=1)


@qml.qnode(dev)
def is_bomb(angle):
    """Construct a circuit at implements a one shot measurement at the bomb.

    Args:
        - angle (float): transmissivity of the Beam splitter, corresponding
        to a rotation around the Y axis.

    Returns:
        - (np.ndarray): a length-1 array representing result of the one-shot measurement
    """

    # QHACK #
    qml.PauliX(0)
    qml.RY(2*angle,wires=0)
    # QHACK #

    return qml.sample(qml.PauliZ(0))


@qml.qnode(dev)
def bomb_tester(angle):
    """Construct a circuit that implements a final one-shot measurement, given that the bomb does not explode

    Args:
        - angle (float): transmissivity of the Beam splitter right before the final detectors

    Returns:
        - (np.ndarray): a length-1 array representing result of the one-shot measurement
    """

    # QHACK #
    qml.PauliX(0)
    qml.RY(2*angle,wires=0)
    qml.PauliX(0)
    # QHACK #

    return qml.sample(qml.PauliZ(0))


def simulate(angle, n):
    """Concatenate n bomb circuits and a final measurement, and return the results of 10000 one-shot measurements

    Args:
        - angle (float): transmissivity of all the beam splitters, taken to be identical.
        - n (int): number of bomb circuits concatenated

    Returns:
        - (float): number of bombs successfully tested / number of bombs that didn't explode.
    """

    # QHACK #

    num_exp = 0
    num_notexp = 0
    num_c = 0
    num_d = 0

    for cycle in range(10000):

        bomb = 0

        qml.BasisState(1,wires=0)

        for i in range(n):
            test = is_bomb(angle)
            if test == 0:
                bomb = 1

        if bomb == 1:
            num_exp += 1
        else:
            num_notexp += 1

        test_final = bomb_tester(angle)
        if test_final == 1:
            num_c +=1
        else:
            num_d +=1

    return num_d/num_notexp
    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    output = simulate(float(inputs[0]), int(inputs[1]))
    print(f"{output}")
