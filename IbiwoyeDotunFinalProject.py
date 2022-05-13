from tkinter import *
from PIL import ImageTk,Image
import myModule

root = Tk()
root.title("Students Grade Calculator")
root.iconbitmap("metro.ico")

# initialize String Variables
global error_text, total_text, average_text, percentage_text, grade_text
error_text = StringVar()
total_text = StringVar()
average_text = StringVar()
percentage_text = StringVar()
grade_text = StringVar()

def handleButtonClick():
    # Retrieve inputs
    scores = {
        "scoreA": e1.get(),
        "scoreB": e2.get(),
        "scoreC": e3.get(),
        "scoreD": e4.get(),
        "scoreE": e5.get()
    }
    # validate inputs and retrieve error messages if any
    inputStatus = myModule.validateInputs(scores)

    if (inputStatus["error"] == False):
        # calculate grade
        results = myModule.Calculator(scores)

        # clear error messages
        error_text.set("")

        # display result
        total_text.set(results["total"])
        average_text.set(results["average"])
        percentage_text.set(results["percentage"])
        grade_text.set(results["grade"])
        openResults(results["grade"])

    else:
        # display error messages
        error_text.set(inputStatus["errorMsg"])
        openResults("error")


def handleButtonClear():
    #clear results and error messages
    error_text.set("")
    total_text.set("")
    average_text.set("")
    percentage_text.set("")
    grade_text.set("")


# Function to open result window
def openResults(msg):
    # initialize Toplevel window
    top = Toplevel(padx=50, pady=50, bg="white")
    top.title("Result")

    # initialize Image frame
    ImgFrame = Label(top)
    ImgFrame.pack(side=TOP)

    global my_img
    # Display icons according to arguments
    if (msg == "error"):
        my_img = ImageTk.PhotoImage(Image.open("error.png"))
    if (msg == "A"):
        my_img = ImageTk.PhotoImage(Image.open("a.png"))
    if (msg == "B"):
        my_img = ImageTk.PhotoImage(Image.open("b.png"))
    if (msg == "C"):
        my_img = ImageTk.PhotoImage(Image.open("c.png"))
    if (msg == "D"):
        my_img = ImageTk.PhotoImage(Image.open("d.png"))
    if (msg == "E"):
        my_img = ImageTk.PhotoImage(Image.open("e.png"))

    my_label = Label(ImgFrame, image=my_img, bg="white")
    my_label.pack()

    # initialize Result frame
    OutputFrame = Label(top, padx=20, pady=20, bg="white")
    OutputFrame.pack(side=BOTTOM, padx=30, pady=30)

    ErrorMsg = Label(OutputFrame, textvariable=error_text, fg="red", bg="white").grid(row=0, column=0)

    TotalLabel = Label(OutputFrame, text="Total Marks:",  bg="white").grid(row=1, column=0)
    TotalResult = Label(OutputFrame, bg="white", textvariable=total_text).grid(row=1, column=1)

    AverageLabel = Label(OutputFrame, text="Average Mark:",  bg="white").grid(row=2, column=0)
    AverageResult = Label(OutputFrame, bg="white", textvariable=average_text).grid(row=2, column=1)

    PercentageLabel = Label(OutputFrame, text="Percentage:",  bg="white").grid(row=3, column=0)
    PercentageResult = Label(OutputFrame, bg="white", textvariable=percentage_text).grid(row=3, column=1)

    GradeLabel = Label(OutputFrame, text="Grade:",  bg="white").grid(row=4, column=0)
    GradeResult = Label(OutputFrame, bg="white", textvariable=grade_text).grid(row=4, column=1)

    space = Label(OutputFrame, bg="white").grid(row=5, column=0)

    ClearButton = Button(OutputFrame, text="Close", padx=10, pady=5, bg="red", fg="white", command=top.destroy).grid(row=7, column=0)




# Build program GUI with TKinter

mainFrame = LabelFrame(root, padx=50, pady=50)
mainFrame.pack(padx=30, pady=30)


# frame = Label(mainFrame, padx=50, pady=50)
# frame.pack(side=LEFT, padx=30, pady=30)

instructionlabel = Label(mainFrame, text="Enter 5 scores", fg="blue").grid(row=0, column=0)
instructionlabelMargin = Label(mainFrame, text="").grid(row=1, column=0)

scoreAlabel = Label(mainFrame, text="Score A").grid(row=2, column=0)
e1 = Entry(mainFrame, width=20)
e1.grid(row=2, column=1, padx=10, pady=10)

scoreBlabel = Label(mainFrame, text="Score B").grid(row=3, column=0)
e2 = Entry(mainFrame, width=20)
e2.grid(row=3, column=1, padx=10, pady=10)

scoreClabel = Label(mainFrame, text="Score C").grid(row=4, column=0)
e3 = Entry(mainFrame, width=20)
e3.grid(row=4, column=1, padx=10, pady=10)

scoreDlabel = Label(mainFrame, text="Score D").grid(row=5, column=0)
e4 = Entry(mainFrame, width=20)
e4.grid(row=5, column=1, padx=10, pady=10)

scoreElabel = Label(mainFrame, text="Score E").grid(row=6, column=0)
e5 = Entry(mainFrame, width=20)
e5.grid(row=6, column=1, padx=10, pady=10)

space2 = Label(mainFrame, text="").grid(row=7, column=0)

CalcButton = Button(mainFrame, text="Calculate Grade", padx=10, pady=5, command=handleButtonClick, bg="blue", fg="white").grid(row=8, column=1)


# OutputFrame = LabelFrame(mainFrame, padx=50, pady=50, bg="white")
# OutputFrame.pack(side=RIGHT)

root.mainloop()