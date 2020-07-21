import tkinter as tk

class Calculator(tk.Canvas):
	def __init__(self, master=None):
		width = 340
		height = 400
		# Initialize a frame with width 350, height 400 and the bg Pink
		super().__init__(master, width = width, height = height,bg="pink")

		self.master = master
		self.pack()
		# make the bg for the calculator
		calcWidth = 200
		calcHeight = 250
		value= 0
		x1 = (width/2) - (calcWidth/2)
		y1 = (height/2) - (calcHeight/2)
		x2 = (width/2) + (calcWidth/2)
		y2 = (height/2) + (calcHeight/2)
		self.create_rectangle(x1,y1,x2,y2)
		for x in range(int(x1), int(x2), calcWidth // 4):
			for y in range(int(y1+ 75), int(y2), int((y2 - (y1 + 75)) / 5)):
				self.makeButton (x = x ,y= y, w= 50, h= 25, value= 'MC', color='pink')	
		for value in range(0, 15,):
    			self.makeButton(x = x ,y= y, w= 50, h= 25, color='pink', value ='1'+str(value + 1))

    


	







	def makeButton(self,x,y,w,h,value,color):
		return tk.Button(self, text= value,  bg= color).place(x= x, y= y, width= w, height= h,)


		

















if __name__ == '__main__':
	root1 = tk.Tk()
	app = Calculator(master=root1)
	app.mainloop()
