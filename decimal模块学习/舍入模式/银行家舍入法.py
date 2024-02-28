import decimal

# ROUND_HALF_EVEN模式
decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN

a = decimal.Decimal('2.35')
# 向偶数舍入到小数点后一位
a_rounded = a.quantize(decimal.Decimal('0.0'))
print("a向偶数舍入后的值为", a_rounded) # 输出结果应该为2.4

b = decimal.Decimal('2.25')
# 同样向偶数舍入到小数点后一位
b_rounded = b.quantize(decimal.Decimal('0.0'))
print("b向偶数舍入后的值为", b_rounded) # 输出结果应该为2.2
