"""GUI"""

mojalista = []
from class_project import Heat_calculator

from tkinter import Tk, Label, Button, ttk
from tkinter import *

root = Tk()
root.title('Heat Flow Calculator')
root.geometry("800x300")


def click_action1():
    global label2, label3, click_button2, material1

    label1.destroy()
    click_button1.destroy()

    label2 = Label(root, text="\nRodzaje materiałów do wyboru:\ncegła pełna, cegła kratówka, cegła dziurawka, pustak ceramiczny", font=30, fg="green")
    label2.pack()
    label3 = Label(root, text="Wpisz rodzaj materiału zewnetrznego: ", font=30, fg="green")
    label3.pack()

    material1 = ttk.Entry(root,font=('Century 12'),width=20)            
    material1.pack(pady= 30)

    click_button2 = Button(root, text="Enter", width=30, command=click_action2)
    click_button2.pack()

def click_action2():
    global label5, label6, material2, click_button3


    lable_text1 = material1.get().lower()

    
    if lable_text1 not in ['cegła pełna', 'cegła kratówka', 'cegła dziurawka', 'pustak ceramiczny']:
        global exit1, click_exit_button1

        label2.destroy()
        label3.destroy()
        click_button2.destroy()
        material1.destroy()
        exit1 = Label(root, text="Niepoprawny materiał, spróbuj jeszcze raz :)", font=30, fg="green")
        exit1.pack()
        click_exit_button1 = Button(root, text="Ok...", width=30, command=click_exit_action1)
        click_exit_button1.pack()
    else:
        mojalista.append(lable_text1)

        label2.destroy()
        label3.destroy()
        click_button2.destroy()
        material1.destroy()

        # pomyliłem indeksy, nie ma label4
        label5 = Label(root, text="\nRodzaje materiałów do wyboru:\nwełna mineralna, styropian", font=30, fg="green")
        label5.pack()
        label6 = Label(root, text="Wpisz rodzaj materiału wewnętrznego:", font=30, fg="green")
        label6.pack()
        
        material2 = ttk.Entry(root,font=('Century 12'),width=20)
        material2.pack(pady= 30)
        click_button3 = Button(root, text="Enter", width=30, command=click_action3)
        click_button3.pack()

def click_action3():
    global label7, temp_zew, click_button4
    
    lable_text2 = material2.get().lower()

    if lable_text2 not in ['wełna mineralna', 'styropian']:
        global exit2, click_exit_button2

        label5.destroy() 
        label6.destroy()
        material2.destroy()
        click_button3.destroy()

        exit2 = Label(root, text="Niepoprawny materiał, spróbuj jeszcze raz :)", font=30, fg="green")
        exit2.pack()
        click_exit_button2 = Button(root, text="Ok...", width=30, command=click_exit_action2)
        click_exit_button2.pack()
        
    else:
        mojalista.append(lable_text2)

        label5.destroy()
        label6.destroy()
        material2.destroy()
        click_button3.destroy()


        label7 = Label(root, text="\nWpisz temperature panującą na zewnątrz [℃ ]:", font=30, fg="green")
        label7.pack()
        temp_zew = ttk.Entry(root,font=('Century 12'),width=20)
        temp_zew.pack(pady= 30)
        click_button4 = Button(root, text="Enter", width=30, command=click_action4)
        click_button4.pack()

def click_action4():
    global label8, temp_wew, click_button5

    lable_text3 = temp_zew.get()
    lable_text3 = float(lable_text3)

    if lable_text3 > 50 or lable_text3 < -50:

        global exit3, click_exit_button3

        label7.destroy()
        temp_zew.destroy()
        click_button4.destroy()

        exit3 = Label(root, text="Na pewno nie panuje taka temperatura, spróbuj jeszcze raz :)", font=30, fg="green")
        exit3.pack()
        click_exit_button3 = Button(root, text="Ok...", width=30, command=click_exit_action3)
        click_exit_button3.pack()
        
    else:    
        mojalista.append(lable_text3)

        label7.destroy()
        temp_zew.destroy()
        click_button4.destroy()

        label8 = Label(root, text="\nWpisz temperature panującą w pokoju [℃ ]:", font=30, fg="green")
        label8.pack()
        temp_wew = ttk.Entry(root,font=('Century 12'),width=20)
        temp_wew.pack(pady= 30)
        click_button5 = Button(root, text="Enter", width=30, command=click_action5)
        click_button5.pack()
    
def click_action5():
    global label9, grubosc_sciany, click_button6

    lable_text4 = temp_wew.get()
    lable_text4 = float(lable_text4)
    if lable_text4 > 35 or lable_text4 < -30:
        global exit4, click_exit_button4

        label8.destroy()
        temp_wew.destroy()
        click_button5.destroy()

        exit4 = Label(root, text="W środku na pewno nie panuje taka temperatura, spróbuj jeszcze raz :)", font=30, fg="green")
        exit4.pack()
        click_exit_button4 = Button(root, text="Ok...", width=30, command=click_exit_action4)
        click_exit_button4.pack()

    else:
        mojalista.append(lable_text4)

        label8.destroy()
        temp_wew.destroy()
        click_button5.destroy()


        label9 = Label(root, text="\nWpisz grubość ściany w [m]:", font=30, fg="green")
        label9.pack()
        global grubosc_sciany
        grubosc_sciany = ttk.Entry(root,font=('Century 12'),width=20)
        grubosc_sciany.pack(pady= 30)
        click_button6 = Button(root, text="Enter", width=30, command=click_action6)
        click_button6.pack()

def click_action6():
    global label10, label11, pole_przekroju, click_button7

    lable_text5 = grubosc_sciany.get()
    lable_text5 = float(lable_text5)

    if lable_text5 > 2 or lable_text5 < 0.1:
        global exit5, click_exit_button5

        label9.destroy()
        grubosc_sciany.destroy()
        click_button6.destroy()

        exit5 = Label(root, text="Na pewno coś źle zmierzyłeś, spróbuj jeszcze raz :)", font=30, fg="green")
        exit5.pack()
        click_exit_button5 = Button(root, text="Ok...", width=30, command=click_exit_action5)
        click_exit_button5.pack()
        ...

    else:
        mojalista.append(lable_text5)

        label9.destroy()
        grubosc_sciany.destroy()
        click_button6.destroy()

        label10 = Label(root, text="\nZostał ostatni krok!", font=30, fg="green")
        label10.pack()
        label11 = Label(root, text="Wpisz jak duża jest twoja ściana w [㎡]:", font=30, fg="green")
        label11.pack()

        pole_przekroju = ttk.Entry(root,font=('Century 12'),width=20)
        pole_przekroju.pack(pady= 30)

        click_button7 = Button(root, text="Enter", width=30, command=click_action7)
        click_button7.pack()

def click_action7():

    lable_text6 = pole_przekroju.get()
    lable_text6 = float(lable_text6)

    if lable_text6 < 0.01 or lable_text6 > 100:
        global exit6, click_exit_button6
        label10.destroy()
        label11.destroy()
        pole_przekroju.destroy()
        click_button7.destroy()

        exit6 = Label(root, text="Na pewno coś źle zmierzyłeś, spróbuj jeszcze raz :)", font=30, fg="green")
        exit6.pack()
        click_exit_button6 = Button(root, text="Ok...", width=30, command=click_exit_action6)
        click_exit_button6.pack()

    else:
        mojalista.append(lable_text6)

        label10.destroy()
        label11.destroy()
        pole_przekroju.destroy()
        click_button7.destroy()

        label12 = Label(root, text="\n\nJuż wszystko wiemy!", font=30, fg="green")
        label12.pack()

        calculator = Heat_calculator(mojalista)
        var = StringVar()
        var.set(calculator)

        label13 = Label(root, textvariable=var, font=30, fg="green")
        label13.pack()
        
        
def click_exit_action1():
    mojalista.clear()
    exit1.destroy()
    click_exit_button1.destroy()
    click_action1()

def click_exit_action2():
    mojalista.clear
    exit2.destroy()
    click_exit_button2.destroy()
    click_action1()

def click_exit_action3():
    mojalista.clear()
    exit3.destroy()
    click_exit_button3.destroy()
    click_action1()

def click_exit_action4():
    mojalista.clear()
    exit4.destroy()
    click_exit_button4.destroy()
    click_action1()

def click_exit_action5():
    mojalista.clear()
    exit5.destroy()
    click_exit_button5.destroy()
    click_action1()

def click_exit_action6():
    mojalista.clear()
    exit6.destroy()
    click_exit_button6.destroy()
    click_action1()




def action():
    global label1, click_button1

    label1 = Label(root, text="\nWpisz poniżej potrzebne parametry a ja pokaże Ci ile ciepła ucieka Ci przez ściane :)\n", font=30, fg="green")
    label1.pack()
    click_button1 = Button(root, text="Spróbujmy!", width=30, command=click_action1)
    click_button1.pack()



def main():
    action()
    root.mainloop()


if __name__ == "__main__":
    main()
