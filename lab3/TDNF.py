def truth_table(formula, num_variables=1):
    clauses = formula.split('|')
    table = []
    variables = ['a', 'b', 'c', 'd', 'e']
    for values in itertools.product([0, 1], repeat=num_variables):
        variable_values = {var: value for var, value in zip(variables[:num_variables], values)}
        clause_results = []
        for clause in clauses:
            literals = clause.split()
            clause_result = True
            for literal in literals:
                var = literal[-1]  # Get the variable name from the literal
                if var in variable_values:  # Check if the variable is in the current set of variables
                    if literal[0] == '!':
                        clause_result &= (variable_values[var] == 0)
                    else:
                        clause_result &= (variable_values[var] == 1)
            clause_results.append(clause_result)
        result = int(any(clause_results))
        table.append(tuple(values) + (result,))
    return table
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
        result = result + "| "
    result = result[:-2]
    return result
def four_and_three_karnaugh_map(table,count_of_row):
    k_map = []
    a = 0
    b = 2
    c = 3
    d = 1
    for i in range(count_of_row):
        row  = []
        row.append(table[a][-1])
        row.append(table[b][-1])
        row.append(table[c][-1])
        row.append(table[d][-1])
        a += 4
        b += 4
        c += 4
        d += 4
        k_map.append(row)
    if count_of_row == 4:
        k_map[-2], k_map[-1] = k_map[-1], k_map[-2]
    return k_map

def two_karnaugh_map(table):
    k_map = []
    a = 0
    b = 1
    for i in range(2):
        row  = []
        row.append(table[a][-1])
        row.append(table[b][-1])
        a += 2
        b += 2
        k_map.append(row)
    return k_map

def group_by_units(binary_clauses):
    constituents = {}

    for clause in binary_clauses:
        count_ones = clause.count('1')
        if count_ones not in constituents:
            constituents[count_ones] = []
        constituents[count_ones].append(clause)
    sorted_constituents = dict(sorted(constituents.items(), key=lambda x: x[0]))
    return sorted_constituents


def karno_compare_constituents(constituents):
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
def sdnf_to_binary(sdnf):
    sdnf = sdnf.strip('()')

    clauses = sdnf.split('|')
    binary_clauses = []

    for clause in clauses:
        binary_clause = []
        terms = clause.strip('()').split()
        for term in terms:
            if term.startswith('!'):
                binary_clause.append('0')
            else:
                binary_clause.append('1')
        binary_clauses.append('(' + ','.join(binary_clause) + ')')

    return binary_clauses
def karno_check(array_data):
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
        result = result + "| "
    result = result[:-2]
    return result
def karno_compare_elements(elements):
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
    return list(result)

def karno_min(dict_data, array_data , binary_output):
    output = binary_output
    binary_output = list(set(binary_output))
    check = []
    result = []
    len_check = 0
    for array in array_data:
        for element in array:
            if len(check) == len(binary_output):
                result = list(set(result))
                if len(result) == 0:
                    return "Нет совпадений"
                result = karno_check(result)
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
        result = result + "|" + differ
        return result
    if len(result) == 0:
        return "Нет совпадений"
    result = karno_check(result)
    return result



k_map = []
implications = []
expression = "((a | b) -> (a & c))"
variables = ['a', 'b', 'c']
formula = generate_truth_table(expression, variables)
num_variables = 3
table = truth_table(formula, num_variables)
binary_output = sdnf_to_binary(formula)
constituents = group_by_units(binary_output)
implication = karno_compare_constituents(constituents)
implications.append(implication)
print("Таблица истинности:")
for row in table:
    print(row)
print("Карта Карно:")
arr = binary_output.copy()[0].replace("(", "")
arr = arr.replace(")", "")
arr = arr.split(",")
for count in range(len(arr)-2):
    implication = karno_compare_elements(implication.copy())
    implications.append(implication)
implications.reverse()
if num_variables == 4:
    k_map = four_and_three_karnaugh_map(table, 4)
if num_variables == 3:
    k_map = four_and_three_karnaugh_map(table, 2)
if num_variables == 2:
    k_map = two_karnaugh_map(table)
for row in k_map:
    print(row)
print("Результат:")
print(karno_min(constituents, implications, binary_output))
