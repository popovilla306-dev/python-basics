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
