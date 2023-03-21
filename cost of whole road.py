from tkinter import BOTTOM, Button, Frame, Menu, Tk, Label, Entry


class Window(Frame):
    def __init__(self, master, width="500", height="400"):
        Frame.__init__(self, master)
        self.master = master
        self.master.geometry(f"{width}x{height}")

        self.label_km = Label(master, text=" how many km", font = 'calibri 15 bold', foreground = 'red')
        self.label_km.pack()
        self.input_km = Entry(master)
        self.input_km.pack()

        self.label_combustion = Label(master, text="average fuel consumption ", font = 'calibri 15 bold', foreground = 'blue')
        self.label_combustion.pack()
        self.input_combustion = Entry(master)
        self.input_combustion.pack()   

        self.label_price = Label(master, text=" price of 1 liter of fuel", font = 'calibri 15 bold', foreground = 'orange')
        self.label_price.pack()
        self.input_price = Entry(master)
        self.input_price.pack()  

        self.button_calkulate = Button(master, text="calculation", command=self.calculate_price)
        self.button_calkulate.pack()

        self.button_reset = Button(master, text="reset", command=self.reset_input)
        self.button_reset.pack()

        self.label_summary = Label(master, text=" sumary", font = 'calibri 15 bold', foreground = 'green')
        self.label_summary.pack()

    def calculate_price(self):
        km = int(self.input_km.get())
        combustion = int(self.input_combustion.get())
        price = int(self.input_price.get())

        cost=(km/100)*combustion*price

        self.label_summary.config(text=cost)

    def reset_input(self):
        self.input_km.delete(0, last=len(self.input_km.get()))
        self.input_combustion.delete(0, last=len(self.input_combustion.get()))
        self.input_price.delete(0, last=len(self.input_price.get()))
        self.label_summary.config(text="")

def main():
    root = Tk()
    Window(root)
    root.wm_title("My Price")
    root.mainloop()


if __name__ == "__main__":
    main()