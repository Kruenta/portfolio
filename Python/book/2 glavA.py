# 2.1 A Составить программу
import math

x = 1
y = (17 * (x ** 2)) - (6 * x) + 13
print(y)

# 2.1 B Составить программу

a = 2
y1 = (3 * (a ** 2)) + (5 * a) - 21
print(y1)

# 2.2 Составить программу вычисления значения функции

a1 = 2
y2 = ((a1 ** 2) + 10) / math.sqrt((a1 ** 2) + 1)
print(y2)

# 2.3 a Составить программу:

a2 = 3
y3 = math.sqrt(((2 * a2) + math.sin(3 * a2)) / 3.56)
print(y3)

# 2.3 б Составить программу:

x1 = 2
y4 = math.sin((3.2 + math.sqrt(1 + x1)) / 5 * x1)
print(y4)

# 2.4 Дана сторона квадрата. Найти его периметр.

a = 2
P = 4 * a
print("Периметр квадрата: ", P)

# 2.5 Дан радиус окружности. Найти ее диаметр

s = 5
d = math.sqrt(4 * s / math.pi)
print('Диаметр: ', '%.2f' % d)
print('Длина: ', '%.2f' % (d * math.pi))

# 2.6 Считая, что Земля  – идеальная сфера с  радиусом R ≈
# 6350  км, определить расстояние до линии горизонта от точки
# с  заданной высотой над Землей.

r = 6350
h = 10
d = math.sqrt(h * ((2 * r) + h))

#  r = 6350
#  h = 10
#  d = ((R+h)**2-R**2)**0.5

print(d)

# 2.7 Дана длина ребра куба. Найти объем куба и  площадь его
# боковой поверхности.

a = 2
v = a * a * a
s1 = 4 * (a ** 2)
print(v, s1)

# 2.8 Дан радиус окружности. Найти длину окружности и  площадь круга
r1 = 3
l = 3 * math.pi
s2 = (l ** 2) / (4 * math.pi)
s3 = math.pi * (r1 ** 2)
print(l, s2, s3)

# 2.9 a Составить программу:

x2 = 2
y5 = 2
z = (2 * (x2 ** 3)) - (3.44 * x2 * y5 + 2.3 * (x2 ** 2)) - (7.1 * y5) + 2
print(z)

# 2.9 б Составить программу:

a3 = 2
b = 2
x5 = 3.14 * ((a3 + b) ** 3) + (2.75 * (b ** 2)) - (12.7 * a3) - 4.1
print(x)

# 2.10 a Даны два целых числа. Найти:
# а) их среднее арифметическое;
# б) их среднее геометрическое.

a4 = 5
a44 = 6
SredA = (a4 + a44) / 2
print(SredA)

# 2.10 б

g = 5
g1 = 6
SredG = math.sqrt(g * g1)
print(SredG)

# 2.11 Известны объем и масса тела. Определить плотность материала этого тела

V1 = 10
M = 14
rho = M / V1
print(rho)

# 2.12 Известны количество жителей в  государстве и  площадь
# его территории. Определить плотность населения в  этом государстве.

p = 719
ns = 5312400
Human = ns / p
print(Human)

# 2.13 Составить программу решения линейного уравнения
# ax + b = 0 (a ≠ 0).

a21 = 2
x = 0
b = 0
y6 = a21 * x + b
print(y6)

# 2.14 Даны катеты прямоугольного треугольника. Найти его
# гипотенузу.

a22 = 5
b1 = 5
p1 = a22 + b1
c = math.sqrt((a22 ** 2) + (b1 ** 2))
p2 = p1 + c
print(p1, c, p2)

# 2.15 Найти площадь кольца по заданным внешнему и  внутреннему радиусам.

r1 = 5
R1 = 6
Square = (math.pi * R1 * R1) - (math.pi * r1 * r1)
print(Square)

# 2.16 Даны катеты прямоугольного треугольника. Найти его
# периметр

a25 = 3
b25 = 4
print("Катет 1: ", a25)
print("Катет 2: ", b25)
c25 = math.sqrt(a25 ** 2 + b25 ** 2)
P25 = a25 + b25 + c25
print("Гипотенуза: ", c25)
print("Периметр: ", P25)

# 2.17 Даны основания и  высота равнобедренной трапеции.
# Найти ее периметр.

a217 = 8
b217 = 6
h217 = 8
S217 = (a217 + b217) * h217 / 2.0
P217 = a217 + b217 + 2 * (h217 ** 2 + (a217 - b217) ** 2 / 4) ** 0.5
print(u"Площадь равнобедренной трапеции равна = {}".format(S217))
print(u"Периметр равнобедренной трапеции равен = {}".format(P217))

# 2.18 Составить программу вычисления значений функций

x218 = 5
y218 = 5
z218 = (x218 + ((2 + y218) / (x218 ** 2))) / (y218 + (1 / (math.sqrt((x218 ** 2) + 10))))
q218 = 7.25 * math.sin(x218) - abs(y218)
print(z218, q218)

# 2.19 Составить программу расчета значения функций

a219 = 3
b219 = 7
x219 = (2 / ((a219 ** 2) + 25) + b219) / (math.sqrt(b219) + ((a219 + b219) / 2))
y219 = (abs(a219) + (2 * math.sin(b219))) / (5.5 * a219)

print(x219, y219)

# 2.20 Составить программу расчета значения функций

e220 = 5
f220 = 8
g220 = 23
h220 = 3
a220 = math.sqrt(abs(e220 - (3 / f220)) + g220)
b220 = math.sin(e220) + math.cos(h220) ** 2
c220 = (33 * g220) / ((e220 * f220) - 3)

print(a220, b220, c220)

# 2.21 Составить программу расчета значения функций

e221 = 5
f221 = 8
g221 = 23
h221 = 3

a221 = ((e221 + (f221 / 2)) / 3)
b221 = abs((h221 ** 2) - g221)
c221 = math.sqrt(((g221 - h221) ** 2) - 3 * math.sin(e221))

print(a221, b221, c221)

# 2.22 Даны два числа. Найти среднее арифметическое и  среднее геометрическое их модулей.

a222 = 35
a2221 = 36
SredA222 = (a4 + a44) / 2
print(abs(SredA222))

# 2.22 б

g222 = 35
g2221 = 36
SredG222 = math.sqrt(g * g1)
print(abs(SredG222))

# 2.23 	 Даны стороны прямоугольника. Найти его периметр
# и длину диагонали.

a223 = 5
b223 = 5
p223 = 2 * a223 + 2 * b223
q223 = math.sqrt((a223**2) + (b223**2))
print(p223, q223)

# 2.24 Даны два числа. Найти их сумму, разность, произведение,
# а также частное от деления первого числа на второе.

a224 = 57
b224 = 5
sum = a224 + b224
raz = a224 - b224
ymn = a224 * b224
dele = a224 / b224
print(sum, raz, ymn, dele)


# 2.25 Даны длины сторон прямоугольного параллелепипеда.
# Найти его объем и  площадь боковой поверхности.

a225 = 28
b225 = 35
c225 = 67
V225 = a225 * b225 * c225
P225 = 2 * (a225 * b225 + a225 * c225 + b225 * c225)
print(V225, P225)


# 2.26 Даны координаты на плоскости двух точек.
# Найти расстояние между этими точками.

x226x, x226x1 = 5, 8
y226y, y226y1 = 2, 9

ab226 = math.sqrt(((x226x1-x226x)**2) + ((y226y1 - y226y)**2))

print(ab226)

# 2.27.	 Даны основания и  высота равнобедренной трапеции.
# Найти периметр трапеции.

--------------------------------

#