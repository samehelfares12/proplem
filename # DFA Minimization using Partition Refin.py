# DFA Minimization using Partition Refinement Method

states = ['A', 'B', 'C', 'D', 'E']
alphabet = ['0', '1']
transitions = {
    'A': {'0': 'B', '1': 'C'},
    'B': {'0': 'A', '1': 'D'},
    'C': {'0': 'E', '1': 'C'},
    'D': {'0': 'B', '1': 'E'},
    'E': {'0': 'E', '1': 'C'}
}
start_state = 'A'
accept_states = ['C', 'E']

accepting = [s for s in states if s in accept_states]
non_accepting = [s for s in states if s not in accept_states]

partitions = []
if accepting:
    partitions.append(accepting)
if non_accepting:
    partitions.append(non_accepting)

changed = True
while changed:
    changed = False
    new_partitions = []

    for group in partitions:
        signatures = {}

        for state in group:
            signature = tuple(transitions[state][a] for a in alphabet)
            if signature not in signatures:
                signatures[signature] = []
            signatures[signature].append(state)

        for key in signatures:
            new_partitions.append(signatures[key])

        if len(signatures) > 1:
            changed = True

    partitions = new_partitions

representative = {}
for part in partitions:
    rep = part[0]
    for s in part:
        representative[s] = rep

minimized_transitions = {}
for part in partitions:
    rep = representative[part[0]]
    minimized_transitions[rep] = {}
    for a in alphabet:
        dest = transitions[rep][a]
        minimized_transitions[rep][a] = representative[dest]

minimized_start = representative[start_state]
minimized_accepts = [rep for rep in minimized_transitions if rep in accept_states]

print("Minimized DFA:")
print("States:", list(minimized_transitions.keys()))
print("Alphabet:", alphabet)
print("Transitions:")
for state in minimized_transitions:
    print(f"  {state}: {minimized_transitions[state]}")
print("Start State:", minimized_start)
print("Accept States:", minimized_accepts)