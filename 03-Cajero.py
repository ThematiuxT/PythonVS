cant = int(input("Cantidad $: "))
bills = {}
tbills = 0
for den in [500,200,100,50,20,10,5,1]:
    bills[str(den)] = 0
    while cant >= den:
        cant = cant - den
        bills[str(den)] = bills[str(den)] + 1
        tbills = tbills + 1


print(f"Se necesitan {tbills} en total")
for val,bill in bills.items():
    if bill > 0:
        print(f"{bill} de {val}")
