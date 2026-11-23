def ticket_total(count, price=12):
    return count * price  #базовая стоимость без скидки
def final_price(count, is_school_group=False):
    total = ticket_total(count)  #вызываем первую функцию
    if is_school_group:
        return total * 0.75  #вычитаем 25% скидки
    return total
p1 = final_price(3)  #цена по умолчанию (12 руб)
print("3 обычных билета:", p1, "руб.")
p2 = final_price(4, is_school_group=True)  #передаем именованный аргумент
print("4 билета для школьной группы:", int(p2), "руб.")
p3 = ticket_total(2, price=15)  #меняем стандартную цену на 15
print("2 билета по 15 рублей:", p3, "руб.")