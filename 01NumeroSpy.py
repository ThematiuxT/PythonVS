min = int(input("Inferior (a): ")) #100
max = int(input("Superior (b): ")) #150

spies = []

for i in range(min,max+1,1):
    suma = 0
    mult = 1
    for x in str(i):
        suma = suma + int(x)
        mult = mult * int(x)
    if suma == mult:
        spies.append(i)

print(f"Hay {len(spies)} numeros espia entre {min} y {max}")
for spy in spies:
    print(spy)
