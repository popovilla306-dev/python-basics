 case ("cash"):
        print("Оплата готівкою")
    case "card":
        print("Оплата картою")
    case _:
        print("Невідомий спосіб оплати")
#чек, має показувати : товар;кількість;ціну за 1 штуку;знижку;кінцеву суму;спосіб оплати.
print("-------------------------------------------")
print(f"Товар: {product}")
print(f"Кількість: {quantity}")
print(f"Ціна за одиниці товару: {average_total}грн")
print(f"Статус:{text_discount}")
print(f"Знижка: {discount*100}% ({subtotal_discount} грн) ")
print(f"До сплати:{total_discount:.2f}")
print(f"Спосіб оплати:{payment}")
print("------------------------------------------")
input("натисніть ENTER щоб вийти ")
