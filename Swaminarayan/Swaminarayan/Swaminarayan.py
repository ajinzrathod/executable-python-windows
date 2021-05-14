import tkinter as Tkinter


def main():
	top = Tkinter.Tk()

	top.geometry("500x500")
	B = Tkinter.Button(top, text ="Hello")

	B.pack()
	top.mainloop()


if __name__ == '__main__':
	main()