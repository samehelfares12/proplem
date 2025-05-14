# CFG to CNF Conversion

def convert_to_cnf(cfg):
    cnf = {}
    for non_term, prods in cfg.items():
        cnf[non_term] = [p for p in prods if p != 'ε']
    for non_term, prods in cnf.items():
        new_prods = []
        for p in prods:
            if len(p) == 1 and p.isupper():
                new_prods.extend(cnf.get(p, []))
            else:
                new_prods.append(p)
        cnf[non_term] = new_prods
    for non_term, prods in list(cnf.items()):
        for p in prods:
            if len(p) > 2:
                while len(p) > 2:
                    new_var = f'X{len(cnf) + 1}'
                    cnf[new_var] = [p[:2]]
                    p = new_var + p[2:]
                cnf[non_term].append(p)
    return cnf

cfg = {
    'S': ['AB', 'BC'],
    'A': ['a', 'ε'],
    'B': ['b'],
    'C': ['c']
}

cnf = convert_to_cnf(cfg)
print('CNF Productions:', cnf)
