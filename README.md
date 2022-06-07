# qhack2022
Python scripts based on Pennylane for the QHack 2022 coding challenges.

Up to this date, this repository contains the challenges I solved during the QHack2022 itself. With time, I plan to add some more to the list.

The challenges are organized in three groups:

Pennylane 101. These challenges implement basic Quantum Computing concepts with Pennylane.

1. Order matters. Implements two circuits and compares the difference in the outcomes. Both circuits apply the same gates but in opposite order.
2. Know your device. Implements effectively the same circuit in two different devices.
3. Superdense coding. Implements the superdense coding, a communication protocol between two parties.
4. Finite-difference Gradient. Computes the gradient of the cost function of a variational quantum circuit.
5. Bit-flip error code. Error-correcting code that detects bit flips.

Algorithms. These challenges implement quantum algorithms that provide advantage over classical counterparts.
1. Deutsch-Jozsa algorithm. Solves the Deutsch-Jozsa problem with exponential advantage with respect to classical solutions.
2. Adapting to the topology. Given a circuit topology and a CNOT gate, computes the required number of SWAP gates to apply it.
3. QFT adder. Adds natural numbers using the Quantum Fourier Transform.
4. Quantum Counting. Returns the error in the quantum counting estimation (of elements that satisfy f(x) = 1). Variation of Groover's search.

Games. These challenges explore aspects of quantum mechanics by implementing/simulating games and other weird quantum experiments.
1. Tardigrade masquerade. Computes the Renyi entropy a single qubit in a two-qubit system, one of them entangled with an outside tardigrade.
2. The CHSH game. An example of a quantum strategy that increases the probability of winning over any possible classical protocol.
3. Elitzur-Vaidman Bomb. Quantum circuit that checks whether a bomb is live or a dud without necessarily triggering it.
4. Find the car. Finds behind which door there is a car with probability 1 by asking only one question with an oracle.
5. Switches. Determines which of 3 switches work by invoquing an oracle only once.

Quantum Machine Learning. These challenges explore the training of quantum variational circuits and quantum neural networks.
1. Generating Fourier basis. Creates the Quantum Fourier Transform operator from scratch by training a variational circuit.
2. Who likes the Beatles? Computes the distance of the data between two different people.

Quantum Chemistry. These challenges explore concepts of Quantum Chemistry, one of the lead application areas of Quantum Computing.
1. Particle conservation. Checks whether a quantum circuit preserves the number of particles.
2. Optimizing measurements. Given a quantum circuit, it compresses it, thus minimizing the number of measurements to be performed.
