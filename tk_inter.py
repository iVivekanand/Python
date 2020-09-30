from tkinter import *
from tkinter import ttk

class HelloApp:
	def __init__(self, master):
		self.label = ttk.Label(master, text = "Hello, Tkinter")
		self.label.grid(row = 0, column = 0, columnspan = 2)

		ttk.Button(master, text = "Paris", command = self.paris_hello).grid(row = 1, column = 0)
		ttk.Button(master, text = "London", command = self.london_hello).grid(row = 1, column = 1)

	def paris_hello(self):
		self.label.config(text = "Bonjour, Tkinter")

	def london_hello(self):
		self.label.config(text = "Good day, Tkinter")

root = Tk()

def main():
	print("Starting main")
	app = HelloApp(root)
	root.mainloop()
	print("Ending main")

#if __name__ == "__main__": main()

#frame = ttk.Frame(root)
#frame.pack()
#frame.config(height = 100, width = 200)
#frame.config(relief = RIDGE)
#ttk.Button(frame, text = 'Click Me').pack()
#frame.config(padding = (30, 15))
#ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()

#root.mainloop()
checkbutton = ttk.Checkbutton(root, text = "SPAM?")
checkbutton.pack()
spam = StringVar()
spam.set("SPAM!")
spam.get()
checkbutton.config(variable = spam, onvalue = "SPAM Please!", offvalue = "Boo SPAM")
breakfast = StringVar()
ttk.Radiobutton(root, text = "SPAM", variable = breakfast, value = "SPAM").pack()
ttk.Radiobutton(root, text = "Eggs", variable = breakfast, value = "Eggs").pack()
ttk.Radiobutton(root, text = "Sausage", variable = breakfast, value = "Sausage").pack()
ttk.Radiobutton(root, text = "SPAM", variable = breakfast, value = "SPAM").pack()
checkbutton.config(textvariable = breakfast)

entry = ttk.Entry(root, width = 30)
entry.pack()
entry.state(['disabled'])
entry.state(['!disabled'])
entry.state(['readonly'])

months = StringVar()
combobox = ttk.Combobox(root, textvariable = months)
combobox.pack()

combobox.config(values = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'))
year = StringVar()
Spinbox(root, from_ = 1900, to = 2020, textvariable = year).pack()

progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)
progressbar.pack()

progressbar.config(mode = 'indeterminate')
#progressbar.start()
progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2)

value = DoubleVar()
progressbar.config(variable = value)

scale = ttk.Scale(root, orient = HORIZONTAL, length = 400, variable = value, from_ = 0.0, to = 11.0)
scale.pack()

frame = ttk.Frame(root)
frame.pack()

frame.config(height = 100, width = 200, relief = RIDGE)
ttk.Button(frame, text = 'Click Me').grid()
frame.config(padding = (30, 15))

ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()

window = Toplevel(root)
window.title('New Window')
window.lower()
window.lift(root)
window.state('zoomed')
window.state('withdrawn')
window.state('iconic')
window.state('normal')
window.state('normal')
window.iconify()
window.deiconify()
window.geometry('640x480+50+100')
window.resizable(False, False)
window.maxsize(640, 480)
window.minsize(200, 200)
window.destroy()
#root.destroy()

panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)
panedwindow.pack(fill = BOTH, expand = True)

frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)
panedwindow.add(frame1, weight = 1)
panedwindow.add(frame2, weight = 4)
frame3 = ttk.Frame(panedwindow, width = 50, height = 400, relief = SUNKEN)
panedwindow.insert(1, frame3)
panedwindow.forget(1)

notebook = ttk.Notebook(root)
notebook.pack()
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text = 'One')
notebook.add(frame2, text = 'Two')

text = Text(root, width = 40, height = 4)
text.pack()
text.config(wrap = 'word')
text.insert('1.0 + 2 lines', 'Inserted message')
text.get('1.0', 'end')
text.delete('1.0')
text.replace('1.0', '1.0 lineend', 'This is the first line')

text.tag_add('my_tag', '1.0', '1.0 wordend')
text.tag_configure('my_tag', background = 'yellow')
text.tag_remove('my_tag', '1.1', '1.3')
text.tag_delete('my_tag')

treeview = ttk.Treeview(root)
treeview.pack()
treeview.insert('', '0', 'item1', text = 'First Item')
treeview.insert('', '1', 'item2', text = 'Second Item')
treeview.insert('', 'end', 'item3', text = 'Third Item')

def callback_tv(event):
	print(treeview.selection())

treeview.bind('<<TreeviewSelect>>', callback_tv)

root.option_add('*tearOff', False)
menubar = Menu(root)
root.config(menu = menubar)
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)
menubar.add_cascade(menu = file, label = 'File')
menubar.add_cascade(menu = edit, label = 'Edit')
menubar.add_cascade(menu = help_, label = 'Help')
file.add_command(label = 'New', command = lambda: print('New file'))

file.add_separator()
file.add_command(label = 'Open...', command = lambda: print('Open file'))
file.add_command(label = 'Save', command = lambda: print('Save file'))

file.entryconfig('New', accelerator = 'Ctrl + N')

canvas = Canvas(root)
canvas.pack()
canvas.config(width = 640, height = 480)
line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5)

from tkinter import messagebox
messagebox.showinfo(title = 'Pop-up', message = 'Hello')

from tkinter import filedialog
filename = filedialog.askopenfile()
print(filename.name)

from tkinter import colorchooser
colorchooser.askcolor(initialcolor = "#FFFFFF")

root.mainloop()