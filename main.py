
#
# 1. Напишите функцию, которая принимает значения x, y
# и вычисляет результат (x+2)*(y-3)
# Примечание: Вы уже реализовали эту функцию на уроке.
# Просто перепишите код и убедитесь, что он проходит тесты
#
def evaluate (x, y):
    return (x + 2) * (y - 3)

#def func(x):
#    if x < 0:
#        s1 = ("The result is negative")
#    else:
#        s1 = ("The result is positive")
#    return s1

#result =   f(-7)  * b(-2)
#s = func(result)
#print("The Number is ",result)
#print(s)

#
# 2. Напишите функцию, которая принимает длину и ширину некого прямоугольника
# Функция возвращает True, если этот прямоугольник является квадратом, и False в противном случае
# Примечание 1: Прямоугольник является квадратом, если обе его стороны равны
# Примечание 2: Как известно, геометрическая фигура должна иметь сторону с длиной больше нуля.
# Верните False также в том случае, если квадрат с такими сторонами существовать не может
#
a = float(input("Input width: "))
b = float(input("Input length: "))
def is_square(a, b):
    if a == b and a > 0:
        return True
    else:
        return False
print(is_square(a, b))


#
# 3. Напишите функцию, которая принимает длину и ширину некого прямоугольника
# Функция вычисляет площадь данного прямоугольника
#
# Примечание: Прямоугольник не может иметь отрицательной размерности.
# Если длина или ширина меньше или равна нулю, то верните строку "Error"
# (обратите внимание на корректность написания и регистр!)
#
a = float(input("Input width: "))
b = float(input("Input length: "))
def square_area (a, b):
    if a <= 0 or b <= 0:
        return ("Error")
    else:
        return (a * b)
print("Square is", square_area (a, b))

####
# Код ниже этой строки изменять запрещено
####

def test_is_square():
    assert is_square(3, 5) == False
    assert is_square(5, 3) == False
    assert is_square(3, 3) == True
    assert is_square(3, 0) == False
    assert is_square(0, 30) == False
    assert is_square(-3, 3) == False
    assert is_square(-5, -5) == False

def test_square_area():
    assert square_area(3, 5) == 15
    assert square_area(5, 3) == 15
    assert square_area(0, 10) == "Error"
    assert square_area(0, -4) == "Error"
    assert square_area(-5, -4) == "Error"

def test_evaluation():
    assert evaluate(2, 3) == 0
    assert evaluate(2, 0) == -12
    assert evaluate(-7, -2) == 25

if __name__ == '__main__':
    test_is_square()
    test_square_area()
    test_evaluation()
