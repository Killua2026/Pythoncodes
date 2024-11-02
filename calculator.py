from tkinter import * #the asterisk means import all the elements in the tkinter module
win = Tk() #this creates an instance of tkinter window/blank window
win.title('Calculator') # to change name title of the app window
win.geometry('370x365') #to adjust size of app window
win.resizable(0,0) #to make the window to be a fixed size  

#Function for button clicking and dispay
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

#Function for clear button     
def bt_clear():
    global expression
    expression = ""
    input_text.set("")

#Function for equal button
def bt_equal():
 global expression
 result = str(eval(expression))
 input_text.set(result)
 expression = ""

expression=""
input_text = StringVar()    

#input field frame
input_frame = Frame(win,width=312,height=50)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font = ('arial', 18, 'bold'), width=45, justify=RIGHT, textvariable = input_text)
input_field.grid(row=0, column=0)

#increase the input field height
input_field.pack(ipady=10) #creates internal padding to increase height

#Button frame
btns_frame = Frame(win, width=310, height=270)
btns_frame.pack()

#BUTTON FIRST ROW
clear = Button(btns_frame, text ='C', width=35, height=3, command=lambda:bt_clear()).grid(row=0,column=0, columnspan=3,padx=1, pady=1)
divide = Button(btns_frame, text = '/', width=10, height=3, command=lambda:btn_click('/')).grid(row=0, column=3, padx=1, pady=1)

#BUTTON SECOND ROW
seven = Button(btns_frame, text='7', width=10, height=3, command=lambda:btn_click(7)).grid(row=1, column=0, padx=1,pady=1)
eight = Button(btns_frame, text='8', width=10, height=3, command=lambda:btn_click(8)).grid(row=1, column=1, padx=1,pady=1)
nine = Button(btns_frame, text='9', width=10, height=3, command=lambda:btn_click(9)).grid(row=1, column=2, padx=1,pady=1)
multiply = Button(btns_frame, text='*', width=10, height=3, command=lambda:btn_click('*')).grid(row=1, column=3, padx=1,pady=1)

#BUTTON THIRD ROW
four = Button(btns_frame, text='4', width=10, height=3, command=lambda:btn_click(4)).grid(row=2, column=0, padx=1,pady=1)
five = Button(btns_frame, text='5', width=10, height=3, command=lambda:btn_click(5)).grid(row=2, column=1, padx=1,pady=1)
six = Button(btns_frame, text='6', width=10, height=3, command=lambda:btn_click(6)).grid(row=2, column=2, padx=1,pady=1)
minus = Button(btns_frame, text='-', width=10, height=3, command=lambda:btn_click('-')).grid(row=2, column=3, padx=1,pady=1)

#BUTTON FOURTH ROW
one = Button(btns_frame, text='1', width=10, height=3, command=lambda:btn_click(1)).grid(row=3, column=0, padx=1,pady=1) 
two = Button(btns_frame, text='2', width=10, height=3, command=lambda:btn_click(2)).grid(row=3, column=1, padx=1,pady=1)
three = Button(btns_frame, text='3', width=10, height=3, command=lambda:btn_click(3)).grid(row=3, column=2, padx=1,pady=1)
plus = Button(btns_frame, text='+', width=10, height=3, command=lambda:btn_click('+')).grid(row=3, column=3, padx=1,pady=1)

#BUTTON FIFTH ROW
zero = Button(btns_frame, text='0', width=24, height=3, command=lambda:btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1,pady=1)
point = Button(btns_frame, text='.', width=10, height=3, command=lambda:btn_click('.')).grid(row=4, column=2, padx=1,pady=1)
equal = Button(btns_frame, text='=', width=10, height=3, command = lambda:bt_equal()).grid(row=4, column=3, padx=1,pady=1)
        
win.mainloop() #this keeps the tkinter window from disapperaring by looping

