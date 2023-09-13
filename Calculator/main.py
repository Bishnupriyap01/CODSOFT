import tkinter as tk

ORANGE = "#d6644d"
PINK = "#95db9e"
BLUE = "#30d0db"
GRAY = "#f2d0ee"
WHITE_LBL = "#73185e"
FONT_ONE = ("Arial", 40, "bold")
FONT_TWO = ("Arial", 16)
FONT_DIGITS = ("Comic Sans MS", 24, "bold")
FONT_DEFAULT = ("Arial", 20)


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("378x500")
        self.window.resizable(0, 0)

        self.window.title("Calculator")

        self.total = ""
        self.current = ""
        self.display_frame = self.create_displayframe()

        self.total_label, self.label = self.create_displaylabels()

        self.digit = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.key_bind()

    def key_bind(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digit:
            self.window.bind(str(key), lambda event, digit=key: self.expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_displaylabels(self):
        total_label = tk.Label(self.display_frame, text=self.total, anchor=tk.E, bg=GRAY,
                               fg=WHITE_LBL, padx=24, font=FONT_TWO)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current, anchor=tk.E, bg=GRAY,
                         fg=WHITE_LBL, padx=24, font=FONT_ONE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_displayframe(self):
        frame = tk.Frame(self.window, height=201, bg=GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def expression(self, value):
        self.current += str(value)
        self.update_label()

    def digit_buttons(self):
        for digit, grid_value in self.digit.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=PINK, fg=WHITE_LBL, font=FONT_DIGITS,
                               borderwidth=0, command=lambda x=digit: self.expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current += operator
        self.total += self.current
        self.current = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=ORANGE, fg=WHITE_LBL, font=FONT_DEFAULT,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current = ""
        self.total = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=ORANGE, fg="red", font=FONT_DEFAULT,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current = str(eval(f"{self.current}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=ORANGE, fg=WHITE_LBL, relief="groove",
                           font=FONT_DEFAULT,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.current = str(eval(f"{self.current}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=ORANGE, fg=WHITE_LBL, relief="raised",
                           font=FONT_DEFAULT,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total += self.current
        self.update_total_label()
        try:
            self.current = str(eval(self.total))

            self.total = ""
        except Exception as e:
            self.current = "Error"
        finally:
            self.update_label()

    def equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=BLUE, fg=WHITE_LBL, font=FONT_DEFAULT,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()

