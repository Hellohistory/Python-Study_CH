import decimal

# ROUND_05UP模式
decimal.getcontext().rounding = decimal.ROUND_05UP

a = decimal.Decimal('2.36')
# 向上舍入到小数点后一位
a_rounded = a.quantize(decimal.Decimal('0.0'))
print("a向上舍入后的值为", a_rounded)  # 输出结果应该为2.3
