import base64

# 定义加密函数
def encrypt(message):
    message_bytes = message.encode('ascii') # 将消息转换为字节
    base64_bytes = base64.b64encode(message_bytes) # 对字节进行base64编码
    base64_message = base64_bytes.decode('ascii') # 将编码后的字节转换为字符串
    return base64_message

# 定义解密函数
def decrypt(base64_message):
    try:
        base64_bytes = base64_message.encode('ascii') # 将字符串转换为字节
        message_bytes = base64.b64decode(base64_bytes) # 对字节进行base64解码
        message = message_bytes.decode('ascii') # 将解码后的字节转换为字符串
        return message
    except:
        return "无效的输入，无法解密"

# 主函数
def main():
    mode = input("请选择模式：加密（E）/解密（D）:")
    if mode == "E":
        message = input("请输入需要加密的消息:")
        encrypted_message = encrypt(message)
        print("加密后的消息:", encrypted_message)
    elif mode == "D":
        base64_message = input("请输入需要解密的消息:")
        decrypted_message = decrypt(base64_message)
        print("解密后的消息:", decrypted_message)
    else:
        print("无效的模式选择")

if __name__ == '__main__':
    main()

