# molecule-complete-solution
Now completed version of the suggested solution to find the ground state of a molecule using quantum computing. We created a variational quantum eigensolver (VQE) that finds the ground state energy of the hydrogen (H2) molecule on IBM's quantum  computer.  We use Jordan-Wigner mapping to map the fermionic operators to Pauli matrices. Noise mitigation is also applied to give a better solution. 

![](https://github.com/WaywardPhoton/QSciTech-QuantumBC-Workshop-Team4-Solution/blob/main/summary.png)

Description of the files :
- hamiltonian.py : This files defines the FermionicHamiltonian class and subclasses. You should be able to partially complete it after activity 2.2 and 2.3. The 'to_linear_combinaison_pauli_string' methods can be completed after activity 3.1.
- pauli_string.py : Defines PauliString and LinearCombinaisonPauliString class. You should be able to complete it after activity 3.1. The 'to_matrix' method is optional.
- mapping.py : Defines the JordanWigner mapping. You should be able to complete it after activity 3.1.
- evaluator.py : Defines the abstract class Evaluator and the BasicEvaluator class. You should be able to complete it after activity 3.2.
- solve.py : Defines VQESolver and ExactSolver. You should be able to complete it after activity 3.2. The ExactSolver is optionnal.


Other files :
- Integrals_sto-3g_H2_d_0.7350_no_spin.npz : Contains the one body and two body integrals (no spin) for a H2 molecule with d=0.735. The two body is given in the physicist order.
- activity3-1.ipynb and activity3-2.ipynb : Tutorial Jupyter notebooks to help code the concepts seen in the respective activities.


