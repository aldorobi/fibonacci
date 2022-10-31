from tkinter import *
root = Tk()

root.title("fibonacci")
root.geometry("500x500")

serie = Label(root,text = "serie de fibonachos")
flaw = Label(root)
spiral = Label(root)

def fibonacci():
    num = 10
    primero = 0
    segundo = 1
    suma = 0
    contador = 1
    while(contador <= num):
        serie["text"]+= str(suma)+ " "
        contador = contador + 1
        primero = segundo
        segundo = suma
        suma = primero + segundo
        flaw["text"]= "los conejos estan cansados"
        spiral["text"]= "los espirales derechos son :" + str(primero) + "\n los espirales izquierdos son :" + str(segundo)
boton = Button(root,command=fibonacci,text ="mostrar")

boton.pack()
serie.pack()
spiral.pack()
flaw.pack()

root.mainloop()