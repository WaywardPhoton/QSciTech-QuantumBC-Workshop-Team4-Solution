"""
mapping.py - Map a Hamiltonian to a LinearCombinaisonPauliString

Copyright 2020-2021 Maxime Dion <maxime.dion@usherbrooke.ca>
This file has been modified by <Your,Name> during the
QSciTech-QuantumBC virtual workshop on gate-based quantum computing.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from pauli_string import PauliString, LinearCombinaisonPauliString
import numpy as np


class Mapping(object):

    def fermionic_hamiltonian_to_linear_combinaison_pauli_string(self, fermionic_hamiltonian):
        """
        Do the mapping of a FermionicHamiltonian. First generates the LCPS representation of the creation/annihilation
        operators for the specific mapping. Uses the 'to_pauli_string_linear_combinaison' of the FermionicHamiltonian
        to generate the complete LCPS.

        Args:
            fermionic_hamiltonian (FermionicHamiltonian): A FermionicHamiltonian that provided a 
                'to_pauli_string_linear_combinaison' method.

        Returns:
            LinearCombinaisonPauliString: The LCPS reprenseting the FermionicHamiltonian
        """

        aps, ams = self.fermionic_operator_linear_combinaison_pauli_string(fermionic_hamiltonian.number_of_orbitals())
        #pslc = fermionic_hamiltonian.to_pauli_string_linear_combinaison(aps, ams)
        pslc = fermionic_hamiltonian.to_linear_combinaison_pauli_string(aps, ams)
        return pslc


class JordanWigner(Mapping):
    def __init__(self):
        """
        The Jordan-Wigner mapping
        """

        self.name = 'jordan-wigner'

    def fermionic_operator_linear_combinaison_pauli_string(self, n_qubits):
        """
        Build the LCPS reprensetations for the creation/annihilation operator for each qubit following 
        Jordan-Wigner mapping.

        Args:
            n_qubits (int): The number of orbitals to be mapped to the same number of qubits.

        Returns:
            list<LinearCombinaisonPauliString>, list<LinearCombinaisonPauliString>: Lists of the creation/annihilation
                operators for each orbital in the form of LinearCombinaisonPauliString.
        """

        aps = list()
        ams = list()
        
        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after activity 3.1)
        # This is a large piece of the puzzle
        
        
        coefs_creation = np.array([0.5,-0.5j],dtype = complex)
        coefs_annihilation = np.array([0.5,0.5j],dtype = complex)
        for i in range(0,n_qubits):
            paulis1 = ['I'] * n_qubits
            paulis2 = ['I'] * n_qubits
            paulis1[n_qubits-i-1] = 'X'
            paulis2[n_qubits-i-1] = 'Y'
            if i > 0:
                for j in range(0,i):
                    paulis1[n_qubits-j-1] = paulis2[n_qubits-j-1] = 'Z'            
            pauli_string_1 = PauliString.from_str(paulis1)
            pauli_string_2 = PauliString.from_str(paulis2)
            pauli_strings = ([pauli_string_1,pauli_string_2])
            aps.append(LinearCombinaisonPauliString(coefs_creation,pauli_strings))
            ams.append(LinearCombinaisonPauliString(coefs_annihilation,pauli_strings))         

        
        ################################################################################################################

        #raise NotImplementedError()

        return aps, ams


class Parity(Mapping):
    def __init__(self):
        """
        The Parity mapping
        """

        self.name = 'parity'

    def fermionic_operator_linear_combinaison_pauli_string(self, n_qubits):
        """
        Build the LCPS reprensetations for the creation/annihilation operator for each qubit following 
        Parity mapping.

        Args:
            n_qubits (int): The number of orbtials to be mapped to the same number of qubits.

        Returns:
            list<LinearCombinaisonPauliString>, list<LinearCombinaisonPauliString>: Lists of the creation/annihilation
                operators for each orbital in the form of LinearCombinaisonPauliString
        """

        aps = list()
        ams = list()
        
        ################################################################################################################
        # YOUR CODE HERE
        # OPTIONAL
        coefs_creation = np.array([0.5,-0.5j],dtype = complex)
        coefs_annihilation = np.array([0.5,0.5j],dtype = complex)
        for i in reversed(range(0,n_qubits)):
            paulis1 = ['I'] * n_qubits
            paulis2 = ['I'] * n_qubits
            #if i == 0:
            paulis1[i] = 'X'
            paulis2[i] = 'Y'
            if i < (n_qubits-1):
                paulis1[i+1] = 'Z'
            if i != 0:               
                paulis1[0:i] = ['X']*i
                paulis2[0:i] = ['X']*i
            
            pauli_string_1 = PauliString.from_str(paulis1)
            pauli_string_2 = PauliString.from_str(paulis2)
            pauli_strings = np.array([pauli_string_1,pauli_string_2],dtype = PauliString)
            aps.append(LinearCombinaisonPauliString(coefs_creation,pauli_strings))
            ams.append(LinearCombinaisonPauliString(coefs_annihilation,pauli_strings))  
            
        ################################################################################################################

        #raise NotImplementedError()

        return aps, ams
