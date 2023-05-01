# 导入必要的模块
import cv2

# QR码解码器

# 输入图像的文件名
filename = input('请输入图片地址:')

# 读取图像
image = cv2.imread(filename)

# 创建QR码检测器
detector = cv2.QRCodeDetector()

# 解码图像中的QR码
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

# 如果QR码被检测到，则打印出解码后的数据
if vertices_array is not None:
    print(data)
