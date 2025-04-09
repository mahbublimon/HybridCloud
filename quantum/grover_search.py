from qiskit import QuantumCircuit, Aer, transpile
from qiskit.algorithms import Grover
from qiskit.circuit.library import ZGate
from qiskit.utils import QuantumInstance

def run_grover():
    print("[Grover] Running Grover’s Algorithm...")
    oracle = QuantumCircuit(2)
    oracle.cz(0, 1)
    instance = QuantumInstance(Aer.get_backend('aer_simulator'))
    grover = Grover(oracle=oracle)
    result = grover.run(instance)
    print("[Grover] Result state vector:", result)
