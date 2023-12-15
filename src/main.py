'''The Main file is intendet to be run ones.
It runs the self checks as well as the sorting and order of particapents
usage:
./main.py [options]'''

import json
import math

from test import *

from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit_ibm_provider import IBMProvider


def create_order(lst, participants):
    '''This method is intendet to append the participants to a given list.'''
    if participants not in lst:
        lst.append(participants)
        return lst

class Participants:
    '''A Participant is an entity that participate at the secret santa event.
    All Participants need a name and an id, while the reciver is left blank at first.
    '''
    def __init__(self, id, name, receiver):
        self.id = id
        self.name = name
        self.receiver = receiver  # person_id to receive

config_file = open('config.json')
config_data = json.load(config_file)

if config_data['Provider_Key'] != '':
    provider_token = config_data['Provider_Key']
else:
    raise ValueError('No provider_token')

provider = IBMProvider(token=provider_token)

num_participants = len(config_data['Participants'])
num_qbits = math.ceil(math.log2(num_participants**2))

qc = QuantumCircuit(num_qbits, num_qbits)
for i in range(num_qbits):
    qc.h(i)

qc.measure(list(range(num_qbits)), list(range(num_qbits)))

#TODO: Add CLI cmd to change this - simulator == -t / --test
backend = provider.get_backend('ibmq_qasm_simulator')
#TODO: Add CLI cmd to change this - also to split it up, to make retries less costly.
shots = 512

transpiled_circuit = transpile(qc, backend)

# Run the circuit and get result
print(f'start job on: {backend}')
job = backend.run(transpiled_circuit, shots=shots, memory=True)
result = job.result()
memory = result.get_memory()
print(f'job finished on {backend}')

part_list = []
for i in config_data['Participants']:
    part_list.append(Participants(i, i['name'], None))

outputArray = []
# convert the result to decimal
for x in range(0, shots):
    converted = int(memory[x], 2)
    outputArray.append(converted%len(part_list))

order = []
i = 0
while len(order) < len(part_list):
    create_order(order, outputArray[0])
    outputArray.pop(0)
    i +=1

orderd_list = [part_list[i] for i in order]

# Calculation:
for i in range(len(part_list)):
    j = outputArray[0]
    print(test_other_num_still_pressent(orderd_list[i].id, part_list, outputArray))
    if test_other_num_still_pressent(orderd_list[i].id, part_list, outputArray):
        while outputArray[j] == orderd_list[i].id:
            j +=1
            j = j%len(outputArray)
        temp = outputArray[j]
        orderd_list[i].receiver = part_list[temp]
        print(f'{orderd_list[i].name}| {orderd_list[i].id} sends something to: {orderd_list[i].receiver.name} | {outputArray[j]}')
        outputArray = list(filter((temp).__ne__, outputArray))
    else:
        raise Exception('We encounted an issue during generation, restart script. - may the randomness be with you')

# Tests:
print(f'all Participants have some one: {test_all_give_someone(part_list)}')

print(f'no self loops: {test_no_self_loops(part_list)}')

print(f'no second order loops: {test_no_second_order_loops(part_list)}')

# Output:
print('the result is:')
for p in part_list:
    print(f'{p.name.ljust(15)}, {p.receiver.name}')
