from tkinter import *
import random
import english_words
import time
window = Tk()
window.title("Word Bomb!")
starters = ["ab","th","en","on","or"]
word = StringVar()
randomword = random.choice(starters)
wordset = StringVar()
word.set(f'Your word contains {randomword}.')
entrylabel = Label(textvariable=word).pack()
entrytable = Entry(window,textvariable=wordset).pack()
while True:
    wordset.set(entrylabel)
    time.sleep(1)
def on_button():
    wordset.set(entrylabel)
    if randomword in wordset.get():
        print("GG")
    else:
        print("Tough luck :(")
        print(wordset.get())
buttonlabel = Button(text="Submit",command=on_button).pack()

window.mainloop()