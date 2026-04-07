from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=20,pady=20)

def convert():
    km_converted = float(miles_entry.get()) * 1.6
    converted_km_label.config(text=km_converted)

miles_entry = Entry()
miles_entry['width'] = 10
miles_entry.grid(column=3,row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=4,row=1)

equal_label = Label(text="is equal to")
equal_label.grid(column=1,row=2)

converted_km_label = Label(text="0")
converted_km_label.grid(column=3,row=2)

km_label = Label(text="Km")
km_label.grid(column=4,row=2)

convert_button = Button(text="Convert",command=convert)
convert_button.grid(column=3,row=3)

window.mainloop()