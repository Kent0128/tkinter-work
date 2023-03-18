import tkinter as tk

class calculator:
    # 創建窗口
    def __init__(self,a):
        self.a=a
        self.a.title("計算器")
        self.create_board()
        
    def create_board(self):
        # 輸入欄
        self.entry=tk.Entry(self.a, width=30, justify="right", font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # 按鈕
        button_1 = tk.Button(self.a, text="1", padx=40, pady=20, command=lambda: self.button_click(1))
        button_2 = tk.Button(self.a, text="2", padx=40, pady=20, command=lambda: self.button_click(2))
        button_3 = tk.Button(self.a, text="3", padx=40, pady=20, command=lambda: self.button_click(3))
        button_4 = tk.Button(self.a, text="4", padx=40, pady=20, command=lambda: self.button_click(4))
        button_5 = tk.Button(self.a, text="5", padx=40, pady=20, command=lambda: self.button_click(5))
        button_6 = tk.Button(self.a, text="6", padx=40, pady=20, command=lambda: self.button_click(6))
        button_7 = tk.Button(self.a, text="7", padx=40, pady=20, command=lambda: self.button_click(7))
        button_8 = tk.Button(self.a, text="8", padx=40, pady=20, command=lambda: self.button_click(8))
        button_9 = tk.Button(self.a, text="9", padx=40, pady=20, command=lambda: self.button_click(9))
        button_0 = tk.Button(self.a, text="0", padx=40, pady=20, command=lambda: self.button_click(0))
        button_add = tk.Button(self.a, text="+", padx=40, pady=20, command=self.button_add)
        button_subtract = tk.Button(self.a, text="一",padx=40, pady=20, command=self.button_subtract)
        button_multiply = tk.Button(self.a, text="*", padx=40, pady=20, command=self.button_multiply)
        button_divide = tk.Button(self.a, text="/", padx=40, pady=20, command=self.button_divide)
        button_equal = tk.Button(self.a, text="=", padx=40, pady=20, command=self.button_equal)
        button_clear = tk.Button(self.a, text="C", padx=40, pady=20, command=self.button_clear)
        button_point = tk.Button(self.a, text=".", padx=40, pady=20, command=lambda: self.button_click("."))

        #UI
        button_1.grid(row=3, column=0)
        button_2.grid(row=3, column=1)
        button_3.grid(row=3, column=2)
        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)
        button_7.grid(row=1, column=0)
        button_8.grid(row=1, column=1)
        button_9.grid(row=1, column=2)
        button_0.grid(row=4, column=0)
        button_point.grid(row=4 ,column=1)
        button_clear.grid(row=4, column=2)
        button_add.grid(row=5, column=0)
        button_subtract.grid(row=6, column=0)
        button_multiply.grid(row=5, column=1)
        button_divide.grid(row=6, column=1)
        button_equal.grid(row=5, column=2,rowspan=2)


    # 按鈕函數
    def button_click(self,number):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        final=str(current) + str(number)
        if final.count(".")>=2:
            self.entry.insert(0, "ERROR")
        else:
            self.entry.insert(0, final)

    def button_clear(self):
        self.entry.delete(0, tk.END)#從第一個string 刪到 最後一個 string 位置

    def button_add(self):
        first_number = self.entry.get()
        global f_num
        global math
        math = "addition"
        f_num = float(first_number)
        self.entry.delete(0, tk.END)

    def button_subtract(self):
        first_number = self.entry.get()
        global f_num
        global math
        math = "subtraction"
        f_num = float(first_number)
        self.entry.delete(0, tk.END)

    def button_multiply(self):
        first_number = self.entry.get()
        global f_num
        global math
        math = "multiplication"
        f_num = float(first_number)
        self.entry.delete(0, tk.END)

    def button_divide(self):
        first_number = self.entry.get()
        global f_num
        global math
        math = "division"
        f_num = float(first_number)
        self.entry.delete(0, tk.END)

    def button_equal(self):
        second_number = self.entry.get()
        self.entry.delete(0, tk.END)

        if math == "addition":
            self.entry.insert(0, f_num + float(second_number))

        if math == "subtraction":
            self.entry.insert(0, f_num - float(second_number))

        if math == "multiplication":
            self.entry.insert(0, f_num * float(second_number))

        if math == "division":
            self.entry.insert(0, f_num / float(second_number))
