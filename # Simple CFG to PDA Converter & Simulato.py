def generate_pda(cfg):
    productions = cfg
    start_symbol = 'S'
    return productions, start_symbol

def simulate_pda(productions, start_symbol, input_str):
    stack = [start_symbol]
    i = 0

    while stack and i <= len(input_str):
        top = stack.pop()

        if top in productions:  # لو متغير
            for rule in productions[top]:
                if rule == 'ε':
                    continue
                stack.extend(reversed(list(rule)))  # طبق القاعدة كاملة
                break
        elif i < len(input_str) and top == input_str[i]:  # لو رمز نهائي
            i += 1
        else:
            return False
    return i == len(input_str) and not stack

def main():
    cfg = {
        'S': ['aSB', 'bSA', 'ε'],
        'A': ['a'],
        'B': ['b']
    }

    productions, start_symbol = generate_pda(cfg)
    test = input("Enter string: ")
    result = simulate_pda(productions, start_symbol, test)
    print("Accepted" if result else "Not Accepted")

if __name__ == "__main__":
    main()