from qiskit import QuantumRegister, QuantumCircuit

from utils.typing_ import Name, QRegsSpec


def create_circuit(regs: QRegsSpec, name: Name) -> QuantumCircuit:
    qregs = [QuantumRegister(size, name=name) for (name, size) in regs]
    return QuantumCircuit(*qregs, name=name)