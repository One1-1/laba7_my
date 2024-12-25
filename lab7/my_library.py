def task7_1():
    import math
    n = 5
    x = [1.0, 2.0, 3.0, 4.0, 5.0, 7.0]
    y = 0
    for i in range(1, n + 1):
        y += (-1) ** i * x[i - 1]
    print(f'f = {y}')

    s = 0
    for i in range(1, n + 1):
        s += x[i - 1] ** 2
    p = math.sqrt(s)
    print(f'p = {p}')


def task7_2(arr):
    n = len(arr)
    if n < 2:
        return arr  # Если массив слишком маленькиц, возвращаем его как есть

    result = [0] * n  # Создаем новый массив той же длины

    result[0] = arr[0]  # Копируем первый элемент

    # Заменяем элементы от 1 до n-2
    for i in range(1, n - 1):
        result[i] = arr[i - 1] or arr[i + 1]  # Логическая сумма соседей

    result[n - 1] = arr[n - 1]  # Копируем последний элемент

    return result

def task7_3():
    import math

    def calculate_distance(point1, point2):
        # Функция для вычисления расстояния между двумя точками
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)  # По теореме Пифагора

    def osn():
        # Основная функция программы
        coordinates = []  # Список для хранения координат точек
        n = int(input("Введите количество точек: "))

        for i in range(n):  # ввод координат каждой точки
            x, y = map(float, input(f"Введите координаты точки {i + 1} (x y): ").split())  # Вводим координаты и преобразуем их в float
            coordinates.append((x, y))

        distances = []  #расстояния между соседними точками
        for i in range(len(coordinates) - 1):  # Цикл по индексам точек, кроме последней
            distance = calculate_distance(coordinates[i],coordinates[i + 1])  # Вычисляем расстояние между соседними точками
            distances.append(distance)

        for i, distance in enumerate(distances):
            print(f"Расстояние между точкой {i + 1} и точкой {i + 2}: {distance:.2f}")

    osn()

def task7_4():
    def check_positions_zeros(input_string):
        numbers = list(map(int, input_string.split()))
        # Проверяем нечетные позиции (индексы 1, 3, 5 и тд) на наличие нулей
        for j in range(1, len(numbers), 2):
            if numbers[j] != 0:
                return False
        return True

    input_string = input("Введите строку чисел, разделенных пробелами: ")

    if check_positions_zeros(input_string):
        print("На всех нечетных позициях стоят нули.")
    else:
        print("На нечетных позициях есть ненулевые значения.")


def task7_5():
    def create_dict(numbers):
        square_dict = {}
        for number in numbers:
            #if number in square_dict:
                #square_dict[number] += number ** 2  # Суммируем квадраты для неуникальных ключей
            #else:

            square_dict[number] = number ** 2  # Добавляем новый ключ и его квадрат
        return square_dict

    input_numbers = input("Введите список чисел: ")
    numbers = list(set(map(int, input_numbers.split())))
    result_dict = create_dict(numbers)

    print(result_dict)


def task7_6():
    consonants = 'бвгджзйклмнпрстфхцчшщ'
    unique = set()
    consonant_count = {}

    input_string = input('Ведите слова через запятую, в концу точка: ')
    words = input_string[:-1].split(", ")

    print(words)

    for word in words:
        for char in word:
            char = char.lower()
            if char in consonants:
                unique.add(char)

    for consonant in unique:
        if consonant in consonant_count:
            consonant_count[consonant] += 1
        else:
            consonant_count[consonant] = 1

    unique_consonant = []

    for consonant, count in consonant_count.items():
        if count == 1:
            unique_consonant.append(consonant)



    unique_consonant.sort()
    print(unique_consonant)




