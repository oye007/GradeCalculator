from tkinter import *
import myModule

root = Tk()
root.title("Students Grade Calculator")

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

        # display error messages if any
        error_text.set("")

        # display result
        total_text.set(results["total"])
        average_text.set(results["average"])
        percentage_text.set(results["percentage"])
        grade_text.set(results["grade"])

    else:
        # display error messages
        error_text.set(inputStatus["errorMsg"])


def handleButtonClear():
    #clear results and error messages
    error_text.set("")
    total_text.set("")
    average_text.set("")
    percentage_text.set("")
    grade_text.set("")


# Build program GUI with TKinter

mainFrame = LabelFrame(root, padx=20, pady=20)
mainFrame.pack(padx=30, pady=30)


frame = Label(mainFrame, padx=50, pady=50)
frame.pack(side=LEFT, padx=30, pady=30)

instructionlabel = Label(frame, text="Enter 5 scores", fg="blue").grid(row=0, column=0)
instructionlabelMargin = Label(frame, text="").grid(row=1, column=0)

scoreAlabel = Label(frame, text="Score A").grid(row=2, column=0)
e1 = Entry(frame, width=20)
e1.grid(row=2, column=1, padx=10, pady=10)

scoreBlabel = Label(frame, text="Score B").grid(row=3, column=0)
e2 = Entry(frame, width=20)
e2.grid(row=3, column=1, padx=10, pady=10)

scoreClabel = Label(frame, text="Score C").grid(row=4, column=0)
e3 = Entry(frame, width=20)
e3.grid(row=4, column=1, padx=10, pady=10)

scoreDlabel = Label(frame, text="Score D").grid(row=5, column=0)
e4 = Entry(frame, width=20)
e4.grid(row=5, column=1, padx=10, pady=10)

scoreElabel = Label(frame, text="Score E").grid(row=6, column=0)
e5 = Entry(frame, width=20)
e5.grid(row=6, column=1, padx=10, pady=10)

space2 = Label(frame, text="").grid(row=7, column=0)

CalcButton = Button(frame, text="Calculate Grade", padx=10, pady=5, command=handleButtonClick, bg="blue", fg="white").grid(row=8, column=1)


OutputFrame = LabelFrame(mainFrame, padx=50, pady=50, bg="white")
OutputFrame.pack(side=RIGHT)

error_text = StringVar()
ErrorMsg = Label(OutputFrame, textvariable=error_text, fg="red", bg="white").grid(row=0, column=0)

TotalLabel = Label(OutputFrame, text="Total Marks:",  bg="white").grid(row=1, column=0)
total_text = StringVar()
TotalResult = Label(OutputFrame, bg="white", textvariable=total_text).grid(row=1, column=1)

AverageLabel = Label(OutputFrame, text="Average Mark:",  bg="white").grid(row=2, column=0)
average_text = StringVar()
AverageResult = Label(OutputFrame, bg="white", textvariable=average_text).grid(row=2, column=1)

PercentageLabel = Label(OutputFrame, text="Percentage:",  bg="white").grid(row=3, column=0)
percentage_text = StringVar()
PercentageResult = Label(OutputFrame, bg="white", textvariable=percentage_text).grid(row=3, column=1)

GradeLabel = Label(OutputFrame, text="Grade:",  bg="white").grid(row=4, column=0)
grade_text = StringVar()
GradeResult = Label(OutputFrame, bg="white", textvariable=grade_text).grid(row=4, column=1)

space = Label(OutputFrame, bg="white").grid(row=5, column=0)

ClearButton = Button(OutputFrame, text="Clear Result", padx=10, pady=5, command=handleButtonClear).grid(row=6, column=0)


root.mainloop()