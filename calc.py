import tkinter as tk

def mink():
	print("manamejeff!!")

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.hi_there = tk.Button(self)
		self.hi_there["text"] = "World of Gumpshy\n(Enter Now)"
		self.hi_there["command"] = self.changeColor("red")
		self.hi_there["bg"] = "red"
		self.hi_there["fg"] = "black"
		self.hi_there.pack(side="top")

		self.blue = tk.Button(self, text="Blue", fg="black", bg="blue", 
			command=self.changeColor("blue"))
		self.blue.pack(side="top")

		self.quit = tk.Button(self, text="QUIT", fg="black",
			command=self.master.destroy)
		self.quit.pack(side="bottom")

	def changeColor(self, col):
		print(col)
		self.configure(bg=col)
		# print(self.bg)

root1 = tk.Tk()
app = Application(master=root1)
app.mainloop()

 #2 buttons 1 red 1 blue 1 says red on it other says blue on it
	#click the red back becomes red blue back becomes blue
