
"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""


from lab7.my_library import task7_2, task7_3


def menu():
    """
    Функция предлагает выбор номера задания и номера лабораторной работы\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
             choice_lab - выбранный номер лабы
    """
    choice_task = int(input('Выберите номер задания в лабораторной работе: '))

    return choice_task

if __name__ == '__main__':
    while True:
        choice = menu()
        print('программа запустилась')


        match choice:

            case 1:
                logical_array = [True, False, True, False, True]
                new_array = task7_2(logical_array)
                print(new_array)
            case 2:

                task7_3()

            case 3:
                pass
            case _:
                break

        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break

