
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
        text="Translate(Google)",
        font=("Helvetica", 12),
        command=lambda: translate_recipe_to_rus()
    )

    yc_translate = Button(
        frame,
        text="Translate(Yandex)",
        font=("Helvetica", 12),
        command=lambda: yc_translate()
    )
    yc_translate.pack(side="right", pady=20)
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
        current_view = view.get(1.0, END)
        view.delete(1.0, END)
        current_label = label.cget("text")
        translator = Translator()
        translated_instructions = translator.translate(current_view, dest='ru').text
        translated_label = translator.translate(current_label, dest='ru').text
        view.insert(END, translated_instructions)
        label.config(text=translated_label)

    def yc_translate():
        current_view = view.get(1.0, END)
        view.delete(1.0, END)
        current_label = label.cget("text")
        IAM_TOKEN = 't1.9euelZqRz4qNms7JlMyeis6cx5XIje3rnpWalIrGyc6cmcuaj4_Lk4yclsrl8_dOOiNJ-e8LNQNK_d3z9w5pIEn57ws1A0r9zef1656VmpOJkM7OjZfGxo3Mzc-ZlceV7_zF656VmpOJkM7OjZfGxo3Mzc-ZlceV.Ink5ZHMkxurcoR-8Go73VQxUWUDkOtUXnU1bxfYdHZ4jjLlnJjK80p_Ni1Vow3qXHDlhxPRYE9F0s_YZ7ZklCA'
        folder_id = 'b1gdr5mlfac2i8am95j9'
        target_language = 'ru'
        texts = current_view
        texts_label = current_label

        body = {
            "targetLanguageCode": target_language,
            "texts": texts,
            "folderId": folder_id,
        }
        body_label = {
            "targetLanguageCode": target_language,
            "texts": texts_label,
            "folderId": folder_id,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(IAM_TOKEN)
        }

        response_view = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                                 json=body,
                                 headers=headers
                                 )
        response_label = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                                      json=body_label,
                                      headers=headers
                                      )
        yc_response_view = response_view.json()
        yc_response_view_text = yc_response_view['translations'][0]['text']

        yc_response_label = response_label.json()
        yc_response_label_text = yc_response_label['translations'][0]['text']

        view.insert(END, yc_response_view_text)
        label.config(text=yc_response_label_text)

    Tk.mainloop(frame)