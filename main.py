from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def oracle() -> QuantumCircuit:
    # Create a QuantumCircuit implementing an oracle function
    # for Grover's Algorithm

    # The quantum circuit will have 3 qubits
    qc = QuantumCircuit(3)

    qc.x(2)
    qc.ccz(0, 1, 2)
    qc.x(2)

    return qc


def grover_operation(oracle: QuantumCircuit):
    # Create a QuantumCircuit implementing Grover's Operation
    # for a 3-qubit system

    qc = QuantumCircuit(3)
    qc.compose(oracle, inplace=True)
    qc.h(range(3))

    # Implement Z_OR using controlled-Z gates
    qc.x(range(3))
    qc.ccz(0,1,2)
    qc.x(range(3))

    qc.h(range(3))

    return qc
    
def grover_algorithm():
    qc = QuantumCircuit(3, 3)

    qc.h(range(3))
    for _ in range(2):
        qc.compose(grover_operation(oracle()),inplace=True)
    qc.measure(range(3), range(3))

    result = AerSimulator().run(qc, shots=100, memory=True).result()
    measurements = result.get_memory()
    return measurements

results = grover_algorithm()

plt.hist(results)
plt.xlabel("Measurement Outcomes")
plt.ylabel("Frequency")
plt.title("Measurements for 100 iterations of 3-Qubit Grover's Algorthm ")
plt.show()

