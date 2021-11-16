
# 1


def suma(*args,**kwargs):
    rez = 0
    for i in args:
        if type(i) == int:
            rez +=1
    return rez
print(suma(1, 5, 7, 'a', [0, 'e', [0, 6, 't']], 'ab'))

#      3

print(suma())

#      0

print(suma(1, 2, valoare1 = 23))

#      2


# 2


def afis(a, b, c):
    print(a)
    print(b)
    print(c)

def suman(n): #suma integrala
    if n == 0:
        return n
    else:
        return n + suman(n-1)

def sumap(n): #suma nr pare
    rez = 0
    for i in range(n):
        if i % 2 == 0:
            rez += i
    return rez

def sumai(n): #suma nr impare
    rez = 0
    for i in range(n):
        if i % 2 == 1:
            rez += i
    return rez

n=int(input("Introduceti valoarea dorita: "))
afis(suman(n), sumap(n), sumai(n))


#                         SAU


def suman(n):
    if n == 0:
        return (0, 0, 0)
    rez1, rez2, rez3 = suman(n - 1)
    if n % 2 == 0:
        rez2 += n
    else:
        rez3 += n
    rez1 += n
    tuplu_u = (rez1, rez2, rez3)
    return tuplu_u
print(suman(6))

# (21, 12, 9)

print(suman(7))

# (28, 12, 16)


# 3


def intreg_nr(n=int(input("Introduceti valoarea lui n: "))):
    if type(n) == int:
        return n
    else:
        return(0)
print(intreg_nr())


#                  SAU


def intreg_nr(numar):
    try:
        vrf = int(numar)
        print(numar)
    except ValueError as e:
        print("0")
intreg_nr(input("Introduceti valoarea: "))