from qiskit.algorithms import QAOA
from qiskit.opflow import PauliSumOp
from qiskit.algorithms.optimizers import COBYLA
from qiskit import Aer
import json

def run_qaoa():
    print("[QAOA] Running Quantum Optimization...")
    hamiltonian = PauliSumOp.from_list([("ZZ", 1.0), ("XX", 0.5)])
    qaoa = QAOA(optimizer=COBYLA(), reps=2)
    backend = Aer.get_backend('aer_simulator')
    result = qaoa.compute_minimum_eigenvalue(hamiltonian, backend=backend)
    with open("result_output/optimization_result.json", "w") as f:
        json.dump({"optimal_value": str(result.optimal_value)}, f)
    print("[QAOA] Optimization complete.")
