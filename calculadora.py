from tkinter import *
import customtkinter as ctk

tela = Tk()
tela.title("Calculadora")
tela.geometry("350x500")
tela.resizable(height=False, width=False)

def apertar(num):
    atual = telaResults.get()
    telaResults.delete(0, END)
    telaResults.insert(0, atual + num)

def limpar():
    telaResults.delete(0, END)

def calcular():
    try:
        expressao = telaResults.get()
        resultado = eval(expressao)
        telaResults.delete(0, END)
        telaResults.insert(0, resultado)
    except:
        telaResults.delete(0, END)
        telaResults.insert(0, "ERRO")

telaResults = Entry(tela, width=16, font=("Verdana 30"), bd=10, justify=RIGHT)
telaResults.place(x=20, y=20, width=310, height=100)

def botoes():
    botao0 = Button(tela, text="0", width=3, height=1, font=("Verdana 25"), command=lambda: apertar("0"))
    botao1 = Button(tela, text="1", width=3, height=1, font=("Verdana 25"), command=lambda: apertar("1"))
    botao2 = Button(tela, text="2", width=3, height=1, font=("Verdana 25"), command=lambda: apertar("2"))
    botao3 = Button(tela, text="3", width=3, height=1, font=("Verdana 25"), command=lambda: apertar("3"))
    botao4 = Button(tela, text="4", width=3, height=1, font=("Verdana 25"), command=lambda: apertar("4"))
    botao5 = Button(tela, text="5", width=3, height=1, font=("Verdana 25"), command=lambda: apertar("5"))
    botao6 = Button(tela, text="6", width=3, height=1, font=("Verdana 25"), command=lambda: apertar("6"))
    botao7 = Button(tela, text="7", width=3, height=1, font=("Verdana 25"), command=lambda: apertar("7"))
    botao8 = Button(tela, text="8", width=3, height=1, font=("Verdana 25"), command=lambda: apertar("8"))
    botao9 = Button(tela, text="9", width=3, height=1, font=("Verdana 25"), command=lambda: apertar("9"))
    botaoMais = Button(tela, text="+", width=3, height=1, font=("Verdana 25"), command=lambda: apertar("+"))
    botaoMenos = Button(tela, text="-", width=3, height=1, font=("Verdana 25"), command=lambda: apertar("-"))
    botaoMulti = Button(tela, text="*", width=3, height=1, font=("Verdana 25"), command=lambda: apertar("*"))
    botaoDivide = Button(tela, text="/", width=3, height=1, font=("Verdana 25"), command=lambda: apertar("/"))
    botaoIgual = Button(tela, text="=", width=3, height=1, font=("Verdana 25"), command=calcular)
    botaoLimpa = Button(tela, text="C", width=3, height=1, font=("Verdana 25"), command=limpar)

    botao0.place(x=100, y=420)
    botao1.place(x=20, y=345)
    botao2.place(x=100, y=345)
    botao3.place(x=180, y=345)
    botao4.place(x=20, y=270)
    botao5.place(x=100, y=270)
    botao6.place(x=180, y=270)
    botao7.place(x=20, y=196)
    botao8.place(x=100, y=195)
    botao9.place(x=180, y=195)
    botaoMais.place(x=20, y=420)
    botaoMenos.place(x=180, y=420)
    botaoLimpa.place(x=260, y=195)
    botaoMulti.place(x=260, y=270)
    botaoDivide.place(x=260, y=345)
    botaoIgual.place(x=260, y=420)

botoes()

tela.mainloop()