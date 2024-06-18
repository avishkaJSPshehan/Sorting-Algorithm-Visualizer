import tkinter
from tkinter import ttk
from tkinter import *
import random
import customtkinter  # <- import the CustomTkinter module
from bubbleSort import bubble_sort
from quickSort import quick_sort


root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("800x440")
root_tk.title("Sorting Algorithm Visualizer")
root_tk.configure(background='#7faceb')

data = []
algo_select = ""
speed = 0



def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1 + radius, y1,
        x1 + radius, y1,
        x2 - radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1 + radius,
        x1, y1,
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# Example usage inside drawData function
def drawData(data,colorArray):
    canvas.delete("all")
    canvas_height = 440
    canvas_width = 560
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_rect = 10
    normalised_data = [i / max(data) for i in data]

    for i, height in enumerate(normalised_data):
        x0 = i * x_width + offset + spacing_bet_rect
        y0 = canvas_height - height * 400
        x1 = (i + 1) * x_width
        y1 = canvas_width

        create_rounded_rectangle(canvas, x0, y0, x1, y1, radius=10, fill=colorArray[i])#76c7c0
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), font=("Helvetica", 10, "bold"), fill="orange")

    root_tk.update_idletasks()

def generat_button_event():
    global data
    print("Generate button pressed")
    
    try:
        minivalue = int(min_size_entry.get())
    except:
        minivalue = 1
    
    try:
        maxivalue = int(max_size_entry.get())
    except:
        maxivalue = 15

    try:
        sizeeivalue = int(input_size_entry.get())
    except:
        sizeeivalue = 10


    if minivalue < 0:
        minivalue = 0
    if maxivalue > 100:
        maxivalue = 100

    if minivalue > maxivalue:
        minivalue,maxivalue = maxivalue,minivalue

    data = []
    for _ in range(sizeeivalue):
        data.append(random.randrange(minivalue,maxivalue+1))

    drawData(data,['#76c7c0' for x in range(len(data))])


def start_button_event():
    global data
    global algo_select
    print("Alsorithm Starting...")

    if not data:
        return
    
    if algo_select == "Bubble Sort":
        bubble_sort(data,drawData,speed)
    elif algo_select == "Quick Sort":
        quick_sort(data,0,len(data)-1,drawData,speed)
        drawData(data, ['green' for x in range(len(data))])

main_heading = customtkinter.CTkLabel(master=root_tk,
                               text="S O R T I N G\nV I S U A L I Z E R",
                               width=50,
                               height=25,
                               corner_radius=8,
                               font=("TypoGraphica",20))
main_heading.place(x=27, y=30)

dark_mode_lb = customtkinter.CTkLabel(master=root_tk,
                               text="Dark Mode ",
                               width=50,
                               height=25,
                               corner_radius=8,
                               font=("TypoGraphica",12))
dark_mode_lb.place(x=5, y=90)

def switch_event():
    print(dark_mode_switch_var.get())
    if dark_mode_switch_var.get() == "on":
        customtkinter.set_appearance_mode("Light")
    else:
        customtkinter.set_appearance_mode("Dark")

dark_mode_switch_var = customtkinter.StringVar(value="on")
dark_mode_switch = customtkinter.CTkSwitch(root_tk, text="", command=switch_event,
                                 variable=dark_mode_switch_var, onvalue="on", offvalue="off")
dark_mode_switch.place(x=90,y=92)


input_size_lb = customtkinter.CTkLabel(master=root_tk,
                               text="Input Size ",
                               width=50,
                               height=25,
                               corner_radius=8,
                               font=("TypoGraphica",12))
input_size_lb.place(x=5, y=120)


input_size_entry = customtkinter.CTkEntry(master=root_tk,
                               width=200,
                               height=18,
                               corner_radius=5)
input_size_entry.place(x=10, y=145)

text = input_size_entry.get()

min_value_lb = customtkinter.CTkLabel(master=root_tk,
                               text="Min Value ",
                               width=50,
                               height=25,
                               corner_radius=8,
                               font=("TypoGraphica",12))
min_value_lb.place(x=5, y=180)

max_value_lb = customtkinter.CTkLabel(master=root_tk,
                               text="Max Value ",
                               width=50,
                               height=25,
                               corner_radius=8,
                               font=("TypoGraphica",12))
max_value_lb.place(x=110, y=180)

min_size_entry = customtkinter.CTkEntry(master=root_tk,
                               width=100,
                               height=18,
                               corner_radius=5)
min_size_entry.place(x=10, y=205)

min_value = min_size_entry.get()

max_size_entry = customtkinter.CTkEntry(master=root_tk,
                               width=100,
                               height=18,
                               corner_radius=5)
max_size_entry.place(x=110, y=205)

max_value = max_size_entry.get()


sorting_algo_lb = customtkinter.CTkLabel(master=root_tk,
                               text="Sorting Algorithm",
                               width=50,
                               height=25,
                               corner_radius=8,
                               font=("TypoGraphica",12))
sorting_algo_lb.place(x=5, y=240)

def combobox_callback(choice):

    global algo_select

    algo_select = choice
    print("combobox dropdown clicked:", choice)

sorting_algo_combobox = customtkinter.CTkComboBox(root_tk, values=["Bubble Sort", "Insertion Sort","Quick Sort","Marge Sort"],width=200,height=25,
                                     command=combobox_callback)
sorting_algo_combobox.set("Bubble Sort")

sorting_algo_combobox.place(x=10,y=265)

speed_lb = customtkinter.CTkLabel(master=root_tk,
                               text="Speed",
                               width=50,
                               height=25,
                               corner_radius=8,
                               font=("TypoGraphica",12))
speed_lb.place(x=5, y=300)

def slider_event(value):
    global speed
    speed =  float(value*1)

speed_slider = customtkinter.CTkSlider(master=root_tk,
                                 width=210,
                                 height=16,
                                 border_width=5.5,
                                 command=slider_event)
speed_slider.place(x=5,y=325)




generat_button = customtkinter.CTkButton(master=root_tk,
                                 text="Generat",
                                 command=generat_button_event,
                                 width=95,
                                 height=28,
                                 border_width=0,
                                 corner_radius=8)
generat_button.place(x=10,y=350)



start_button = customtkinter.CTkButton(master=root_tk,
                                 text="Start",
                                 command=start_button_event,
                                 width=95,
                                 height=28,
                                 border_width=0,
                                 corner_radius=8)
start_button.place(x=115,y=350)

canvas = Canvas(root_tk,width=560, height=440,bg="#e6f0f7")
canvas.place(x=240,y=0)


root_tk.mainloop()