def prog0():
    from random import randint
    rand_list=[]
    n=5
    for i in range(n):
        rand_list.append(randint(1,9))

    a = int(input("Введите число:"))
    if a in rand_list:
        print("Вы угадали число",a)
        print("Общий список",rand_list)
    else:
        print("Вы не угадали")
        print("Общий список", rand_list)
def prog1():
    from random import randint
    from collections import Counter
    a = []
    n = 10
    for i in range(n):
        a.append(randint(1, 9))
    c = Counter(a)
    print(c)

def prog2():
    a = ("пн", "вт", "ср", "чт", "пт", "сб", "вс")
    w = int(input("Сколько выходных"))
    print("Выходные дни", a[:-w-1:-1])
    print("Рабочие дни", a[:-w ])
def prog3():
    import random
    one = ['Иванов', 'Ц', 'У', 'К','Е', 'Н', 'Г', 'Ш', 'Щ','З']
    two = ['Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж']
    one_two = (random.sample(one,5) + random.sample(two,5))
    print(one)
    print(two)
    print(one_two)
    print('Len:', len(one_two))
    one_two = tuple(sorted(one_two))
    if 'Иванов' in one_two:
        print(one_two.count('Иванов'))
    else:
        print('Не выходит ')
prog3()