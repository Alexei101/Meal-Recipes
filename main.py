
import requests

from tkinter import *

#from Tools.demo.spreadsheet import translate
from googletrans import Translator

if __name__ == '__main__':

    window = Tk()
    window.title("Recipes")
    window.geometry("800x600")


    frame = Frame(
        window,
        padx=10,
        pady=10
    )
    frame.pack(expand=True)
    frame.grid(rows=8, columns = 8)

    label = Label (
        frame,
        text="Name of meal",
        font = ("Helvetica", 18, "bold"), anchor = "center"
    )
    label.pack(pady= 10)

    view = Text(
        frame,
        font = ("Helvetica", 12), wrap = "word", padx = 10, pady = 10
    )
    #view.grid(row=4, column=4)
    view.pack(padx = 10, pady = 10)

    button = Button(
        frame,
        text="Get Recipe",
        font=("Helvetica", 12),
        command=lambda: print_recipe()
    )


    buttonTranslate = Button (
        frame,
        text="Translate",
        font=("Helvetica", 12),
        command=lambda: translate_recipe_to_rus()
    )
    buttonTranslate.pack(side = "right", padx = 20)
    button.pack(side="right", pady = 20)
    def print_recipe():
        view.delete(1.0, END)
        response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
        ans = response.json()
        recipe_instructions = ans['meals'][0]['strInstructions']

        #print(recipe_instructions)
        view.insert(END, recipe_instructions)
        label.config(text=ans['meals'][0]['strMeal'])


    def translate_recipe_to_rus():
        v = view.get(1.0, END)
        view.delete(1.0, END)
        translator = Translator()
        translated_instructions = translator.translate(v, dest='ru').text
        view.insert(END, translated_instructions)


    Tk.mainloop(frame)