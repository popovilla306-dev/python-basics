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
