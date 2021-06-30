import tkinter as tk
LIGHT_GREY = "#F5F5F5"
LABEL_COLOR = "#25265E"
SMALL_FONT_SIZE = ("Arial",16)
LARGE_FONT_STYLE = ("Arial",40,"bold")
WHITE = "#FFFFFF"
LIGHT_BLUE= "#CCEDFF"
OFF_WHITE = "#F8FAFF"
DIGITS_FONT_STYLE=("Arial",24,"bold")
DEFAULT_FONT_STYLE=("Arial",20)

class Calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("375x567")
        self.window.resizable(0,0)
        self.window.title("Nidhy's Calculator")
        self.total_exp = ""
        self.current_exp =""
        self.display_frame= self.create_display_frame()
        self.total_label,self.label=self.create_display_label()
        self.button_frame= self.create_button_frame()
        self.digits={
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), '.':(4,1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)
        self.create_digit_button()
        self.create_operator_button()
        self.create_special_button()

    def create_special_button(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_sqrt_button()
        self.create_square_button()

    def create_display_label(self):
        total_label = tk.Label(self.display_frame,text=self.total_exp,
                             anchor=tk.E, bg=LIGHT_GREY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_SIZE)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_exp,
                               anchor=tk.E, bg=LIGHT_GREY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill="both")

        return total_label , label

    def create_display_frame(self):
        frame=tk.Frame(self.window,height=221,bg=LIGHT_GREY)
        frame.pack(expand=True, fill="both")
        return  frame

    def add_to_exp(self, value):
        self.current_exp += str(value)
        self.update_label()

    def create_digit_button(self):
        for digit,grid_value in self.digits.items():
            button=tk.Button(self.button_frame,
                             text=str(digit), bg=WHITE, fg=LABEL_COLOR,
                             font=DIGITS_FONT_STYLE, borderwidth=0,command=lambda x=digit: self.add_to_exp(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self,operator):
        self.current_exp += operator
        self.total_exp += self.current_exp
        self.current_exp = " "
        self.update_total_label()
        self.update_label()




    def create_operator_button(self):
        i=0
        for operator,symbol in self.operations.items():
            button=tk.Button(self.button_frame, text=symbol,
                             bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4,sticky=tk.NSEW)
            i+=1

    def clear(self):
        self.current_exp = " "
        self.total_exp = " "
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="Clear",
                           bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_exp=str(eval(f"{self.current_exp} **2"))
        self.update_label()


    def create_square_button(self):
        button = tk.Button(self.button_frame, text="x\u00b2",
                           bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)


    def sqrt(self):
        self.current_exp= str(eval(f"{self.current_exp} **0.5"))
        self.update_label()


    def create_sqrt_button(self):
        button = tk.Button(self.button_frame, text="\u221ax",
                           bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)



    def evaluate(self):
        self.total_exp += self.current_exp
        self.update_total_label()
        self.current_exp = str(eval(self.total_exp))
        self.total_exp = " "
        self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.button_frame, text="=",
                           bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)


    def create_button_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(expand=True,fill="both")
        return frame

    def update_total_label(self):
        self.total_label.config(text=self.total_exp)


    def update_label(self):
        self.label.config(text=self.current_exp[:11])
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc=Calculator()
    calc.run()