# program untuk menghitung berapa banyaknya bilangan ganjil dari 1 sampai dengan 100
R = 1
for R in range(0,100,1):
    if R % 2 == 0:
        print(F"{R}adalah bilangan ganjil ke {R//2 + 1}")