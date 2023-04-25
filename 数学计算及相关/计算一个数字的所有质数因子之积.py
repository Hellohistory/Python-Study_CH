def productPrimeFactors(n):
    product = 1
    for i in range(2, n+1):
        if (n % i == 0):
            isPrime = 1
            for j in range(2, int(i/2 + 1)):
                if (i % j == 0):
                    isPrime = 0
                    break
            # 如果 'i' 是质数并且是num的因子
            if (isPrime):
                product = product * i
    return product

n = int(input('请输入数字:'))
print(productPrimeFactors(n))