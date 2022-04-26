#! /usr/bin/python3

import sys
import pennylane as qml
from pennylane import numpy as np


def compare_circuits(angles):
    """Given two angles, compare two circuit outputs that have their order of operations flipped: RX then RY VERSUS RY then RX.

    Args:
        - angles (np.ndarray): Two angles

    Returns:
        - (float): | < \sigma^x >_1 - < \sigma^x >_2 |
    """

    # QHACK #

    # define a device and quantum functions/circuits here

    x, y = angles

    dev = qml.device('default.qubit', wires=2, shots=None)

    @qml.qnode(dev)
    def qfunction_1(x,y):
        qml.RX(x,wires=0)
        qml.RY(y,wires=0)
        return qml.expval(qml.PauliX(0))

    @qml.qnode(dev)
    def qfunction_2(x,y):
        qml.RY(y,wires=1)
        qml.RX(x,wires=1)
        return qml.expval(qml.PauliX(1))

    return abs(qfunction_1(x,y) - qfunction_2(x,y))
    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    angles = np.array(sys.stdin.read().split(","), dtype=float)
    output = compare_circuits(angles)
    print(f"{output:.6f}")
