# print("Hello world")
# print()
# print('test')
#
# print("one", "two", "three", sep="-", end=" ")
# print("hello")
# print("hello")

# однорядковий коментар

'''
три одинарні лапки
багаторядковий
коментар
тут можна писати будь-який текст і він буде проігнорований інтерпретатором
'''

# оператор присвоєння

# Ctrl + / -> comment или uncomment

# print("hello11")
# print("hello22")
#
# aljfjklsdfjkvskjfd
# print("qwerty")

########################
####
# # escape послідовності
# # \n -> перенесення на новий рядок
# print("Hello\nworld")
# # \t -> табуляція -> 4 пробіли. (буває в консолі 2 або 8 пробіли)
# print("Hello\n\tworld")
# # \ -> дзеркалювання, екранування – якщо необхідно службовий символ зробити друкованим
# print("hello \"world\"")
# print("hello \'world\'")
# print("Hello\\n\\t\"world\"")
# print("\\\\\\\\\\")
# print("\n" * 10)

##############
#####
# int -> ціле число 12
# float -> дробове число 12.5
# bool -> логічний тип даних: True False
# str -> рядок - масив (набір) символів

# Змінна - це іменована область оперативної пам'яті значення можна змінювати
# number: int = 10
# print(number)
# print(type(number))
# number = 20.5
# print(number)
# print(type(number))
# number = "Vasya"
# print(number)
# print(type(number))
# number = True
# print(number)
# print(type(number))

####################
# user_name1 = "Vasya"
# userName = "Vasya"
# name = "qqq"

##############
# # input -> буде очікувати на введення даних з клавіатури в консолі і поверне за замовчуванням значення типу даних str
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# # v1
# print("Name: ", name, " Age: ", age)
# # v2 конкатенація - складання рядків. Рядок + рядок -> один великий рядок
# print("Name: " + name + " Age: " + str(age))
# # print("Name: " + name + " Age: " + age, 1234, "qwehbkqwer" + "sdbhdvsfkjhbdsvafbk")
# # v3 інтерполяція рядка - вбудовування змінних у рядок завдяки функції format (вивчимо докладніше пізніше)
# print(f"Name: {name} age: {age}")
#
# print(age + 10)

################################################################
# + - * /
# print(2 + 3)
# print(2 - 3)
# print(2 * 3)
# print(2 / 3)
# print(2 ** 3)  # основа ** показник (зведення в ступінь
# print(2 // 3)  # ціла частина від розподілу
# print(2 % 3)  # залишок від ділення
#
# num1 = 15
# num2 = 8
# print(num1 // num2)
# print(num1 % num2)

##################
############
# ввести з клавіатури тризначне число та вивести суму цифр цього числа
# // %
# int() - так як input поверне str, нам потрібно цей рядок привести до типу int (ціле число)
# щоб можна було застосовувати арифметичні оператори
# number = int(input("Enter 3-digit number: "))
# # 146
# n1 = number // 100
# # v1
# n2 = number // 10 % 10
# # v2
# # n2 = number % 100 // 10
# n3 = number % 10
#
# result = n1 + n2 + n3
# print(f"n1: {n1} n2: {n2} n3 {n3}")
# print(f"Result: {result}")
#
# # number = 10
# # print(number)

##
# git init -> create git repository
# print("hello world")

###################
# умови
# v1
# n1 = 10 + 20 * 2  # оператор привласнення, отрабатывает последним
# n2 = 20
# v2
# n1, n2 = 10, 20 + 10  # множинне привласнення
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)
# print(n1 <= n2)
# print(n1 == n2)  # поверне True якщо обидва операнди рівні (однакові)
# print(n1 != n2)  # поверне True якщо обидва операнди різні
#
# print(1 == 1 and 3 == 3)  # поверне True якщо обидва операнди рівні True, інакше False
# print(1 == 1 or 2 == 3)  # поверне True якщо хоча б один операнд дорівнює True, інакше False
#
# is_valid = False
# print(is_valid)
# print(not is_valid)  # not -> інверсія, якщо значення False стане True, і навпаки

# print("hello" in "hello world")

#############
# hours = int(input("Enter hours: "))
#
# # v1
# # if hours >= 12:
# #     print("PM")
# #     print("asedfasdf")
# # else:
# #     print("AM")
#
# # v2
# if 12 <= hours < 24:
#     print("PM")
# elif hours >= 0 and hours < 12:
#     print("AM")
# else:
#     print("Incorrect hours!")
#
# print("Hello world")

##################################
# ввести рейтинг фільму: якщо рейтинг дорівнює 5 або 4 - ок, інакше - погано

# film_rating = int(input("Enter film rating: "))
#
# if 0 < film_rating <= 5:
#     if film_rating == 4 or film_rating == 5:
#         print("OK")
#     else:
#         print("Not ok")
# else:
#     print("Incorrect rating!")

########
# 1. create develop branch from master branch
# 2. create feature branch from develop branch

# ввести з клавіатури 3 числа
# - вивести найменше із трьох чисел
# - кол-во однакових чисел

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
#
# # вывести наименьшее из трех чисел
# if n1 < n2 < n3:
#     print(n1)
# elif n2 < n3 < n1:
#     print(n2)
# elif n3 < n2 < n1:
#     print(n3)
# else:
#     print("All numbers equals")

# - кол-во одинаковых чисел
if n1 == n2 == n3:
    print(3)
elif n1 == n2 or n2 == n3 or n1 == n3:
    print(2)
else:
    print(0)
