# 9.2开始使用
from tkinter import *

"""
def lesson9_2():

    window = Tk()
    # 创建一个窗口
    label = Label(window, text="Welcom to Python")
    button = Button(window, text="Click Me")
    label.pack()
    button.pack()
    window.mainloop()
"""

# 9.3处理事件
# 一个Tkinter构建可以与一个函数绑定，当事件发生时被调用

"""
def processOK():
    print("OK button is ckicked")


def processCancel():
    print("Cancel button is clicked")


window = Tk()
btOK = Button(window, text="OK", fg="red", command=processOK)
btCancel = Button(window, text="Cancel", bg="yellow", command=processCancel)
btOK.pack()
btCancel.pack()
window.mainloop()
"""
# 也可以将所有函数放在一个类中来编写这个程序
"""
class ProcessButtonEvent:
    def __init__(self):
        window = Tk()

    btOK = Button(window, text="OK", fg="red", command=processOK)
    btCancel = Button(window, text="Cancel", bg="yellow", command=processCancel)
    btOK.pack()
    btCancel.pack()
    window.mainloop()

    def processOK(self):
        print("OK button is cliked")

    def procseeCancel(self):
        print("Cancel BUtton is cliked")
ProcessButtonEvent()
"""

"""
class WidgetsDemo:
    def __init__(self):
        window = Tk()
        window.title("Widgets Demo")

        frame1 = Frame(window)
        frame1.pack()
        self.v1 = IntVar()
        cbtBold = Checkbutton(
            frame1, text="Bold", variable=self.v1, command=self.processCheckbutton
        )
        self.v2 = IntVar()
        rbRed = Radiobutton(
            frame1,
            text="Red",
            bg="red",
            variable=self.v2,
            value=1,
            command=self.processRadiobutton,
        )
        rbYellow = Radiobutton(
            frame1,
            text="Yellow",
            bg="yellow",
            variable=self.v2,
            value=2,
            command=self.processRadiobutton,
        )
        cbtBold.grid(row=1, column=1)
        rbRed.grid(row=1, column=2)
        rbYellow.grid(row=1, column=3)
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text="Enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable=self.name)
        btGetName = Button(frame2, text="Get Name", command=self.processButton)
        message = Message(frame2, text="It is a widgets demo")
        label.grid(row=1, column=1)
        entryName.grid(row=1, column=2)
        btGetName.grid(row=1, column=3)
        message.grid(row=1, column=4)

        text = Text(window)
        text.pack()
        text.insert(END, "Tip\nThe best way to learn Tkinter is to read")
        text.insert(END, "these carefully designed examoles and use them")
        text.insert(END, "to creat your applications")
        window.mainloop()

    def processCheckbutton(self):
        print("check button is" + "checked" if self.v1.get() == 1 else "unchecked")

    def processRadiobutton(self):
        print("Red" if self.v2.get() == 1 else "Yellow")

    def processButton(self):
        print("Your name is " + self.name.get())


WidgetsDemo()
"""
# 改变标签颜色，字体，和内容
from tkinter import *


class ChangeLabelDemo:
    def __init__(self) -> None:
        window = Tk()
        window.title("Change Label Demo")

        frame1 = Frame(window)
        frame1.pack()
        self.lbl = Label(frame1, text="Programming is fun")
        self.lbl.pack()

        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text="Enter text: ")
        self.msg = StringVar()
        entry = Entry(frame2, textvariable=self.msg)
        btChangeText = Button(frame2, text="change text", command=self.processButton)
        self.v1 = StringVar()
        rbRed = Radiobutton(
            frame2,
            text="Red",
            bg="red",
            variable=self.v1,
            value="R",
            command=self.processRadiobutton,
        )
        rbYellow = Radiobutton(
            frame2,
            text="Yellow",
            bg="Yellow",
            variable=self.v1,
            value="Y",
            command=self.processRadiobutton,
        )

        label.grid(row=1, column=1)
        entry.grid(row=1, column=2)
        btChangeText.grid(row=1, column=3)
        rbRed.grid(row=1, column=4)
        rbYellow.grid(row=1, column=5)

        window.mainloop()

    def processRadiobutton(self):
        if self.v1.get() == "R":
            self.lbl["fg"] = "red"
        elif self.v1.get() == "Y":
            self.lbl["fg"] == "yellow"

    def processButton(self):
        self.lbl["text"] = self.msg.get()


ChangeLabelDemo()
