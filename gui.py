from tkinter import *
from calculation import *


class Diagram():
    def __init__(self):
        self.OFFSET_X = 60
        self.OFFSET_Y = 50
        self.root = Tk()
        self.root.minsize(700, 700)
        self.root.maxsize(850, 850)

        self.root.geometry('700x700')

        self.canv = Canvas(self.root, bg="white", width=700, height=700)
        self.canv.pack()

    def input_num_exp(self):
        self.entry = Entry(self.canv, bg="red")
        self.bat = Button(self.canv, text = "ok", width=3)
        self.bat.bind('<Button-1>', self.click)

        self.canv.create_window(10,10,window=self.bat)
        self.canv.create_window(90,10,window=self.entry)

    def click(self, _):
            self.canv.delete("all")
            self.canv.create_window(10,10,window=self.bat)
            self.canv.create_window(90,10,window=self.entry)
            try:
                num = int(self.entry.get())
                if num <= 0:
                    raise ValueError
                res, prob = calculation(num)
                self.output_res(res, prob)
            except ValueError:
                pass

    def output_res(self, res, prob):
        DIMEN_COORDPL = 500 # dimension of the coordinate plane
        OFFSET_X = self.OFFSET_X
        OFFSET_Y = self.OFFSET_Y
        self.prob = prob
        self.res = res
        STEP_X = DIMEN_COORDPL / 32 # 32 is number of cards

        self.canv.create_text(OFFSET_X, DIMEN_COORDPL + OFFSET_Y + 50, text = self.res)

        self.canv.create_line(OFFSET_X, OFFSET_Y,
                             OFFSET_X,OFFSET_Y + DIMEN_COORDPL, width=2) 
        self.canv.create_line(OFFSET_X, OFFSET_Y + DIMEN_COORDPL,
                             OFFSET_X + DIMEN_COORDPL + STEP_X, OFFSET_Y + DIMEN_COORDPL, width=2)
        
        MAXVALUE_Y = max(self.prob.values())
        #y / Y * DIMEN_COORDPL
        #x * STEP_X
        iter = tuple(self.prob)
        for i in iter:
            term_value = self.prob[i] / MAXVALUE_Y * DIMEN_COORDPL # hight 
            self.prob.update({i:term_value})
        # for y to value
        iter = iter[:len(iter) - 1]


        self.canv.create_text(OFFSET_X - 20, OFFSET_Y, text="%0.3f" % (MAXVALUE_Y))
        self.canv.create_text(OFFSET_X - 20, OFFSET_Y + DIMEN_COORDPL / 2, text="%0.3f" % (MAXVALUE_Y / 2))

        for i in iter:
            self.canv.create_text(OFFSET_X + (i-1) * STEP_X,
                                DIMEN_COORDPL + OFFSET_Y + 15,
                                text = str(i))

            self.canv.create_line(OFFSET_X + (i-1) * STEP_X,
                                DIMEN_COORDPL + OFFSET_Y * 2  - (OFFSET_Y + self.prob[i]),
                                OFFSET_X + (i) * STEP_X,
                                DIMEN_COORDPL + OFFSET_Y * 2 - (OFFSET_Y + self.prob[i + 1]),
                                width=2.5, fill="red")
        else:
            self.canv.create_text(OFFSET_X + (33) * STEP_X,
                                DIMEN_COORDPL + OFFSET_Y + 15,
                                text = str(34))

        
    

if __name__ == "__main__":
    dia = Diagram()
    dia.input_num_exp()
    dia.root.mainloop()

