import itertools
import re

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
            minterm = ' '.join(var if value else '!' + var for var, value in zip(variables, combination))
            minterms.append(minterm)
            binary_numbers_1.append(''.join(str(int(value)) for value in combination))
        else:
            maxterm = ' '.join('!' + var if value else var for var, value in zip(variables, combination))
            maxterms.append(maxterm)
            binary_numbers_0.append(''.join(str(int(value)) for value in combination))
    sdnf = ' | '.join(minterms) if minterms else '0'
    sknf = ' & '.join(maxterms) if maxterms else '1'
    print("\nSDNF:", sdnf)

    print("SKNF:", sknf)
    return sdnf

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
    return truth_table

def sdnf_to_binary(sdnf):
    # Remove the outer parentheses
    sdnf = sdnf.strip('()')

    # Split the input string into clauses
    clauses = sdnf.split('|')
    binary_clauses = []

    # Process each clause
    for clause in clauses:
        binary_clause = []
        # Split the clause into terms
        terms = clause.strip('()').split()
        for term in terms:
            # If the term is a variable, replace it with '1' or '0'
            if term.startswith('!'):
                binary_clause.append('0')
            else:
                binary_clause.append('1')
        # Join the terms in the clause into a string and add it to the list of binary clauses
        binary_clauses.append('(' + ','.join(binary_clause) + ')')

    # Join the binary clauses into a string and return it
    return binary_clauses

def truth_table_min(dict_data, array_data , binary_output):
    output = binary_output
    find_min(dict_data, array_data , binary_output)
    binary_output = list(set(binary_output))
    check = []
    result = []
    len_check = 0
    for array in array_data:
        for element in array:
            if len(check) == len(binary_output):
                result = list(set(result))
                result = put_letters_instead_of_numbers(result)
                return result
            for key, value in dict_data.items():
                is_true = True
                for dict_element in value:
                    is_true = True
                    for j in range(len(dict_element)):
                        if element[j] != '(' and element[j] != ',' and element[j] != ')' and element[j] != '*':
                            if element[j] != dict_element[j]:
                                is_true = False
                        if j == len(dict_element)-1 and is_true:
                            len_check = len(check)
                            check.append(dict_element)
                            check = list(set(check))
                            if len(check) > len_check:
                                result.append(element)
    result = list(set(result))
    if len(check) != len(output):
        check = set(check)
        output = set(output)
        differ = output - check
        differ = list(differ)
        differ = put_letters_instead_of_numbers(differ)
        result = put_letters_instead_of_numbers(result)
        result = result + differ
        return result
    result = put_letters_instead_of_numbers(result)
    return result
def group_by_units(binary_clauses):
    # Create a dictionary to hold the arrays
    constituents = {}

    # Process each binary clause
    for clause in binary_clauses:
        # Count the number of '1's in the clause
        count_ones = clause.count('1')
        # If the count is not already a key in the dictionary, create a new list
        if count_ones not in constituents:
            constituents[count_ones] = []
        # Add the clause to the list corresponding to its count of '1's
        constituents[count_ones].append(clause)
    sorted_constituents = dict(sorted(constituents.items(), key=lambda x: x[0]))
    # Return the arrays
    return sorted_constituents


def compare_constituents(constituents):
    result = []
    keys = list(constituents.keys())

    for i in range(len(keys) - 1):
        current_key = keys[i]
        next_key = keys[i + 1]

        current_arrays = constituents[current_key]
        next_arrays = constituents[next_key]

        for current_array in current_arrays:
            for next_array in next_arrays:
                diff_count = 0
                diff_index = -1
                for j in range(len(current_array)):
                    if current_array[j] != next_array[j]:
                        diff_count += 1
                        diff_index = j

                if diff_count == 1:
                    modified_array = list(current_array)
                    modified_array[diff_index] = '*'
                    modified_array_str = ''.join(modified_array)
                    if modified_array_str not in result:
                        result.append(modified_array_str)

    return result

def compare_elements(elements):
    result = set()
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            diff_count = 0
            diff_index = -1
            for k in range(len(elements[i])):
                if elements[i][k] != '*' and elements[j][k] != '*' and elements[i][k] != elements[j][k]:
                    diff_count += 1
                    diff_index = k
                if elements[i][k] == '*' or elements[j][k] == '*':
                    if elements[i][k] != elements[j][k]:
                        diff_count += 1
            if diff_count == 1:
                modified_element = list(elements[i])
                modified_element[diff_index] = '*'
                result.add(''.join(modified_element))
    return list(result)  # Convert the set back to a list before returning


def put_letters_instead_of_numbers(array_data):
    result = ""
    for element in array_data:
        arr = element.replace("(", "")
        arr = arr.replace(")", "")
        arr = arr.split(",")
        for i in range(len(arr)):
            if arr[i] != '*':
                if arr[i] == '0':
                    result = result + '!'
                if i == 0:
                    result = result + "a "
                if i == 1:
                    result = result + "b "
                if i == 2:
                    result = result + "c "
                if i == 3:
                    result = result + "d "
                if i == 4:
                    result = result + "e "
        result = result[:-1]
        result = result + "|"
    return result

def find_min(dict_data, array_data , binary_output):
    result = []
    min_funs = ""
    for imp in implications:
        min_funs = min_funs + put_letters_instead_of_numbers(imp)
    min_funs = min_funs.replace(' ', ' & ')
    min_funs = '(' + min_funs
    min_funs = min_funs.replace('|', ') | (')
    min_funs = min_funs[:-4]
    print(min_funs)
    parsed_expression = parse_infix(min_funs)
    truth_table = create_truth_table(parsed_expression)
    mins = min_funs.split('|')
    for element in mins:
        element_check = mins.pop()
        truth_check = create_truth_table(parsed_expression)
        if truth_check == truth_table:
            continue
        else:
            result.append(element)
    return result







implications = []
expression = "((a | b) -> c)"
variables = ['a', 'b', 'c']
formula = generate_truth_table(expression, variables)
binary_output = sdnf_to_binary(formula)
constituents = group_by_units(binary_output)
implication = compare_constituents(constituents)
implications.append(implication)
arr = binary_output.copy()[0].replace("(", "")
arr = arr.replace(")", "")
arr = arr.split(",")
for count in range(len(arr)-2):
    implication = compare_elements(implication.copy())
    implications.append(implication)
implications.reverse()

print(truth_table_min(constituents, implications, binary_output))

