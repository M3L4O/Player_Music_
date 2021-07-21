from musicas import *
from tkinter import * 
from audioplayer import AudioPlayer

lista_de_musicas = list()
global index 
index = int(0)
root = Tk()
def play():
    button['text'] = '||'
    button['command'] = pause
    if lista_de_musicas.__len__() == index + 1:
        button_forward.configure(state = DISABLED)
        if index > 0:
            button_back.configure(state = NORMAL)
    elif index == 0:
        button_back.configure(state = DISABLED)
        if lista_de_musicas.__len__() > index + 1:
            button_forward.configure(state = NORMAL)
    else:
        button_back.configure(state = NORMAL)
        button_forward.configure(state = NORMAL)
    global player
    player = AudioPlayer(lista_de_musicas[index])
    player.play()
    
def resume():
    button['text'] = '||'
    button['command'] = pause
    player.resume()

def pause():
    button['text'] = '|>'
    button['command'] = resume
    player.pause()
    
def forward():
    player.close()
    global index
    index += 1
    play()

def back():
    player.close()
    global index
    index -= index
    play()

button = Button(root, text = '|>', command = play, padx= 20 ,pady = 20, background = 'black', fg = 'lightgreen', justify='center')
button.grid(row = 1, column = 1)

button_forward = Button(root, text = '>>', command = forward, padx= 20 ,pady = 20, background = 'black', fg = 'lightgreen', justify='right')
button_forward.grid(row = 1, column = 2)

button_back = Button(root, text = '<<', command = back, padx= 20 ,pady = 20, background = 'black', fg = 'lightgreen', justify='left')
button_back.grid(row = 1, column = 0)

root.configure(width = 300, height = 300, pady = 5, padx = 5, background = 'black')

minha_imagem = PhotoImage(file='playerm.png')
canva = Canvas(root)
canva.configure(width = 300, height = 300, background = 'darkgrey')
canva.grid(row = 0, columnspan = 3, column= 0)
canva.create_image(150, 150, image = minha_imagem)


lista_de_musicas = musica()
print(lista_de_musicas.__len__())
root.mainloop()
