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

