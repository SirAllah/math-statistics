from tkinter import *
from calculation import *


class Main(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('700x850+100+40')
        self.minsize(700, 700)
        self.maxsize(850, 850)
        out = Output(self)
        Input(self, out)
        Formulas(self)



class Formulas(Label):
    def __init__(self, root):
        super().__init__(root, text="M[x] = ∑ x * p\nD[x] = M[x^2] - M[x]^2\nσ = √D")
        self.grid(row=0, column=1)


class Output(Canvas):
    def __init__(self, root):
        super().__init__(root, bg="white", width=700, height=700)
        self.grid(row=1, columnspan=2)
        
    def output_res(self, res, prob):
        DIMEN_COORDPL = 500 # dimension of the coordinate plane
        OFFSET_X = 60
        OFFSET_Y = 50
        CARDS = 32
        STEP_X = DIMEN_COORDPL / CARDS

        self.delete("all")

        self.create_text(OFFSET_X, DIMEN_COORDPL + OFFSET_Y + 60, text = res)

        self.create_line(OFFSET_X, OFFSET_Y,
                             OFFSET_X,OFFSET_Y + DIMEN_COORDPL, width=2)
        self.create_line(OFFSET_X, OFFSET_Y + DIMEN_COORDPL,
                             OFFSET_X + DIMEN_COORDPL + STEP_X, OFFSET_Y + DIMEN_COORDPL, width=2)
        
        MAXVALUE_Y = max(prob.values())
        #y / Y * DIMEN_COORDPL
        #x * STEP_X
        iter = tuple(prob)
        for i in iter:
            term_value = prob[i] / MAXVALUE_Y * DIMEN_COORDPL # hight 
            prob.update({i:term_value})
        iter = iter[:len(iter) - 1]

        self.create_text(OFFSET_X - 20, OFFSET_Y, text="%0.3f" % (MAXVALUE_Y))
        self.create_text(OFFSET_X - 20, OFFSET_Y + DIMEN_COORDPL / 2, text="%0.3f" % (MAXVALUE_Y / 2))

        for i in iter:
            self.create_text(OFFSET_X + (i-1) * STEP_X,
                                DIMEN_COORDPL + OFFSET_Y + 15,
                                text = str(i))

            self.create_line(OFFSET_X + (i-1) * STEP_X,
                                DIMEN_COORDPL + OFFSET_Y - prob[i],
                                OFFSET_X + (i) * STEP_X,
                                DIMEN_COORDPL + OFFSET_Y - prob[i + 1],
                                width=2.5, fill="red")
        else:
            self.create_text(OFFSET_X + (33) * STEP_X,
                                DIMEN_COORDPL + OFFSET_Y + 15,
                                text = str(34))


class Input(Frame):
    def __init__(self, root, out):
        super().__init__(root)
        self.out = out
        self.grid(row=0, column=0)
        self.input_num_exp()

    def input_num_exp(self):
        self.entry = Entry(self, bg="red")
        self.bat = Button(self, text = "ok", width=4, relief = FLAT)
        self.bat.bind('<Button-1>', self.click)

        self.bat.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)

    def click(self, _):
            try:
                num = int(self.entry.get())
                if num <= 0:
                    raise ValueError
                res, prob = calculation(num)
                self.out.output_res(res, prob)
                
            except ValueError:
                pass


if __name__ == "__main__":
    main = Main()
    main.mainloop()