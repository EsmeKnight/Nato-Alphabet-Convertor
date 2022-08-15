from tkinter import *
import pandas as pd

nato_alphabet_csv = pd.read_csv("NatoAlphabetConverter/nato_phonetic_alphabet.csv")

# use list comprehension to create dicitonary from csv data frame
nato_alphabet = {row.letter: row.code for (index, row) in nato_alphabet_csv.iterrows()}


# use list comprehension to get desired result
def nato_converter():
    user_input = to_be_converted_entry.get().upper()
    # user_input = input("Text to be converted: ").upper()
    user_input = [*user_input]
    try:
        nato_conversion = [nato_alphabet[char] for char in user_input]
    except KeyError:
        output_entry.insert(
            chars="Please only convert letters in the alphabet", index=1.0
        )
    else:
        # print(nato_conversion)
        output_entry.insert(chars=", ".join(nato_conversion), index=1.0)


# nato_converter()


# UI
# window
window = Tk()
window.title("Nato Text Convertor")
window.config(padx=20, pady=20)
window.minsize(
    width=320, height=150
)  # minsize is 240 to account for the 20 padding on each side

# label
to_be_converted_label = Label(text="To be converted:")
to_be_converted_label.grid(column=0, row=1, sticky=E)
output = Label(text="Output:")
output.grid(column=0, row=2, sticky=E)

# entries
to_be_converted_entry = Entry()
to_be_converted_entry.grid(column=1, row=1)
# focus conversion entry
to_be_converted_entry.focus()

output_entry = Text(width=22, height=5)
output_entry.grid(column=1, row=2, columnspan=2)

# button
convert_button = Button(text="Convert", command=nato_converter)
convert_button.grid(column=2, row=1)


# functions as a while loop to keep window open
window.mainloop()
