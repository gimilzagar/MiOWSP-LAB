M = int(input("Podaj ilość strumieni ruchu M: "))
a = []
t = []
for i in range(0, M):
    a.append(int(input("podaj ruch oferowany - a"+format(i)+": ")))
    t.append(int(input("podaj ruch oferowany - t"+format(i)+": ")))
V = int(input("Podaj pojemność wiązki V: "))
n = int(input("Podaj lcizbę kanałów n: "))
xn = [1]
print(a, ";", t)
