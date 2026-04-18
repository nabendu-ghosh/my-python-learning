from tkinter import *
import random
import pandas

# Constants
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel",40,"italic")
WORD_FONT = ("Ariel",60,"bold")
CSV_FILEPATH_ORIGINAL = r"intermediate\flash_cards\data\french_words.csv"
CSV_FILEPATH_TO_LEARN = r"intermediate\flash_cards\data\words_to_learn.csv"

timer = ""
generated_word_dict = {}

# Read and Transform Data
try:
    csv_data = pandas.read_csv(filepath_or_buffer=CSV_FILEPATH_TO_LEARN)
except FileNotFoundError:
    csv_data = pandas.read_csv(filepath_or_buffer=CSV_FILEPATH_ORIGINAL)
finally:
    words_dict = csv_data.to_dict(orient="records")

# Generate Flash Card
def generate_card():

    global generated_word_dict
    global card_front_image
    global timer
    window.after_cancel(timer)
    generated_word_dict = random.choice(words_dict)
    french_word = generated_word_dict["French"]
    canvas.itemconfig(canvas_image, image= card_front_image)
    canvas.itemconfig(canvas_title, text="French", fill ="black")
    canvas.itemconfig(canvas_word, text=french_word, fill ="black")
    timer = window.after(3000, flip_card)

#Flip Flash Card

def flip_card():

    global generated_word_dict
    global card_back_image
    global timer
    english_word = generated_word_dict["English"]
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(canvas_title, text="English", fill ="white")
    canvas.itemconfig(canvas_word, text=english_word, fill ="white")
    

# Button Functions
def cross():
    generate_card()

def tick():
    words_dict.remove(generated_word_dict)
    data = pandas.DataFrame(words_dict)
    data.to_csv(path_or_buf=r"intermediate\flash_cards\data\words_to_learn.csv", index=False)
    generate_card()


# UI Design
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_image = PhotoImage(file=r"intermediate\flash_cards\images\card_front.png")
card_back_image = PhotoImage(file=r"intermediate\flash_cards\images\card_back.png")
canvas = Canvas(width=800, height=525, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 266, image=card_front_image)
canvas_title = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
canvas_word = canvas.create_text(400, 255, text="Word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

cross_button_image = PhotoImage(file=r"intermediate\flash_cards\images\wrong.png")
cross_button = Button(image=cross_button_image, highlightthickness=0, command=cross)
cross_button.grid(row=1, column=0)

tick_button_image = PhotoImage(file=r"intermediate\flash_cards\images\right.png")
tick_button = Button(image=tick_button_image, highlightthickness=0, command=tick)
tick_button.grid(row=1, column=1)

timer = window.after(3000, flip_card)
generate_card()

window.mainloop()