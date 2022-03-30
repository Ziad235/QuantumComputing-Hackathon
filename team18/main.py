from qiskit import QuantumCircuit, transpile
from qiskit.test.mock import FakeAthens
from mqt import qcec

if __name__ == "__main__":
    # create your quantum circuit
    circ = QuantumCircuit(3)
    circ.h(0)
    circ.cx(0, 1)
    circ.cx(0, 2)
    circ.measure_all()
    print(circ.draw(fold=-1))

    # compile circuit to 5 qubit London Architecture
    circ_comp = transpile(circ, backend=FakeAthens())
    print(circ_comp.draw(fold=-1))

    # initialize the equivalence checker
    ecm = qcec.EquivalenceCheckingManager(circ, circ_comp, )

    # set the application scheme to be based off a profile
    ecm.set_application_scheme('gate_cost')
    ecm.set_gate_cost_profile('dummy.profile')

    # execute the check
    ecm.run()

    # obtain the result
    print(ecm.equivalence())

    # obtain runtime
    results = ecm.get_results()
    print('Took:', results.check_time, '[s]')
