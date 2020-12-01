from automata.fa.nfa import NFA
from automata.fa.dfa import DFA


def count(str_length, dfa):
    curr_dict = {}
    next_dict = {}
    for state in dfa.states:
        curr_dict[state] = 0
        next_dict[state] = 0

    # below code block populates curr_dict at accepting states
    for state in curr_dict:
        if state in dfa.final_states:
            curr_dict[state] = 1

    # build next_dict from curr_dict
    for i in range(str_length):
        for state in dfa.states:
            next_dict[state] = curr_dict[dfa.transitions[state]['0']] + curr_dict[dfa.transitions[state]['1']] + \
                               curr_dict[dfa.transitions[state]['2']] + curr_dict[dfa.transitions[state]['3']] + \
                               curr_dict[dfa.transitions[state]['4']] + curr_dict[dfa.transitions[state]['5']] + \
                               curr_dict[dfa.transitions[state]['6']] + curr_dict[dfa.transitions[state]['7']] + \
                               curr_dict[dfa.transitions[state]['8']] + curr_dict[dfa.transitions[state]['9']]

        for state1 in dfa.states:
            curr_dict[state1] = next_dict[state1]

    return curr_dict['{start_state}']


def main():
    nfa = NFA(  # this code builds the weakly divisible by 7 NFA
        states={'start_state', 'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q0prime', 'q1prime', 'q2prime', 'q3prime',
                'q4prime', 'q5prime', 'q6prime', 'fail_state'},
        input_symbols={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
        transitions={
            'start_state': {'0': {'fail_state'}, '1': {'q1', 'q0prime'}, '2': {'q2', 'q0prime'}, '3': {'q3', 'q0prime'},
                            '4': {'q4', 'q0prime'}, '5': {'q5', 'q0prime'}, '6': {'q6', 'q0prime'},
                            '7': {'q0', 'q0prime'},
                            '8': {'q1', 'q0prime'}, '9': {'q2', 'q0prime'}},
            'fail_state': {'0': {'fail_state'}, '1': {'fail_state'}, '2': {'fail_state'}, '3': {'fail_state'},
                           '4': {'fail_state'}, '5': {'fail_state'}, '6': {'fail_state'}, '7': {'fail_state'},
                           '8': {'fail_state'}, '9': {'fail_state'}},
            'q0': {'0': {'q0', 'q0prime'}, '1': {'q1', 'q0prime'}, '2': {'q2', 'q0prime'}, '3': {'q3', 'q0prime'},
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
        initial_state='start_state',
        final_states={'q0', 'q0prime'}
    )

    str_length = int(input("Enter an integer for string length: "))
    dfa = DFA.from_nfa(nfa)  # creates a DFA from the above built NFA

    num_strings = count(str_length, dfa)
    print("The number of strings of length", str_length, "accepted by the DFA is", num_strings)


main()
