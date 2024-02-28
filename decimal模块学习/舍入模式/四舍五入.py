import decimal

# ROUND_HALF_UP模式
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

a = decimal.Decimal('22.5')
# 四舍五入到整数
a_rounded = a.to_integral_value()
print("a四舍五入后的值为", a_rounded)  # 输出结果应该为23

b = decimal.Decimal('6.542')
# 四舍五入到小数点后两位
b_rounded = b.quantize(decimal.Decimal('0.00'))
print("b四舍五入后的值为", b_rounded)  # 输出结果应该为6.54
