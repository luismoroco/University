from matplotlib import pyplot as plt

with open("out.txt") as file_in:
    tam = [] 
    first = []
    second = []
    for line in file_in:
        [a, b, c] = line.split()
        tam.append(a) 
        first.append(b)
        second.append(c)


plt.plot(tam, first, label='Primer Bucle')
plt.plot(tam, second, label='Segundo Bucle')
plt.title(f'Primer vs Segundo Bucle Cap 2.2 Memoria Caché')
plt.xlabel('Tamaño de Matriz')
plt.ylabel('Tiempo')
plt.legend()
plt.show()
