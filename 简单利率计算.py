principle = float(input("请输入本金:"))
time = int(input("请输入时间（年）:"))
rate = float(input("请输入利率:"))
simple_interest = (principle * time * rate) / 100
print("简单利息为:", simple_interest)
