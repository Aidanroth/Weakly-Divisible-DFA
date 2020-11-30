from automata.fa.nfa import NFA
from automata.fa.dfa import DFA

'''
def generate_delta_table(DFA):
    delta_table = [[0 for i in range(10)] for j in range(len(DFA.states))]
    i = 0
    for state in range(len(DFA.transitions)):
        for input_symbol in DFA.input_symbols:
            delta_table[i][int(input_symbol)] = (DFA.transitions[state])
        i += 1
    return delta_table
'''


def generate_delta_table(DFA):
    delta_table = [[0 for i in range(10)] for j in range(len(DFA.states))]
    i = 0
    for state in DFA.transitions:
        for input_symbol in DFA.input_symbols:
            delta_table[i][int(input_symbol)] = (DFA.transitions[state][input_symbol])
        i += 1
    return delta_table


def state_to_int(dfa, output_state):
    # converts a state to an integer based on its location in dfa.states
    state_list = list(dfa.states)
    for i in range(len(state_list)):
        if output_state == state_list[i]:
            return i
    print("State not found")


def count(str_length, dfa, delta_table):
    curr_dict = {}
    next_dict = {}
    for state in dfa.states:
        curr_dict[state] = 0
        next_dict[state] = 0
    # below code block builds list of accepting states (does it make more sense to make this a dict?)
    final = [False for i in range(len(dfa.states))]
    i = 0
    for state in curr_dict:
        if state in dfa.final_states:
            final[i] = True
            curr_dict[state] = 1
        i += 1

    # below code block builds "current" array
    current = [0 for i in range(len(dfa.states))]
    for j in range(len(dfa.states)):
        if final[j]:
            current[j] = 1

    # build next array from current array
    next_array = [0 for i in range(len(dfa.states))]
    for i in range(str_length):
        k = 0
        for state in dfa.states:
            curr0 = curr_dict[dfa.transitions[state]['0']]
            curr1 = curr_dict[dfa.transitions[state]['1']]
            curr2 = curr_dict[dfa.transitions[state]['2']]
            curr3 = curr_dict[dfa.transitions[state]['3']]
            curr4 = curr_dict[dfa.transitions[state]['4']]
            curr5 = curr_dict[dfa.transitions[state]['5']]
            curr6 = curr_dict[dfa.transitions[state]['6']]
            curr7 = curr_dict[dfa.transitions[state]['7']]
            curr8 = curr_dict[dfa.transitions[state]['8']]
            curr9 = curr_dict[dfa.transitions[state]['9']]
            k += 1
            next_dict[state] = curr0 + curr1 + curr2 + curr3 + curr4 + curr5 + curr6 + curr7 + curr8 + curr9
            '''
        next_array[k] = current[state_to_int(dfa, delta_table[k][0])] + current[state_to_int(dfa, delta_table[k][1])] + current[state_to_int(dfa, delta_table[k][2])] + \
                            current[state_to_int(dfa, delta_table[k][3])] + current[state_to_int(dfa, delta_table[k][4])] + current[state_to_int(dfa, delta_table[k][5])] + \
                            current[state_to_int(dfa, delta_table[k][6])] + current[state_to_int(dfa, delta_table[k][7])] + current[state_to_int(dfa, delta_table[k][8])] + \
                            current[state_to_int(dfa, delta_table[k][9])]
        '''
        for state1 in dfa.states:
            curr_dict[state1] = next_dict[state1]

        key_list = list(curr_dict.keys())
        val_list = list(curr_dict.values())
        if 37 in val_list:
            print("correct key is", key_list[val_list.index(37)])
            #print("This should display 37", curr_dict['q0'])
        for values in range(len(val_list)):
            if val_list[values] == 37:
                index = values
                print("correct value found at", index)

    first = list(curr_dict.keys())[0]
    return curr_dict['{q0}']


def main():
    nfa = NFA(  # this code builds the weakly divisible by 7 NFA
        states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q0prime', 'q1prime', 'q2prime', 'q3prime',
                'q4prime', 'q5prime', 'q6prime'},
        input_symbols={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
        transitions={
            'q0': {'1': {'q1', 'q0prime'}, '2': {'q2', 'q0prime'}, '3': {'q3', 'q0prime'},
                   '4': {'q4', 'q0prime'}, '5': {'q5', 'q0prime'}, '6': {'q6', 'q0prime'}, '7': {'q0', 'q0prime'},
                   '8': {'q1', 'q0prime'}, '9': {'q2', 'q0prime'}},
            'q1': {'0': {'q3', 'q1prime'}, '1': {'q4', 'q1prime'}, '2': {'q5', 'q1prime'}, '3': {'q6', 'q1prime'},
                   '4': {'q0', 'q1prime'}, '5': {'q1', 'q1prime'}, '6': {'q2', 'q1prime'}, '7': {'q3', 'q1prime'},
                   '8': {'q4', 'q1prime'}, '9': {'q5', 'q1prime'}, '': {'q1', 'q1prime'}},
            'q2': {'0': {'q6', 'q2prime'}, '1': {'q0', 'q2prime'}, '2': {'q1', 'q2prime'}, '3': {'q2', 'q2prime'},
                   '4': {'q3', 'q2prime'}, '5': {'q4', 'q2prime'}, '6': {'q5', 'q2prime'}, '7': {'q6', 'q2prime'},
                   '8': {'q0', 'q2prime'}, '9': {'q1', 'q2prime'}, '': {'q2', 'q2prime'}},
            'q3': {'0': {'q2', 'q3prime'}, '1': {'q3', 'q3prime'}, '2': {'q4', 'q3prime'}, '3': {'q5', 'q3prime'},
                   '4': {'q6', 'q3prime'}, '5': {'q0', 'q3prime'}, '6': {'q1', 'q3prime'}, '7': {'q2', 'q3prime'},
                   '8': {'q3', 'q3prime'}, '9': {'q4', 'q3prime'}, '': {'q3'}},
            'q4': {'0': {'q5', 'q4prime'}, '1': {'q6', 'q4prime'}, '2': {'q0', 'q4prime'}, '3': {'q1', 'q4prime'},
                   '4': {'q2', 'q4prime'}, '5': {'q3', 'q4prime'}, '6': {'q4', 'q4prime'}, '7': {'q5', 'q4prime'},
                   '8': {'q6', 'q4prime'}, '9': {'q0', 'q4prime'}, '': {'q4'}},
            'q5': {'0': {'q1', 'q5prime'}, '1': {'q2', 'q5prime'}, '2': {'q3', 'q5prime'}, '3': {'q4', 'q5prime'},
                   '4': {'q5', 'q5prime'}, '5': {'q6', 'q5prime'}, '6': {'q0', 'q5prime'}, '7': {'q1', 'q5prime'},
                   '8': {'q2', 'q5prime'}, '9': {'q3', 'q5prime'}, '': {'q5'}},
            'q6': {'0': {'q4', 'q6prime'}, '1': {'q5', 'q6prime'}, '2': {'q6', 'q6prime'}, '3': {'q0', 'q6prime'},
                   '4': {'q1', 'q6prime'}, '5': {'q2', 'q6prime'}, '6': {'q3', 'q6prime'}, '7': {'q4', 'q6prime'},
                   '8': {'q5', 'q6prime'}, '9': {'q6', 'q6prime'}, '': {'q6'}},
            'q0prime': {'0': {'q0prime'}, '1': {'q1prime'}, '2': {'q2prime'}, '3': {'q3prime'}, '4': {'q4prime'},
                        '5': {'q5prime'}, '6': {'q6prime'}, '7': {'q0prime'}, '8': {'q1prime'}, '9': {'q2prime'}},
            'q1prime': {'0': {'q3prime'}, '1': {'q4prime'}, '2': {'q5prime'}, '3': {'q6prime'}, '4': {'q0prime'},
                        '5': {'q1prime'}, '6': {'q2prime'}, '7': {'q3prime'}, '8': {'q4prime'}, '9': {'q5prime'}},
            'q2prime': {'0': {'q6prime'}, '1': {'q0prime'}, '2': {'q1prime'}, '3': {'q2prime'}, '4': {'q3prime'},
                        '5': {'q4prime'}, '6': {'q5prime'}, '7': {'q6prime'}, '8': {'q0prime'}, '9': {'q1prime'}},
            'q3prime': {'0': {'q2prime'}, '1': {'q3prime'}, '2': {'q4prime'}, '3': {'q5prime'}, '4': {'q6prime'},
                        '5': {'q0prime'}, '6': {'q1prime'}, '7': {'q2prime'}, '8': {'q3prime'}, '9': {'q4prime'}},
            'q4prime': {'0': {'q5prime'}, '1': {'q6prime'}, '2': {'q0prime'}, '3': {'q1prime'}, '4': {'q2prime'},
                        '5': {'q3prime'}, '6': {'q4prime'}, '7': {'q5prime'}, '8': {'q6prime'}, '9': {'q0prime'}},
            'q5prime': {'0': {'q1prime'}, '1': {'q2prime'}, '2': {'q3prime'}, '3': {'q4prime'}, '4': {'q5prime'},
                        '5': {'q6prime'}, '6': {'q0prime'}, '7': {'q1prime'}, '8': {'q2prime'}, '9': {'q3prime'}},
            'q6prime': {'0': {'q4prime'}, '1': {'q5prime'}, '2': {'q6prime'}, '3': {'q0prime'}, '4': {'q1prime'},
                        '5': {'q2prime'}, '6': {'q3prime'}, '7': {'q4prime'}, '8': {'q5prime'}, '9': {'q6prime'}}
        },
        initial_state='q0',
        final_states={'q0', 'q0prime'}
    )

    str_length = int(input("Enter an integer for string length: "))
    dfa = DFA.from_nfa(nfa)     # creates a DFA from the above built NFA
    print("Minifying DFA...")
    min_dfa = dfa.minify()
    #min_dfa.transitions = sorted(min_dfa.transitions)
    min_dfa.states = sorted(min_dfa.states)
    #print(min_dfa.accepts_input('0147'))  # should be false
    #print(min_dfa.accepts_input('1047'))  # should be true

    delta_table = generate_delta_table(min_dfa)
    #pprint(delta_table)

    num_strings = count(str_length, min_dfa, delta_table)
    print("The number of strings of length", str_length, "accepted by the DFA is", num_strings)


main()
