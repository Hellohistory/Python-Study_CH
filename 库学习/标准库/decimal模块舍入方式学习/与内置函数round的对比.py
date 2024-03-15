# coding=utf-8
import decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN

a = decimal.Decimal('2.35')
a_rounded = a.quantize(decimal.Decimal('0.0'))
print("a向偶数舍入后的值为", a_rounded)  # 应该输出2.4

b = decimal.Decimal('2.25')
b_rounded = b.quantize(decimal.Decimal('0.0'))
print("b向偶数舍入后的值为", b_rounded)  # 应该输出2.2

# 内置round函数
c = round(2.35, 1)
print("c使用round函数舍入后的值为", c)  # 应该是2.4

d = round(2.25, 1)
print("d使用round函数舍入后的值为", d)  # 应该是2.2
