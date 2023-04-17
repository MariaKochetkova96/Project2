
# 2. Вам дается файл task2_input.txt, в нем лежит список. Каждый элемент на новой строке, и последняя строка - значение
# искомого элемента el.
# Напишите функцию, которая будет принимать имя этого файла, читать данные из него и создавать файл task2_output.txt,
# куда будет записывать часть списка ДО первого места, где попался el.
# Пример: в функцию передан файл с числами -1, 3, 2, 5, 1, 6, 2 (каждый с новой строки, здесь через запятую
# для краткости). В таком случае значение el - 2 (последняя строка), и ваша функция должна записать в файл
# список -1, 3 (каждый элемент с новой строки).
# Если значение, равное el, стоит на первом месте списка, запишите в файл слово "Empty".
# Если значения, равного el, в списке не нашлось, запишите в файл слово "Error"

def get_sublist(file_name):
    file = open("task2_input.txt", "r")

    input_list = []
    for line in file:
        line_cleaned = line.strip()
        input_list.append(line_cleaned)

    item = input_list.pop(-1)
    output_file = open("task2_output.txt", "w")
    if item not in input_list:
         output_file.write("Error")
    elif item == input_list[0]:
        output_file.write("Empty")
    else:
        output_list = []
        for el in input_list:  # сторити output_list, пройтись в циклі по листу і всі ел записати у файл
            if el == item:
                output_list.append(n)
                output_file.write(output_list[0:item])



    # 3. В функцию передается CSV файл task3_input.csv, c заголовком city,score. Ниже в нем информация в
# виде "название города,кол-во балов" (делимитер - запятая).
# Функция должна вернуть CSV файл task3_output.csv следующего вида:
#     score_sum,avg_score,best_city
#     1,2,3
# где:
# 1 - сумма очков всех городов
# 2 - среднее арифметичское всех очков (сумма, деленная на количество элементов)
# 3 - название города, у которого максимальное количество очков

def city_rating(file_name):




# 4. Вам дается файл task4_input.csv с заголовком name,swimming,chess,guitar и контентом следующего вида:
# имя ребенка и через запятую три значения - 1, если ребенок посещает соответствующий кружок, 0 - если нет.
# Пример:
#     name,swimming,chess,guitar
#     Emma,1,0,0
# У Эммы 1 только в колонке swimming, следовательно, она посещает только плавание.
# На основе этих данных вам нужно вычислить детей, которые не знают никого, кроме одногруппников из своего кружка
# (то есть они не пересекаются с детьми из других кружков).
# Результат запишите в файл task4_output.txt, где каждое имя из вычисленного множества - на новой строке

def not_busy_children(file_name):
    pass


# ===========================================================================
# КОД НИЖЕ МЕНЯТЬ НЕЛЬЗЯ
# ===========================================================================

def get_result_list(file_name):
    output = open(file_name)

    result_list = []
    for line in output:
        result_list.append(line.strip())
    return result_list


def test_get_sublist():
    get_sublist("task2_input.txt")
    result_list = get_result_list("task2_output.txt")
    result_list = [int(item) for item in result_list]

    assert result_list == [1, 5, 3]


def test_city_rating():
    city_rating("task3_input.csv")
    result_list = get_result_list("task3_output.txt")
    result = tuple(result_list)

    assert result == ("366", "61.0", "Munich")


def test_not_busy_children():
    not_busy_children("task4_input.csv")
    result_list = get_result_list("task4_output.txt")
    result = set(result_list)

    assert result == {"Emma", "Caroline", "Pam", "Sam"}


if __name__ == '__main__':
    test_get_sublist()
    test_city_rating()
    test_not_busy_children()
    print("Well done!!!")