import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("電卓")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        self.expression = ""
        
        # ディスプレイの作成
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        display_font = font.Font(family="Arial", size=24, weight="bold")
        display = tk.Entry(
            root,
            textvar=self.display_var,
            font=display_font,
            justify="right",
            bd=5,
            state="readonly"
        )
        display.pack(fill="both", padx=10, pady=10, ipady=20)
        
        # ボタンフレーム
        button_frame = tk.Frame(root)
        button_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # ボタンレイアウト
        buttons = [
            ["C", "←", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]
        
        button_font = font.Font(family="Arial", size=16, weight="bold")
        
        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                btn = tk.Button(
                    button_frame,
                    text=btn_text,
                    font=button_font,
                    command=lambda x=btn_text: self.on_button_click(x)
                )
                
                if btn_text == "=":
                    btn.config(bg="#4CAF50", fg="white")
                    btn.grid(row=row_idx, column=col_idx, columnspan=2, sticky="nsew", padx=2, pady=2)
                elif btn_text in ["C", "÷", "×", "-", "+"]:
                    btn.config(bg="#FF9800", fg="white")
                    btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=2, pady=2)
                else:
                    btn.config(bg="#E0E0E0", fg="black")
                    btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=2, pady=2)
        
        # グリッドの行と列の重みを設定
        for i in range(len(buttons)):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.display_var.set("0")
        elif char == "←":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")
        elif char == "=":
            try:
                # 表示用の演算子を計算用に変換
                calc_expr = self.expression.replace("÷", "/").replace("×", "*")
                result = eval(calc_expr)
                self.expression = str(result)
                self.display_var.set(self.expression)
            except:
                self.display_var.set("エラー")
                self.expression = ""
        else:
            self.expression += char
            self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
