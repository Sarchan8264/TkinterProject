from tkinter import *

win = Tk()
win.title("BMI Calculator")
win.minsize(350, 250)
win.config(padx=10, pady=10)



def Calculate():
    height=entry_height.get()
    weight=entry_weight.get()
    if height == "" or weight == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number!")

"""""
#BMI_Categoria
under 18.5-Under Weight-Minimal
18.5-24.9 -Normal Weight-Minimal
25-29.9- OverWeight - Increased
30-34.9 - Obese-High
35-39.9-Severly Obese-Very High
40 and over"Morbidly Obese-Extremely High"
"""
BMI_label = Label(win, text="BMI Calculator", font=("Bold", 15, "bold"))
BMI_label.pack()

Entry_weight = Label(win, text="Enter You weight(kg):", font=("Times New Roman", 12, "bold"))
Entry_weight.pack()

entry_weight = Entry(width=22)
entry_weight.pack()

Entry_height = Label(win, text="Enter You height(cm):", font=("Times New Roman", 12, "bold"))
Entry_height.pack()

entry_height = Entry(width=22)
entry_height.pack()

Calculate_Button = Button(text="Calculate", width=15,command=Calculate)
Calculate_Button.pack()
result_label = Label()
result_label.pack()
def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 18.5:
        result_string += "Under Weight!"
    elif 18.5 < bmi <= 24.9:
        result_string += "Normal Weight!"
    elif 25 < bmi <= 29.9:
        result_string += "OverWeight!"
    elif 30 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 34.9:
        result_string += "obese class 1"
    elif 35 < bmi <= 39.9:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string

win.mainloop()
