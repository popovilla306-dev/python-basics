name_shop: str = "GGshop"
MAX_QUANTITY = 100
prices={"Minecraft":900,
        "GTA V":1200,
        "chiken gan":12000,
        "Terraria":700,
        }
print(f"Вітаємо у нашому магазині {name_shop}")
user_name=input("Введіть ваше ім'я:")
print("Раді бачити вас,",user_name)
print("Доступні товари:")
print("Minecraft")
print("GTA V")
print("chiken gan")
print("Terraria")
product = input("Виберіть товар:", )
quantity = int(input("Вкажіть кількість товару:", ))
if product in prices and quantity > 0 and quantity <= MAX_QUANTITY:
     price = (prices[product])
     total = (price * quantity)
     print("Ціна вибраного вами товару:", price, "грн")
     print(f"Загальна сума: {total} грн")
else:
     print("Помилка")
     exit()
average_total=total/quantity
#додавання знижки
discount=0
if total>=3000:
     discount=0.15
elif total>=2000:
     discount=0.10
else:
     discount=0
has_discount=discount>0
if has_discount:
    if discount==0.15:
        print("Велика знижка 15%!")
    else:
        print("Знижка 10%")
else:
    print("Знижки немає")
subtotal_discount=total*discount
total_discount=total-subtotal_discount
text_discount= "Є знижка" if has_discount else "Без знижки"
print("Ціна зі знижкою:",total_discount)
payment=input("Виберіть тип оплати: (cash/card)",).lower()
if not (payment=="cash" or payment=="card"):
    print("Будь ласка виберіть інший спосіб оплати")
    exit()
match payment:
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