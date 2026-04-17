from tkinter import *
import random
import pandas

# Constants
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel",40,"italic")
WORD_FONT = ("Ariel",60,"bold")
CSV_FILEPATH = r"intermediate\flash_cards\data\french_words.csv"

# Read and Transform Data
csv_data = pandas.read_csv(filepath_or_buffer=CSV_FILEPATH)
words_dict = csv_data.to_dict(orient="records")

# Generate Flash Card
def generate_card():

    generated_word_dict = random.choice(words_dict)
    french_word = generated_word_dict["French"]
    english_word = generated_word_dict["English"]
    canvas.itemconfig(canvas_title, text="French")
    canvas.itemconfig(canvas_word, text=french_word)

# Button Functions
def cross():
    generate_card()

def tick():
    generate_card()

# UI Design
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_image = PhotoImage(file=r"intermediate\flash_cards\images\card_front.png")
canvas = Canvas(width=800, height=525, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 266, image=card_front_image)
canvas_title = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
canvas_word = canvas.create_text(400, 255, text="Word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

cross_button_image = PhotoImage(file=r"intermediate\flash_cards\images\wrong.png")
cross_button = Button(image=cross_button_image, highlightthickness=0, command=cross)
cross_button.grid(row=1, column=0)

tick_button_image = PhotoImage(file=r"intermediate\flash_cards\images\right.png")
tick_button = Button(image=tick_button_image, highlightthickness=0, command=tick)
tick_button.grid(row=1, column=1)

window.mainloop()