from automata.fa.nfa import NFA
from automata.fa.dfa import DFA


def main():
    nfa = NFA(
        states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q0prime', 'q1prime', 'q2prime', 'q3prime',
                'q4prime', 'q5prime', 'q6prime'},
        input_symbols={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
        transitions={
            'q0': {'0': {'q0', 'q0prime'}, '1': {'q1', 'q0prime'}, '2': {'q2', 'q0prime'}, '3': {'q3', 'q0prime'},
                   '4': {'q4', 'q0prime'}, '5': {'q5', 'q0prime'}, '6': {'q6', 'q0prime'}, '7': {'q0', 'q0prime'},
                   '8': {'q1', 'q0prime'}, '9': {'q2', 'q0prime'}, '': {'q0'}},
            'q1': {'0': {'q3'}, '1': {'q4'}, '2': {'q5'}, '3': {'q6'}, '4': {'q0'}, '5': {'q1'}, '6': {'q2'},
                   '7': {'q3'}, '8': {'q4'}, '9': {'q5'}, '': {'q1'}},
            'q2': {'0': {'q6'}, '1': {'q0'}, '2': {'q1'}, '3': {'q2'}, '4': {'q3'}, '5': {'q4'}, '6': {'q5'},
                   '7': {'q6'}, '8': {'q0'}, '9': {'q1'}, '': {'q2'}},
            'q3': {'0': {'q2'}, '1': {'q3'}, '2': {'q4'}, '3': {'q5'}, '4': {'q6'}, '5': {'q0'}, '6': {'q1'},
                   '7': {'q2'}, '8': {'q3'}, '9': {'q4'}, '': {'q3'}},
            'q4': {'0': {'q5'}, '1': {'q6'}, '2': {'q0'}, '3': {'q1'}, '4': {'q2'}, '5': {'q3'}, '6': {'q4'},
                   '7': {'q5'}, '8': {'q6'}, '9': {'q0'}, '': {'q4'}},
            'q5': {'0': {'q1'}, '1': {'q2'}, '2': {'q3'}, '3': {'q4'}, '4': {'q5'}, '5': {'q6'}, '6': {'q0'},
                   '7': {'q1'}, '8': {'q2'}, '9': {'q3'}, '': {'q5'}},
            'q6': {'0': {'q4'}, '1': {'q5'}, '2': {'q6'}, '3': {'q0'}, '4': {'q1'}, '5': {'q2'}, '6': {'q3'},
                   '7': {'q4'}, '8': {'q5'}, '9': {'q6'}, '': {'q6'}},
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

    dfa = DFA.from_nfa(nfa)
    print(nfa.read_input('7'))
    print(nfa.read_input('07'))
    print(nfa.accepts_input('21114'))
    print(dfa.accepts_input('21114'))


main()
