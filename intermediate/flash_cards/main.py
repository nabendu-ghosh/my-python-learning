from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
# UI Design
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_image = PhotoImage(file=r"intermediate\flash_cards\images\card_front.png")
canvas = Canvas(width=800,height=525, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 266, image=card_front_image)
canvas_title = canvas.create_text(400, 150, text="Title", font=("Ariel",40,"italic"))
canvas_word = canvas.create_text(400, 255, text="Word", font=("Ariel",60,"bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_button_image = PhotoImage(file=r"intermediate\flash_cards\images\wrong.png")
cross_button = Button(image=cross_button_image, highlightthickness=0)
cross_button.grid(row=1, column=0)

tick_button_image = PhotoImage(file=r"intermediate\flash_cards\images\right.png")
tick_button = Button(image=tick_button_image, highlightthickness=0)
tick_button.grid(row=1, column=1)

window.mainloop()