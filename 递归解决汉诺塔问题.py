def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("将盘子1从", source, "移动到", destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print("将盘子", n, "从", source, "移动到", destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
