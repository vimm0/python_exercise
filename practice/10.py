
from Tkinter import *
class CatchGame:
	"""
	A circle in a window.
	"""
	def __init__(self, parent):
		self.canvas = Canvas(parent, width=200, height=200)
		self.canvas.grid(column=0,row=0)
		self.ball = self.canvas.create_oval(90,90,110,110,fill="blue")
		
root = Tk()
app = CatchGame(root)
root.mainloop()