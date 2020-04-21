import tkinter as tk

class Calculator(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master, width = 345, height = 400,bg="pink")
		self.master = master
		self.pack()






















if __name__ == '__main__':
	root1 = tk.Tk()
	app = Calculator(master=root1)
	app.mainloop()
