import json
import requests
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("320x320")
root.title("Vreme")
root.configure(bg='white')

lable_0 = Label(root, text="Vreme", width=20, bg='white', font=("bold", 20), fg='brown')
lable_0.place(x=0, y=93)

city_names = StringVar()
entry_1 = Entry(root, textvariable=city_names)
city_names.set("Vnesi mesto ...")
entry_1.place(x=102, y=140)

lable_2 = Label(root, text="Temparatura : ", width=20, bg='white', font=("bold", 10), fg='blue')
lable_2.place(x=62, y=220)

lable_3 = Label(root, text="Pritisk : ", width=20, bg='white', font=("bold", 10), fg='blue')
lable_3.place(x=62, y=240)



lable_temp = Label(root, text="...", width=5, bg='white', font=("bold", 10), fg='blue')
lable_temp.place(x=192, y=220)

lable_pres = Label(root, text="...", width=5, bg='white', font=("bold", 10), fg='blue')
lable_pres.place(x=192, y=240)




def getTemp():
    api_key = "<cf1cf47b12ba5ea83221345ee5452526>"
    base_url =("http://api.weatherstack.com/current?access_key=d8a4e4add5cab312ead864ead48dcdd9&query=")
    city_name = entry_1.get()
    complete_url = base_url +  city_name

    response = requests.get(complete_url)
    x = response.json()

    if ["cod"] != '404':
        y = x
        current_temprature = y["current"]["temperature"]
        current_pressure = y["current"]["pressure"]


        z = x
        weather_description = z

        lable_pres.configure(text=current_pressure)
        lable_temp.configure(text=current_temprature)
        
    else:
        lable_pres.configure(text="Err")
        lable_temp.configure(text="Err")
        lable_desc.configure(text="Err")


Button(root, text="Potrdi", width=10, bg='brown', fg='white', command=getTemp).place(x=122, y=170)

lable_unit = Label(root, text="Temparatura je v  stopinjah in pritisk je v  mb", width=35, bg='white', font=("bold", 10),
                   fg='brown')
lable_unit.place(x=22, y=290)

mainloop()
