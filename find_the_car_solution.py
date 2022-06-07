#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml


dev = qml.device("default.qubit", wires=[0, 1, "sol"], shots=1)


def find_the_car(oracle):
    """Function which, given an oracle, returns which door that the car is behind.

    Args:
        - oracle (function): function that will act as an oracle. The first two qubits (0,1)
        will refer to the door and the third ("sol") to the answer.

    Returns:
        - (int): 0, 1, 2, or 3. The door that the car is behind.
    """

    @qml.qnode(dev)
    def circuit1():
        # QHACK #
        qml.BasisState(np.array([0,0,0]),wires=[0,1,"sol"])
        qml.Hadamard(wires=0)
        qml.CNOT(wires=[0,1])
        qml.PauliX("sol")
        qml.Hadamard(wires="sol")
        oracle()
        qml.CNOT(wires=[0,1])
        qml.Hadamard(wires=0)
        # QHACK #
        return qml.sample()

    @qml.qnode(dev)
    def circuit2(num):
        # QHACK #
        if num==0:
            qml.BasisState(np.array([0,0,0]),wires=[0,1,"sol"])
        else:
            qml.BasisState(np.array([0,1,0]),wires=[0,1,"sol"])
        qml.Hadamard(wires=0)
        qml.CNOT(wires=[0,1])
        oracle()

        # QHACK #
        return qml.sample()

    sol1 = circuit1()
    if sol1[0]+sol1[1] == 1:
        sol2 = circuit2(0)
        if sol2[2] == 1 and sol2[1]==0:
            return 0
        elif sol2[2] == 1 and sol2[1]==1:
            return 3
        elif sol2[2] == 0 and sol2[1]==0:
            return 3
        elif sol2[2] == 0 and sol2[1]==1:
            return 0
    else:
        sol2 = circuit2(1)
        if sol2[2] == 1 and sol2[1]==0:
            return 2
        elif sol2[2] == 1 and sol2[1]==1:
            return 1
        elif sol2[2] == 0 and sol2[1]==0:
            return 1
        elif sol2[2] == 0 and sol2[1]==1:
            return 2

    # QHACK #

    # process sol1 and sol2 to determine which door the car is behind.
    print(sol1)
    print(sol2)

    if sol1[2] == 1:
        if sol1[0] == 0 and sol1[1] == 0:
            return 0
        if sol1[0] == 1 and sol1[1] == 1:
            return 3
    elif sol1[0] == 0 and sol1[1] == 1:
        return 3
    elif sol1[0] == 1 and sol1[1] == 0:
        return 0

    if sol2[2] == 1:
        if sol2[0] == 0 and sol2[1] == 1:
            return 1
        if sol2[0] == 1 and sol2[1] == 0:
            return 2
    elif sol2[0] == 0 and sol2[1] == 0:
        return 2
    elif sol2[0] == 1 and sol2[1] == 1:
        return 1

    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    numbers = [int(i) for i in inputs]

    def oracle():
        if numbers[0] == 1:
            qml.PauliX(wires=0)
        if numbers[1] == 1:
            qml.PauliX(wires=1)
        qml.Toffoli(wires=[0, 1, "sol"])
        if numbers[0] == 1:
            qml.PauliX(wires=0)
        if numbers[1] == 1:
            qml.PauliX(wires=1)

    output = find_the_car(oracle)
    print(f"{output}")
