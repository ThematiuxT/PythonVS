#Soldados altura diferente, ordenados, minimo numero de intercambios necesarios

fila = [4,3,5,1,2]
cambios = 0
_MEM = 0 #Variable auxiliar para hacer el cambio

for n in range(len(fila)-1):
    for i in range(len(fila)-n-1):
        j = i + 1
        if fila[i] < fila[j]:
            _MEM  = fila[i]
            fila[i] = fila[j]
            fila[j] = _MEM
            cambios = cambios + 1

print(cambios)
