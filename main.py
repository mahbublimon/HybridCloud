from classical.ai_processor import process_data
from quantum.qaoa_optimizer import run_qaoa
from quantum.kyber_crypto import run_kyber
from quantum.grover_search import run_grover
from quantum.shor_attack_test import run_shor_attack
from classical.hybrid_executor import hybrid_integration

if __name__ == "__main__":
    print("Starting Hybrid Quantum-Classical Execution...")

    process_data()
    run_kyber()
    run_qaoa()
    run_grover()
    hybrid_integration()
    run_shor_attack()

    print("Execution completed. Check output in result_output/")
