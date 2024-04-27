import itertools
import re


def parse_infix(expression):
    precedence = {'!': 4, '-': 3, '&': 2, '|': 2, '->': 1, '~': 0}
    output = []
    stack = []

    tokens = re.findall(r'[a-e]|[\!-\&\|\-\>~()]|\s+|\S', expression)
    tokens = [token for token in tokens if token.strip() != '']

    for token in tokens:
        if token.isalpha():
            output.append(token)
        elif token in precedence:
            if token == '-':
                if stack and stack[-1] in precedence:
                    output.append(stack.pop())
                    stack.append(token)
                else:
                    stack.append(token)
            else:
                while (stack and stack[-1] in precedence and
                       precedence[token] <= precedence[stack[-1]]):
                    output.append(stack.pop())
                stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses")
            stack.pop()
        else:
            raise ValueError(f"Invalid token: {token}")

    while stack:
        if stack[-1] == '(':
            raise ValueError("Mismatched parentheses")
        output.append(stack.pop())

    return output

def evaluate_expression(expression, variables):
    stack = []
    for token in expression:
        if token in variables:
            stack.append(variables[token])
        elif token == '!':
            stack[-1] = not stack[-1]
        elif token == '&':
            b = stack.pop()
            a = stack.pop()
            stack.append(a and b)
        elif token == '|':
            b = stack.pop()
            a = stack.pop()
            stack.append(a or b)
        elif token == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(not a or b)
        elif token == '~':
            b = stack.pop()
            a = stack.pop()
            stack.append((not a or b) and (not b or a))
    return stack[0]

def create_truth_table(expression):
    int_result = ""
    variables = sorted(set(token for token in expression if token.isalpha()))
    n_variables = len(variables)

    combinations = list(itertools.product([False, True], repeat=n_variables))

    truth_table = []
    for combination in combinations:
        variable_values = {var: value for var, value in zip(variables, combination)}

        result = evaluate_expression(expression, variable_values)

        truth_table.append(combination + (result,))
        int_result += str(int(result))
    return truth_table, variables, int_result


def generate_sdnf(truth_table, variables):
    index = 0
    sdnf_numeric_form = []
    minterms = []
    for combination in truth_table:
        if combination[-1]:
            minterms.append(combination)
            sdnf_numeric_form.append(index)
            index += 1
        else:
            index += 1
    sdnf_terms = []

    for minterm in minterms:
        term = '('
        for var, value in zip(variables, minterm[:-1]):
            if not value:
                term += '!' + var + ' & '
            else:
                term += var + ' & '
        sdnf_terms.append(term.rstrip(' & ') + ')')

    sdnf = ' | '.join(sdnf_terms)
    return sdnf, sdnf_numeric_form


def generate_sknf(truth_table, variables):
    index = 0
    sknf_numeric_form = []
    maxterms = []
    for combination in truth_table:
        if not combination[-1]:
            maxterms.append(combination)
            sknf_numeric_form.append(index)
            index += 1
        else:
            index += 1
    sknf_terms = []

    for maxterm in maxterms:
        term = '('
        for var, value in zip(variables, maxterm[:-1]):
            if value:  # If the variable is complemented
                term += '!' + var + ' | '
            else:
                term += var + ' | '
        sknf_terms.append(term.rstrip(' | ') + ')')

    sknf = ' & '.join(sknf_terms)
    return sknf, sknf_numeric_form


expression = "(!a - (b | c))"
parsed_expression = parse_infix(expression)
truth_table, variables, int_result = create_truth_table(parsed_expression)

print(' '.join(variables) + ' Result')
for row in truth_table:
    print(' '.join(str(int(val)) for val in row))

sdnf, sdnf_numeric_form = generate_sdnf(truth_table, variables)
sknf, sknf_numeric_form = generate_sknf(truth_table, variables)
print("SDNF:", sdnf)
print("SKNF:", sknf)
print("Числовые формы:")
print(f'{sdnf_numeric_form}| \n {sknf_numeric_form}&')
print("Индексная форма:")
print(f'{int(int_result, 2)} - {int_result}')