import tkinter as tk
import webbrowser
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()


def Google ():  
 url = 'https://facebook.com'
 url2 = 'http://soundcloud.com'
 webbrowser.open(url)
 webbrowser.open(url2)

 label1 = tk.Label(root, text= 'Open!', fg='green', font=('helvetica', 12, 'bold'))
 canvas1.create_window(150, 200, window=label1)
    
button1 = tk.Button(text='Get Started',command=Google, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)




root.mainloop()



