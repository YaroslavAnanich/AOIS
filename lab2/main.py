import itertools

def generate_truth_table(expression, variables):
    combinations = list(itertools.product([True, False], repeat=len(variables)))
    combinations = combinations[::-1]

    print(' '.join(variables) + ' ' + expression)

    minterms = []
    maxterms = []
    binary_numbers_last_column = []
    binary_numbers_0 = []
    binary_numbers_1 = []
    for combination in combinations:
        values = {var: value for var, value in zip(variables, combination)}
        expression_py = expression.replace('&', ' and ').replace('|', ' or ').replace('!', ' not ').replace('->', '<=').replace('~', '==')
        try:
            result = eval(expression_py, {}, values)
        except Exception as e:

            print(f"Error evaluating expression: {e}")

            return
        binary_numbers_last_column.append(str(int(result)))
        print(' '.join(str(int(value)) for value in combination) + ' ' + str(int(result)))
        if result:
            minterm = ' & '.join(var if value else '!' + var for var, value in zip(variables, combination))
            minterms.append(minterm)
            binary_numbers_1.append(''.join(str(int(value)) for value in combination))
        else:
            maxterm = ' | '.join('!' + var if value else var for var, value in zip(variables, combination))
            maxterms.append(maxterm)
            binary_numbers_0.append(''.join(str(int(value)) for value in combination))
    sdnf = ' | '.join(minterms) if minterms else '0'
    sknf = ' & '.join(maxterms) if maxterms else '1'
    print("\nSDNF:", sdnf)

    print("SKNF:", sknf)

    print("\nЧисловые формы: ")

    print([int(num, 2) for num in binary_numbers_0], "&")

    print([int(num, 2) for num in binary_numbers_1], "|")

    print("\nИндексная форма: ")

    print(int(''.join(binary_numbers_last_column), 2), "-", ''.join(binary_numbers_last_column))

# Example usage:
expression = "((a | c) -> ((!b ~ d) & e))"
variables = ['a', 'b', 'c', 'd', 'e']
generate_truth_table(expression, variables)