#  1 Map
#  1
def grad(c):
    return (c * 9/5) +32

numb = [0, 10, 20, 30, 40]
squa_num = list(map(grad, numb))
print(numb)
print(squa_num)

new = list(map(lambda xy: xy / 5, squa_num))
print(new)


#  2
def lang(n):
    return len(n)
numb = ['apple', 'banana', 'orange', 'kiwi']
squa_num = map(lang, numb)
print(list(squa_num))


#  3
def text(x):
    return x.upper()
numbers = ['hello', 'world', 'python', 'programming']
result = list(map(text, numbers))
print(result)

#  2 Filter
#  1
def is_event(x):
    return len(x) < 5

numbers = ['apple', 'banana', 'orange', 'kiwi', 'grape']
even_numbers = filter(is_event, numbers)
print(list(even_numbers))


#  2
def empty_str(x):
    return len(x) == 0

numbers = ['hello', '', 'world', 'python', '', 'programming']
empty = filter(empty_str, numbers)
print(list(empty))


#  3
def name_a (x):
    return x[0] != 'a'

numbers = ['apple', 'banana', 'orange', 'kiwi', 'grape', 'avocado']
name = filter(name_a, numbers)
print(list(name))


#  3 Reduce

from functools import reduce
#  1
def sum_nubers(x,y):
    return x + y
numbers = [1, 2, 3, 4, 5]
summ = reduce(sum_nubers, numbers)
print(summ)


#  2
numbers = [23, 12, 56, 34, 78, 9, 67]
print(reduce(max, numbers))


#  3

def string_l(x, y):
    return x + " " + y

line = ['hello', 'world', 'python', 'programming']
print(list(reduce(string_l, line)))