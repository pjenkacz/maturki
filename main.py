import math
handle = open('punkty.txt', 'r')
def is_prime(num):
    if num <=1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False

    return True


wsp_A = list()
wsp_B = list()
liczba1 = list()
zad_4_1 = 0
liczba2 = list()




for line in handle:
    line = line.rstrip()
    liczby = line.split()
    liczba1.append(sorted(liczby[0]))
    liczba2.append(sorted(liczby[1]))
    wsp_A.append(liczby[0])
    wsp_B.append(liczby[1])
    if is_prime(int(liczby[0])) and is_prime(int(liczby[1])):
        zad_4_1 +=1
posortowane_liczba1 = list()
posortowane_liczba2 = list()
licznik_4_2 = 0
pomocnicza = list()
pomocnicza2 = list()

bufor = ''
for x in liczba1:
    for i in range(0,len(x)):
        if i == 0 :
            pomocnicza.append(x[0])
            continue
        if(x[i] != x[i-1]):
            pomocnicza.append(x[i])
    #print('przed: ', liczba1[help], ' po: ', pomocnicza)
    for j in range(len(pomocnicza)):
        bufor += pomocnicza[j]
    posortowane_liczba1.append(bufor)
    bufor = ''
    pomocnicza.clear()

for x in liczba2:
    for i in range(0,len(x)):
        if i == 0 :
            pomocnicza.append(x[0])
            continue
        if(x[i] != x[i-1]):
            pomocnicza.append(x[i])

    for j in range(len(pomocnicza)):
        bufor += pomocnicza[j]
    posortowane_liczba2.append(bufor)
    bufor = ''
    pomocnicza.clear()

for k in range(len(posortowane_liczba1)):
    print(k+1, ' --1: ', posortowane_liczba1[k], ' --2:', posortowane_liczba2[k])
    if posortowane_liczba1[k] == posortowane_liczba2[k]:
        print("BINGO")
        licznik_4_2 =+1

max_odleglosc = -2
wewnatrz_kwadratu = 0
zewnatrz_kwadratu = 0
na_kwadracie = 0


for k in range(len(wsp_A)):
    xa = int(wsp_A[k])
    ya = int(wsp_B[k])

    if (xa <5000 and xa > -5000) and (ya <5000 and ya >-5000):
        wewnatrz_kwadratu +=1
    elif xa > 5000 or xa < - 5000 or ya > 5000 or ya < -5000:
        zewnatrz_kwadratu +=1
    else:
        na_kwadracie+=1
    for h in range(k + 1, len(wsp_A)):
        yb = int(wsp_B[h])
        xb = int(wsp_A[h])
        xx = xb - xa
        yy = yb - ya
        dl = math.sqrt( ( pow(xx,2) ) + ( pow(yy,2) ) )
        if dl > max_odleglosc:
            max_odleglosc = dl

print('ZADANIE 4_1',zad_4_1)
print('ZADANIE 4_2',licznik_4_2)
print('ZADANIE 4_3',round(max_odleglosc))
print("WEWNATRZ KWADRATU:" , wewnatrz_kwadratu, ' ZEWNATRZ KWADDRATU: ', zewnatrz_kwadratu, ' W SRODKU', na_kwadracie)