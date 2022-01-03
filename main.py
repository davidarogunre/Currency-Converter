import tkinter as tk
from tkinter import *
import requests
from tkinter import Label,Entry, Button, StringVar, ttk
class CurrencyConverter():
    def __init__(self):
        response = requests.get("http://data.fixer.io/api/latest?access_key=7dee11ee097837ffddb970bad28db4d6")
        r=response.json()
        self.rates=r['rates']
        self.currlist =[]
    def getkeys(self):
        for key in self.rates.keys():
            self.currlist.append(key)
        self.currlist.append('EUR')
    def convert(self, fromcurrency, fromcurrvalue, to_currency, tocurrvalue):
        curr_str1 = fromcurrency.get()
        curr_str2 = to_currency.get()
        if curr_str1 == 'EUR':
            amount = float(self.rates[curr_str2])
            amount = float(amount) * float(fromcurrvalue)
            amount = round(amount,2)
            tocurrvalue.delete(0,END)
            tocurrvalue.insert(0,amount)
        elif curr_str2 == "EUR":
            amount = float(self.rates[curr_str1])
            amount = float(fromcurrvalue)/float(amount)
            amount = round(amount,2)
            tocurrvalue.delete(0,END)
            tocurrvalue.insert(0,amount)
        else:
            baseamount = float(self.rates[curr_str1])
            amount = float(fromcurrvalue)/baseamount
            amount = amount*float(self.rates[curr_str2])
            amount = round(amount, 2)
            tocurrvalue.delete(0,END)
            tocurrvalue.insert(0,amount)
       
class CurrencyConverterUI(tk.Tk):
    def  __init__(self, converter):
        self.currency_converter = converter
        tk.Tk.__init__(self) 
        self.geometry("365x200")
        self.resizable(0,0)
        self.title("Currency Converter")
        self.space = Label(text="").grid(row=0)
        self.n= StringVar()
        self.currency_converter.getkeys()
        self.curr1= ttk.Combobox(textvariable=self.n, width=5, text='curr1')
        self.curr1['values']=self.currency_converter.currlist
        self.curr1.current()
        self.curr1.grid(row=0, column=0, padx=(30,0), pady=(10,0))
        self.text = Label(text="to").grid(row=0,column=1,padx=(90,90), pady=(20,0))
        self.curr2= ttk.Combobox(textvariable=self.n, width=5,text="curr2")
        self.curr2['values']= self.currency_converter.currlist
        self.curr2.current()
        self.curr2.grid(row=0, column=2,padx=(0,60), pady=(20,0))
        self.space = Label(text="").grid(row=1)
        self.curr1_value = Entry(width=8)
        self.curr1_value.grid(row=2, column=0, padx= (30,0))
        self.curr2_value = Entry(width=8)
        self.curr2_value.grid(row=2, column=2, padx= (0,60))
        
        self.space = Label(text="").grid(row=3)

        self.button = Button(text="CONVERT", background='white', borderwidth=1, height=1, width=10,  font =('arial', 8), command= lambda:self.currency_converter.convert(self.curr1,self.curr1_value.get(), self.curr2, self.curr2_value) ).grid(row=4,columnspan=2, column=0, padx=(80,0))
if __name__ == '__main__': 
    CurrencyConverterUI(CurrencyConverter()) 
    mainloop() 



