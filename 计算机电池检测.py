# 导入sys库，用于退出程序
import sys
# 导入platform库，用于获取当前操作系统信息
import platform
# 导入traceback库，用于打印异常信息
import traceback
# 导入plyer库中的notification模块，用于发送通知
from plyer import notification
# 导入psutil库，用于获取电池相关信息
import psutil

# 检查当前操作系统是否为Windows
if platform.system() != 'Windows':
    print('抱歉，此程序只能在Windows操作系统上运行')
    sys.exit(1)

try:
    # 获取电池相关信息
    battery = psutil.sensors_battery()
    percent = battery.percent
    charging = battery.power_plugged

    # 根据电池状态确定提示消息
    if charging:
        if percent == 100:
            charging_message = "请拔掉充电器"
        else:
            charging_message = "正在充电"
    else:
        charging_message = "未充电"

    # 组装通知消息
    message = f"{percent}% 已充电\n{charging_message}"

    # 发送通知
    notification.notify(title="电池信息", message=message, timeout=10)
except psutil.Error as e:
    print(f"获取电池状态时出错: {e}")
except ModuleNotFoundError as e:
    print(f"无法导入外部库: {e}")
except Exception:
    traceback.print_exc()
    print("程序发生了未知错误")
