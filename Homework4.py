#                LISTS                 #

# 1. Напишите функцию, которая будет возвращать True, если переданный в нее список отсортирован,
# или False, если он не отсортирован (по возрастанию, т.е. от меньшего к большему). Если в списке строки,
# то отсортированным он считается, когда элементы расположены по алфавиту.

def is_sorted(my_list):
    if my_list == sorted(my_list):
        return True
    else:
        return False


# 2. Напишите функцию, которая будет принимать список и переменную item и возвращать часть списка ДО первого места,
# где попался item.
# Пример: в функцию передан список [-1, 3, 2, 5, 1, 6] и item = 2. В таком случае ваша функция должна вернуть
# список [-1, 3]
# Если значение, равное item, стоит на первом месте списка, верните пустой лист [].
# Если значения, равного item, в списке не нашлось, верните строку "Error"

def get_sublist(my_list, item):
    if item not in my_list:
        return "Error"
    elif my_list.index(item) == 0:
        return []
    else:
        i = my_list.index(item)
        return my_list[:i]


#            DICTIONARIES                 #

# 3. В функцию передан dictionary, где ключи - немецкие города, а занчения - количество очков набранных этим городом
# в рейтинге удобства для жизни.
# Функция должна вернуть tuple, который содержит 3 элемента:
# 1) сумму очков всех городов
# 2) среднее арифметичское всех очков (сумма, деленная на количество элементов)
# 3) название города, у которого максимальное количество очков


def city_rating(cities_dict):
    cities_dict = {
        "Munich": 74,
        "Berlin": 62,
        "Cologne": 51,
        "Hamburg": 68,
        "Dusseldorf": 59,
        "Kassel": 52
    }
    return (sum(cities_dict.values()), (sum(cities_dict.values()) / len(cities_dict.values())), (max(cities_dict.keys())))


#                SETS                 #

# 4. Вам даны списки групп трех детских кружков: плавание (swimming), шахматы (chess) и игра на гитаре (guitar).
# Переданы эти данные в виде dictionary, где ключи - названия кружков, и значения - списки участников.
# Вам нужно вернуть множество детей, которые не знают никого, кроме одногруппников из своего кружка (то есть они
# не пересекаются с детьми из других кружков)

def not_busy_children(groups_dict):
    groups = {
        "swimming": ["Emma", "Albert", "Peter"],
        "chess": ["Caroline", "Albert", "Pam", "Harry"],
        "guitar": ["Harry", "Peter", "Sam"],
    }
    swimming = set(groups_dict["swimming"])
    chess = set(groups_dict["chess"])
    guitar = set(groups_dict["guitar"])

    result1 = swimming.symmetric_difference(chess)
    result2 = result1.symmetric_difference(guitar)
    return (result2)

# ===========================================================================
# КОД НИЖЕ МЕНЯТЬ НЕЛЬЗЯ
# ===========================================================================

def test_is_sorted():
    assert is_sorted([1, 3, 5]) == True
    assert is_sorted([1, 5, 3, 8, 10]) == False
    assert is_sorted(["apple", "blackberry", "cherry", "plum"]) == True
    assert is_sorted(["mercedes", "mazda", "suzuki", "toyota"]) == False


def test_get_sublist():
    assert get_sublist([1, 3, 5], 1) == []
    assert get_sublist([1, 5, 3, 8, 10], 8) == [1, 5, 3]
    assert get_sublist([], 8) == "Error"
    assert get_sublist(["apple", "blackberry", "cherry", "plum"], "carrot") == "Error"
    assert get_sublist(["mercedes", "mazda", "toyota", "suzuki"], "mazda") == ["mercedes"]


def test_city_rating():
    cities_dict = {
        "Munich": 74,
        "Berlin": 62,
        "Cologne": 51,
        "Hamburg": 68,
        "Dusseldorf": 59,
        "Kassel": 52
    }
    assert city_rating(cities_dict) == (366, 61.0, "Munich")


def test_not_busy_children():
    groups = {
        "swimming": ["Emma", "Albert", "Peter"],
        "chess": ["Caroline", "Albert", "Pam", "Harry"],
        "guitar": ["Harry", "Peter", "Sam"],
    }
    assert not_busy_children(groups) == {"Emma", "Caroline", "Pam", "Sam"}


if __name__ == '__main__':
    test_is_sorted()
    test_get_sublist()
    test_city_rating()
    test_not_busy_children()