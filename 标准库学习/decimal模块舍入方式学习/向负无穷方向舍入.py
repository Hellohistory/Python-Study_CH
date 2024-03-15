import decimal

# ROUND_FLOOR模式
decimal.getcontext().rounding = decimal.ROUND_FLOOR

a = decimal.Decimal('2.39')
# 向下舍入到小数点后一位
a_rounded = a.quantize(decimal.Decimal('0.0'))
print("a向下舍入后的值为", a_rounded)  # 输出结果应该为2.3
