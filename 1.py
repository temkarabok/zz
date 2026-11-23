def average_grade(a, b, c):
    return (a + b + c) / 3  # считаем среднее
def grade_message(average):
    if average >= 4.5:
        return "Отлично"
    elif average >= 3.5:
        return "Хорошо"
    else:
        return "Нужно повторить материал"

res1 = average_grade(5, 4, 5)  # первый набор оценок
print(round(res1, 2), grade_message(res1))  # округляем до сотых как в примере

res2 = average_grade(3, 4, 3)  # второй набор оценок
print(round(res2, 2), grade_message(res2))