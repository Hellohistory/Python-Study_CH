import numpy as np

# 生成测试信号
t = np.linspace(0, 1, 1000, endpoint=False)
x = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*20*t)

# 计算傅里叶变换
y = np.fft.fft(x)

# 计算频率域
freqs = np.fft.fftfreq(len(x), t[1]-t[0])

# 输出结果
print("频率域：", freqs)
print("幅度谱：", np.abs(y))
print("相位谱：", np.angle(y))