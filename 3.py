def analyze_scores(*scores):
    if len(scores) == 0: #проверка, если ничего не передали
        return 0, 0, 0
    s = sum(scores)
    c = len(scores)
    avg = s / c
    return s, c, avg #возвращаем сразу три значения
def print_report(team_name, **info):
    print("Команда:", team_name)
    for k, v in info.items(): #перебираем переданные характеристики
        print(k, "-", v)
print("Для (8, 10, 7, 9):", analyze_scores(8, 10, 7, 9))
print("Для (5, 5):", analyze_scores(5, 5))
print("Без аргументов:", analyze_scores())
print() #пустая строка для разделения
print_report("Комета", coach="Алексей", city="Минск", rank=1) #вызов с именованными аргументами