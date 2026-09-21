


PROBLEMS = {

    "1.1":  dict(lab="lab1", title="Максимальная стоимость добычи", tl=2.0,  ml=256,
                 solutions=["lab1/src/1.1.py"], checker="c_1_1"),
    "1.2":  dict(lab="lab1", title="Заправки", tl=2.0, ml=256, solutions=["lab1/src/1.2.py"]),
    "1.3":  dict(lab="lab1", title="Максимальный доход от рекламы", tl=2.0, ml=256,
                 solutions=["lab1/src/1.3.py"]),
    "1.8":  dict(lab="lab1", title="Расписание лекций", tl=2.0, ml=256, solutions=["lab1/src/1.8.py"]),
    "1.10": dict(lab="lab1", title="Яблоки", tl=2.0, ml=256, solutions=["lab1/src/1.10.py"],
                 checker="c_1_10"),
    "1.11": dict(lab="lab1", title="Максимальное количество золота", tl=5.0, ml=256,
                 solutions=["lab1/src/1.11.py"]),
    "1.12": dict(lab="lab1", title="Последовательность", tl=2.0, ml=256,
                 solutions=["lab1/src/1.12.py"], checker="c_1_12"),
    "1.16": dict(lab="lab1", title="Продавец (TSP)", tl=1.0, ml=256,
                 solutions=["lab1/src/1.16.py"], checker="c_1_16"),
    "1.17": dict(lab="lab1", title="Ход конем", tl=1.0, ml=256, solutions=["lab1/src/1.17.py"]),


    "2.1":  dict(lab="lab2", title="Обход двоичного дерева", tl=5.0, ml=512,
                 solutions=["lab2/src/2.1.py"]),
    "2.5":  dict(lab="lab2", title="Простое двоичное дерево поиска", tl=2.0, ml=512,
                 solutions=["lab2/src/2.5.py"]),
    "2.6":  dict(lab="lab2", title="Опознание BST", tl=10.0, ml=512, solutions=["lab2/src/2.6.py"]),
    "2.7":  dict(lab="lab2", title="Опознание BST (усложненная)", tl=10.0, ml=512,
                 solutions=["lab2/src/2.7.py"]),
    "2.10": dict(lab="lab2", title="Проверка корректности", tl=2.0, ml=256,
                 solutions=["lab2/src/2.10.py"]),
    "2.12": dict(lab="lab2", title="Проверка сбалансированности", tl=2.0, ml=256,
                 solutions=["lab2/src/2.12.py"]),
    "2.13": dict(lab="lab2", title="Делаю я левый поворот...", tl=2.0, ml=256,
                 solutions=["lab2/src/2.13.py"], checker="c_2_13"),


    "3.1":  dict(lab="lab3", title="Лабиринт", tl=5.0, ml=512, solutions=["lab3/src/3.1.py"]),
    "3.2":  dict(lab="lab3", title="Компоненты", tl=5.0, ml=512, solutions=["lab3/src/3.2.py"]),
    "3.5":  dict(lab="lab3", title="Город с односторонним движением", tl=5.0, ml=512,
                 solutions=["lab3/src/3.5.py"]),
    "3.6":  dict(lab="lab3", title="Количество пересадок", tl=10.0, ml=512,
                 solutions=["lab3/src/3.6.py"]),
    "3.7":  dict(lab="lab3", title="Двудольный граф", tl=10.0, ml=512, solutions=["lab3/src/3.7.py"]),
    "3.9":  dict(lab="lab3", title="Аномалии курсов валют", tl=10.0, ml=512,
                 solutions=["lab3/src/3.9.py"]),
    "3.10": dict(lab="lab3", title="Оптимальный обмен валюты", tl=10.0, ml=512,
                 solutions=["lab3/src/3.10.py"]),


    "4.1":  dict(lab="lab4", title="Наивный поиск подстроки", tl=2.0, ml=256,
                 solutions=["lab4/src/4.1.py"]),
    "4.2":  dict(lab="lab4", title="Карта", tl=2.0, ml=256, solutions=["lab4/src/4.2.py"]),
    "4.3":  dict(lab="lab4", title="Паттерн в тексте (Рабин-Карп)", tl=2.0, ml=256,
                 solutions=["lab4/src/4.3.py"]),
    "4.4":  dict(lab="lab4", title="Равенство подстрок", tl=10.0, ml=512,
                 solutions=["lab4/src/4.4.py"]),
    "4.5":  dict(lab="lab4", title="Префикс-функция", tl=2.0, ml=256, solutions=["lab4/src/4.5.py"]),
    "4.6":  dict(lab="lab4", title="Z-функция", tl=2.0, ml=256, solutions=["lab4/src/4.6.py"]),
    "4.7":  dict(lab="lab4", title="Наибольшая общая подстрока", tl=15.0, ml=512,
                 solutions=["lab4/src/4.7.py"], checker="c_4_7"),
    "4.9":  dict(lab="lab4", title="Декомпозиция строки", tl=2.0, ml=256,
                 solutions=["lab4/src/4.9.py"], checker="c_4_9"),
}

LAB_ORDER = ["lab1", "lab2", "lab3", "lab4"]


def sort_key(pid):
    a, b = pid.split(".")
    return (int(a), int(b))


def all_ids():
    return sorted(PROBLEMS, key=sort_key)
