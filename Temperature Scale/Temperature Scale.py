# Temperature Scale


from tkinter import *


def display():
    if 0 <= scale.get() <= 16:
        print("The temperature is", scale.get(), "degree Celsius.", "You will Freeze there..")

    elif 17 <= scale.get() <= 22:
        print("The temperature is", scale.get(), "degree Celsius.", "And its too Cold (⚈̥̥̥̥̥́⚈̥̥̥̥̥̀)")

    elif 23 <= scale.get() <= 34:
        print("The temperature is", scale.get(), "degree Celsius.", "It's Good.. And, You can Play outside. ;)")

    elif 35 <= scale.get() <= 45:
        print("The temperature is", scale.get(), "degree Celsius.", "Its very Hot!!! outside.")

    elif 46 <= scale.get() <= 60:
        print("The temperature is", scale.get(), "degree Celsius.", "You will definitely get a Skin Burn.!!!")

    elif 61 <= scale.get() <= 100:
        print("The temperature is", scale.get(), "degree Celsius.", "You will melt in there... :(")


window = Tk()

photo = PhotoImage(file="thermometer.gif")
window.iconphoto(True, photo)

window.title("Temp. Scale")

window.geometry("300x750")
window.config(bg="#1e10e3")

hot_image = PhotoImage(file="hot.gif")
hot_label = Label(window, image=hot_image)
hot_label.pack()

scale = Scale(window, from_=100, to=0,
              length=500,
              tickinterval=5,
              font=("calibri", 12),
              bg="black",
              fg="#00ff00",
              troughcolor="aqua",

              )
scale.pack()
scale.set((scale['from']-scale['to'])/2 + scale['to'])

cold_image = PhotoImage(file="cold.gif")
cold_label = Label(window, image=cold_image)
cold_label.pack()

submit_button = Button(window, text="SUBMIT", command=display, bg="#111111", fg="red",
                       font=("", 30, "bold"))
submit_button.pack()

window.mainloop()
