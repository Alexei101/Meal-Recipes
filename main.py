
import requests
import json
from tkinter import *


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
        command=lambda: printRecipe()
    )

    button.pack(pady = 20)

    def printRecipe():
        view.delete(1.0, END)
        response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
        ans = response.json()
        recipe_instructions = ans['meals'][0]['strInstructions']
        print(recipe_instructions)
        view.insert(END, recipe_instructions)
        label.config(text=ans['meals'][0]['strMeal'])


    Tk.mainloop(frame)