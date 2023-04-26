import re
import calendar
import datetime
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(
            self, text="请输入日期:", font=("微软雅黑", 15)
        )
        self.label.pack(pady=10)

        self.user_input = tk.Entry(self, font=("微软雅黑", 15), bg="white", fg="black")
        self.user_input.pack(pady=10)

        self.check_button = tk.Button(
            self,
            text="查询",
            font=("微软雅黑", 15),
            fg="white",
            bg="black",
            command=self.show_day,
        )
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(self, font=("微软雅黑", 15))
        self.result_label.pack(pady=10)

    def process_date(self, user_input):
        user_input = re.sub(r"/", "-", user_input)  # 用-替换/
        user_input = re.sub(r"\s", "-", user_input)  # 用-替换空格
        return user_input

    def show_day(self):
        date = self.user_input.get()
        try:
            date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            self.result_label.config(text="日期格式不正确，请重新输入")
            return

        day = calendar.day_name[date_obj.weekday()]  # 获取星期几的名称
        year, month, day = date.split("-")
        result_text = f"{year}年{month}月{day}日是{day}"
        self.result_label.config(text=result_text)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400+100+100")
    app = Application(master=root)
    app.mainloop()
