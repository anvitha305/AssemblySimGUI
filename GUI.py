import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
global filename
global darkMode
class AssemblySimApp(tk.Tk):
	def __init__(self, *args, **kwargs):
		global darkMode
		tk.Tk.__init__(self, *args, **kwargs)
		self.title = "legv8 assembly simulator"
		self.geometry("1000x700+200+200")
		self.style = ttk.Style(self.master)
		self.style.configure("My.TLabel", font=('Arial', 30))
		self.style.configure("Cont.TLabel", font=('Arial', 15))
		self.style.configure("TButton", font=('Arial, 20'))
		self.label1 = ttk.Label(text="File View", style="My.TLabel")
		self.label1.grid(row=0, column = 0, padx=10, pady=10)
		self.button1 = ttk.Button(text="Dark Mode", command=self.darkMode)
		self.button1.grid(row = 0, column = 1, padx=10, pady=10)
		self.button2 = ttk.Button(text="Light Mode", command=self.lightMode)
		self.button2.grid(row = 0, column = 2, padx=10, pady=10)
		self.button3 = ttk.Button(text = "Open File", command = self.browseFiles) 
		self.button3.grid(row=0, column=3,padx=10,pady=10)
		self.label2 = ttk.Label(text = "File to be simulated:", style="Cont.TLabel")
		self.label2.grid(row=1, column=0, padx=10,pady=10)
		self.label3 = ttk.Label(text="Registers View", style="My.TLabel")
		self.label3.grid(row=3, column=0,padx=10,pady=10)
		for i in range(0,8):
			self.label4 = ttk.Label(text="X"+str(i), style="Cont.TLabel")
			self.entry2 = ttk.Entry()
			self.label4.grid(row=4, column=i*2, padx=10,pady=10)
			self.entry2.grid(row=4, column=i*2+1, padx=10, pady=10)
		darkMode = False
	def darkMode(self):
		global darkMode	
		self.configure(bg='black')
		self.style.configure("TLabel", background="black",foreground="white")
		try:
			self.labelcont.configure(bg="black",fg="white")
		except Exception as e:
			pass
		darkMode = True
	def lightMode(self):
		global darkMode
		self.configure(bg='white')
		self.style.configure("TLabel", background="white", foreground="black")
		try:
			self.labelcont.configure(bg="white",fg="black")
		except Exception as e:
			pass
		darkMode = False
	def browseFiles(self):
		global darkMode
		filename = tk.filedialog.askopenfilename(initialdir = "-",title = "Select a legv8 (.s, .legv8) file to run",filetypes = (("Assembly","*.s"), ("LEGV8","*.legv8"),("All Files","*.*")))
		try:
			self.labelfile.destroy()
			self.labelcont.destroy()
		except Exception as e:
			pass
		file = open(filename)
		txt = file.read()
		file.close()
		self.labelfile = ttk.Label(text=filename, style="Cont.TLabel")
		self.labelfile.grid(row=1, column=1, columnspan=5, padx=10, pady=10)
		self.labelcont = scrolledtext.ScrolledText(wrap = tk.WORD, height = 8, font = ("Arial", 15))
		if darkMode:
			self.labelcont.configure(bg="black",fg="white")
		else:
			self.labelcont.configure(bg="white", fg="black")
		self.labelcont.grid(row=2, column=0,columnspan=6, padx=10, pady=10)
		self.labelcont.insert(tk.INSERT, txt)
		self.labelcont.configure(state="disabled")
app = AssemblySimApp()

app.mainloop()
