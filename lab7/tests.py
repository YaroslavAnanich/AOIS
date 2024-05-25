import unittest
import Main
class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        # Создаем матрицу для тестов
        self.matrix = [[0 for _ in range(16)] for _ in range(16)]
        self.matrix = Main.write_word_to_column(self.matrix, "1001001100110011", 1)

    def test_find_word(self):
        # Проверяем, что функция find_word находит слово в матрице
        self.assertEqual(Main.find_word(self.matrix, "1001001100110011"), (1, 1))
        # Проверяем, что функция find_word возвращает None, если слово не найдено


    def test_read_word_by_index(self):
        self.matrix = Main.write_word_to_column(self.matrix, "1001001100110011", 1)
        word = Main.read_word_by_index(self.matrix, 1)
        self.assertEqual(word, "1001001100110011")


    def test_perform_disjunction_and_paste(self):
        # Проверяем, что функция perform_disjunction_and_paste выполняет операцию "или" и вставляет результат
        self.matrix = Main.perform_disjunction_and_paste(self.matrix, 1, 2, 4)
        self.assertEqual(Main.read_word_by_index(self.matrix, 3), "0000000000000000")

    def setUp(self):
        # Создаем матрицу для тестов
        self.matrix = [[0 for _ in range(16)] for _ in range(16)]
        self.matrix = Main.write_word_to_column(self.matrix, "1001001100110011", 1)

    # ... (остальные тесты)

    def test_read_word_by_index(self):
        # Проверяем, что функция read_word_by_index корректно читает слово из матрицы
        self.assertEqual(Main.read_word_by_index(self.matrix, 1), "1001001100110011")

    def test_write_word_to_column(self):
        # Проверяем, что функция write_word_to_column корректно записывает слово в столбец матрицы
        word = "0101010101010101"
        column_index = 2
        self.matrix = Main.write_word_to_column(self.matrix, word, column_index)
        self.assertEqual(Main.read_word_by_index(self.matrix, column_index), word)

    def test_add_fields_for_matching_v(self):
        # Проверяем, что функция add_fields_for_matching_v корректно изменяет значения в столбцах, у которых v_field соответствует v_key
        v_key = "001"  # Предполагается, что v_key в двоичном формате
        self.matrix = Main.add_fields_for_matching_v(self.matrix, v_key)
        # Добавьте проверку, что значения в столбцах, у которых v_field соответствует v_key, были изменены соответствующим образом
        # Например, проверьте, что значение в столбце 1 изменилось
    def test_perform_pierce_operation_and_paste(self):
        # Проверяем, что функция perform_pierce_operation_and_paste выполняет операцию "не или" и вставляет результат
        self.matrix = Main.perform_pierce_operation_and_paste(self.matrix, 1, 2, 3)
        self.assertEqual(Main.read_word_by_index(self.matrix, 3), "0110110011001100")

    def test_perform_conjunction_negation_and_paste(self):
        # Проверяем, что функция perform_conjunction_negation_and_paste выполняет операцию "и не" и вставляет результат
        self.matrix = Main.perform_conjunction_negation_and_paste(self.matrix, 1, 2, 3)
        self.assertEqual(Main.read_word_by_index(self.matrix, 3), "1001001100110011")

    def test_perform_negation_disjunction_and_paste(self):
        # Проверяем, что функция perform_negation_disjunction_and_paste выполняет операцию "не или" и вставляет результат
        self.matrix = Main.perform_negation_disjunction_and_paste(self.matrix, 1, 2, 3)
        self.assertEqual(Main.read_word_by_index(self.matrix, 3), "0110110011001100")

    def test_search_values_in_interval(self):
        # Проверяем, что функция search_values_in_interval находит значения в заданном интервале
        self.assertEqual(Main.search_values_in_interval(self.matrix, "0010000000000000", "1111111111111111"), [1])

if __name__ == '__main__':
    unittest.main()