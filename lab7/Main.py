def find_word(matrix, word):
    # Проверяем, что длина слова соответствует количеству столбцов в матрице
    if len(word) != len(matrix[0]):
        return None

    # Ищем слово в матрице
    for column_index in range(len(matrix[0])):
        word_in_matrix = ""
        for row_index in range(len(matrix)):
            if row_index + column_index < len(matrix):
                word_in_matrix += str(matrix[row_index + column_index][column_index])
            else:
                word_in_matrix += str(matrix[row_index + column_index - len(matrix)][column_index])
        if word_in_matrix == word:
            return (column_index,column_index)
    return None


def perform_disjunction_and_paste(matrix, index1, index2, target_column_index):
    word1 = read_word_by_index(matrix, index1)
    word2 = read_word_by_index(matrix, index2)

    result_word = ""
    for i in range(len(word1)):
        result_word += str(int(word1[i]) or int(word2[i]))

    matrix = write_word_to_column(matrix, result_word, target_column_index)

    return matrix


def perform_pierce_operation_and_paste(matrix, index1, index2, target_column_index):
    word1 = read_word_by_index(matrix, index1)
    word2 = read_word_by_index(matrix, index2)

    result_word = ""
    for i in range(len(word1)):
        result_word += str(int(not (int(word1[i]) or int(word2[i]))))

    matrix = write_word_to_column(matrix, result_word, target_column_index)

    return matrix


def perform_conjunction_negation_and_paste(matrix, index1, index2, target_column_index):
    word1 = read_word_by_index(matrix, index1)
    word2 = read_word_by_index(matrix, index2)

    result_word = ""
    for i in range(len(word1)):
        result_word += str(int(int(word1[i]) and not int(word2[i])))

    matrix = write_word_to_column(matrix, result_word, target_column_index)

    return matrix


def perform_negation_disjunction_and_paste(matrix, index1, index2, target_column_index):
    word1 = read_word_by_index(matrix, index1)
    word2 = read_word_by_index(matrix, index2)

    result_word = ""
    for i in range(len(word1)):
        result_word += str(int(not int(word1[i]) or int(word2[i])))

    matrix = write_word_to_column(matrix, result_word, target_column_index)

    return matrix
def read_word_by_index(matrix, column_index):
    word = ""
    for row_index in range(len(matrix)):
        if row_index + column_index < len(matrix):
            word += str(matrix[row_index + column_index][column_index])
        else:
            word += str(matrix[row_index + column_index - len(matrix)][column_index])
    return word


def write_word_to_column(matrix, word, column_index):
    for row_index in range(len(matrix)):
        if row_index + column_index < len(matrix):
            matrix[row_index + column_index][column_index] = int(word[row_index])
        else:
            matrix[row_index + column_index - len(matrix)][column_index] = int(word[row_index])
    return matrix
def adres_row(matrix,number):
    print("Адреса столбцов:")
    for column_index in range(len(matrix[0])):
        if (column_index+number <= 15):
            print(matrix[column_index+number][column_index], end="")
        else:
            print(matrix[column_index + number-16][column_index], end="")

def add_fields_for_matching_v(matrix, v_key):
    for column_index in range(len(matrix[0])):
        word = read_word_by_index(matrix, column_index)
        v_field = int(word[:3], 2)
        a_field = int(word[3:7], 2)
        b_field = int(word[7:11], 2)
        s_field = int(word[11:], 2)

        if v_field == int(v_key, 2):
            result = a_field + b_field
            new_s_field = format(result, '05b')

            new_word = word[:11] + new_s_field
            matrix = write_word_to_column(matrix, new_word, column_index)

    return matrix
def search_values_in_interval(matrix, lower_bound, upper_bound):
    # Инициализируем флаги результата для каждого слова в матрице
    result_flags = [1] * len(matrix[0])

    # Шаг 1: отыскиваются все числа, которые меньше верхней границы
    for column_index in range(len(matrix[0])):
        word = read_word_by_index(matrix, column_index)
        if int(word, 2) < int(upper_bound, 2):
            result_flags[column_index] = 1
        else:
            result_flags[column_index] = 0

    # Шаг 2: отыскиваются те числа, которые больше нижней границы
    for column_index in range(len(matrix[0])):
        word = read_word_by_index(matrix, column_index)
        if int(word, 2) > int(lower_bound, 2) and result_flags[column_index] == 1:
            result_flags[column_index] = 1
        else:
            result_flags[column_index] = 0

    # Возвращаем список индексов слов, которые находятся в требуемом интервале
    return [i for i, flag in enumerate(result_flags) if flag == 1]



def print_matrix(matrix):
    for row in matrix:
        print(row)
    print("\n")


# Создаем пустую матрицу 16x16
matrix = [[0 for _ in range(16)] for _ in range(16)]

# Записываем значение в столбец 1
matrix = write_word_to_column(matrix, "1001001100110011", 2)
print("Initial matrix:")
print_matrix(matrix)
print("Слово найдено:",find_word(matrix, "1001001100110011"))
print("Слово найдено:",read_word_by_index(matrix, 2))
adres_row(matrix,0)
print("\n")

matrix = write_word_to_column(matrix, "1000000000000000", 3)
perform_disjunction_and_paste(matrix, 2, 3, 4)
print_matrix(matrix)
perform_pierce_operation_and_paste(matrix, 2, 3, 4)
print_matrix(matrix)
perform_conjunction_negation_and_paste(matrix, 2, 3, 4)
print_matrix(matrix)
perform_negation_disjunction_and_paste(matrix, 2, 3, 4)
print_matrix(matrix)
result=search_values_in_interval(matrix,"0010000000000000", "1111111111111111")
print("Слова в указанном интервале :")
print(result)
matrix = write_word_to_column(matrix, "1111000000000000", 15)
result1 = add_fields_for_matching_v(matrix, "111")
print("Ключ применён")
print_matrix(result1)
