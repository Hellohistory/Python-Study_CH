import numpy as np
from scipy.fft import fft

# 定义一个信号
t = np.linspace(0, 1, 1000, endpoint=False)
y = np.sin(2*np.pi*5*t) + np.sin(2*np.pi*10*t) + np.sin(2*np.pi*20*t)

# 计算傅里叶变换
Y = fft(y)

# 计算频率轴
freqs = np.fft.fftfreq(len(y), t[1]-t[0])

# 打印结果
for freq, mag in zip(freqs, np.abs(Y)):
    print(f"频率为 {freq:.2f} 的幅值为 {mag:.2f}")