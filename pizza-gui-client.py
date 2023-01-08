from tkinter import *
import socket
import json


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.toppings = []
        self.prices = {}

        self.host = socket.gethostbyname('LAPTOP-MKJSDQEP')
        self.port = 8685
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.data = bytes.decode(self.client.recv(1024))
        print(self.data)

        self.client.send(str.encode('p'))
        self.data = bytes.decode(self.client.recv(1024))
        self.prices = json.loads(self.data)

        self.client.send(str.encode('t'))
        self.data = bytes.decode(self.client.recv(1024))
        self.toppings = json.loads(self.data)

        self.client.send(str.encode('exit'))
        self.client.close()

        self.chk = []
        self.chkVar = list(self.toppings)
        self.size = StringVar()
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        self.lbl_title = Label(self, text='Python Pizza Calculator', font='Arial 16')
        self.lbl_title.grid(row=0, column=0, columnspan=3, sticky=W)

        self.lbl_ss = Label(self, text='Select Size:', font='Arial 13')
        self.lbl_ss.grid(row=1, column=0, sticky=W)

        self.rad_med = Radiobutton(self, text='Medium', font='Arial 13', variable=self.size, value='Medium')
        self.rad_med.grid(row=2, column=0, sticky=W)
        self.rad_large = Radiobutton(self, text='Large', font='Arial 13', variable=self.size, value='Large')
        self.rad_large.grid(row=2, column=1, sticky=W)
        self.rad_xlarge = Radiobutton(self, text='Extra Large', font='Arial 13', variable=self.size, value='XLarge')
        self.rad_xlarge.grid(row=2, column=2, sticky=W)
        # code to select default value  
        self.rad_med.select()

        self.lbl_st = Label(self, text='Select Toppings:', font='Arial 13')
        self.lbl_st.grid(row=3, column=0, columnspan=2, sticky=W)

        cur_row = 4
        for i in range(len(self.toppings)):  # (2.23...12/02)
            # this code is to store if topping is selcted or not ...1.53.00
            # it is boolean bcuz it will store if the box is checked or not checked 
            # so if true, then get or retrieve me the value of the checkbox
            # then we need to also declare it above too
            self.chkVar[i] = BooleanVar()
            self.chk.append(Checkbutton(self, text=self.toppings[i], variable=self.chkVar[i], font='Arial 13'))
            self.chk[i].grid(row=cur_row, column=0, sticky=W)
            cur_row += 1

        self.btn_reset = Button(self, text='Reset', width=12, font='Arial 13', command=self.reset)
        self.btn_reset.grid(row=cur_row, column=0, sticky=E)
        self.btn_cal = Button(self, width=12, text='Calculate Price', font='Arial 13', command=self.calc_price)
        self.btn_cal.grid(row=cur_row, column=1, sticky=W)
        cur_row += 1

        self.lbl_total = Label(self, text='Total: ', font='Arial 13')
        self.lbl_total.grid(row=cur_row, column=0, sticky=E)
        self.ent_total = Entry(self, width=10, font='Arial 13')
        self.ent_total.grid(row=cur_row, column=1, sticky=W)
        cur_row += 1

    def reset(self):
        # function to take radio button back to radio button default (i.e to reset it)
        self.rad_med.select()

        # code to reset toppings 
        for i in range(len(self.toppings)):
            self.chk[i].deselect()

        # 0 means begining (it means put in front of what is there)
        # END means at the end (it means join it to whatever is coming,)
        # code to reset total entry widget 
        self.ent_total.delete(0, END)
        self.ent_total.insert(0, '0')

    def calc_price(self):
        # get selected topping size and put it in lower case....1.50.00
        size = self.size.get().lower()

        # this 2 are created because they are needed for calculation 
        toppings_total = 0
        total = 0

        # 1.46.00... in audio
        # this code is to look through the toppings and check for the selected topping 
        for i in range(len(self.toppings)):

            # then when you see the selected one, get the price and add to total 
            if self.chkVar[i].get():
                toppings_total += self.prices[self.toppings[i].lower()]

        # this will add the size price to the toppings total prices 
        total = self.prices[size] + toppings_total

        # delete from begining to end to clear for new total 
        self.ent_total.delete(0, END)

        # insert new total 
        self.ent_total.insert(0, f'{total}')


window = Tk()
window.title("Test Application Window")
window.geometry("370x450")
app = Application(window)
app.mainloop()
