from qiskit.algorithms import Shor
from qiskit import Aer

def run_shor_attack():
    print("[Shor] Testing quantum security using Shor’s algorithm...")
    shor = Shor()
    backend = Aer.get_backend('qasm_simulator')
    result = shor.factor(15, backend)
    print("[Shor] Factors of 15 found:", result.factors)
