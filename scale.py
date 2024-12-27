from tkinter import *
window= Tk()
def Submit():
    print("THE TEMPERATURE IS "+ str(scale.get())+" Degree")
hot_image= PhotoImage(file='fire1.png').subsample(20,20)
hotLabel=Label(image=hot_image)
hotLabel.pack()
scale=Scale(window,from_=100,to=0,font='Arial',
            orient=VERTICAL,
            length=600,
            width=40,
            tickinterval=10,
            showvalue=0,
            fg='Black',
            bg='white',
            resolution=5,
            
            )
scale.pack()
scale.set(50)

cool_image= PhotoImage(file='cool1.png').subsample(15,15)
coollabel=Label(image=cool_image)
coollabel.pack()

button=Button(window,text='submit',command=Submit)
button.pack()
window.mainloop()