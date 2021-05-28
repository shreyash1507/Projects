###IMPORTING LIBRARIES###
import profunc
import sqlite3
import tkinter as tk


#####MAIN WINDOW######

w=tk.Tk()
w.config(bg='black')
w.title('Phonebook')
w.geometry('585x550')   #window size


textStr=tk.StringVar()
contact=tk.StringVar()

vari=tk.StringVar()

pb=profunc.phone()  #object of class from profunc

######ADDITION FUNCTION AND WINDOW#########

def add():
    w1=tk.Tk()
    w1.config(bg='black')
    w1.title('ADD NEW')
    w1.geometry('400x400')
    name=tk.StringVar()
    number=tk.StringVar()
    
    #####LABEL####
    lab_name=tk.Label(w1,text="NAME",font=('Cambria',25),fg='azure',bg='black')
    lab_num=tk.Label(w1,text="CONTACT NUMBER",font=('Cambria',25),fg='azure',bg='black')
    ####ENTRY####
    entry_name=tk.Entry(w1,text="Name",textvariable=name,font=('Cambria',25),bg='azure',fg='black')
    entry_num=tk.Entry(w1,text="Number",textvariable=number,font=('Cambria',25),bg='azure',fg='black')
    lab_name.pack(side='top')
    entry_name.pack(side='top')
    lab_num.pack(side='top')
    entry_num.pack(side='top')
    ####BUTTON#####
    add_btn=tk.Button(w1,text='ADD',font=('Cambria',25),bg='azure',fg='black',command=lambda:pb.add_num(str(entry_name.get()),str(entry_num.get())))
    add_btn.pack(side='top')
    
    exit_btn=tk.Button(w1,text="EXIT",font=('Cambria',25),bg='azure',fg='red',command=w1.destroy)
    exit_btn.pack(side='bottom')
    w1.mainloop()

####SEARCH FUNCTION#####
def searrch(x):
    
    var=pb.search(x)
    contact.set(var[0])

#####UPDATE FUNCTIONS AND WINDOW#####

def update():
    w2=tk.Tk()
    w2.config(bg='black')
    w2.title('Update')
    w2.geometry('400x500')
    
    
    update_l=tk.Label(w2,text='UPDATE CONTACT',font=('Cambria',25),fg='azure',bg='black')
    update_l.pack(side='top')

    name=tk.StringVar()
    number=tk.StringVar()
    
    #####LABEL####
    lab_name=tk.Label(w2,text="NAME",font=('Cambria',25),fg='azure',bg='black')
    lab_num=tk.Label(w2,text="CONTACT NUMBER",font=('Cambria',25),fg='azure',bg='black')
    entry_name=tk.Entry(w2,text="Name",textvariable=name,font=('Cambria',25),bg='azure',fg='black')
    entry_num=tk.Entry(w2,text="Number",textvariable=number,font=('Cambria',25),bg='azure',fg='black')
    lab_name.pack(side='top')
    
    ####ENTRY####
    entry_name.pack(side='top')
    lab_num.pack(side='top')
    entry_num.pack(side='top')
    
    ####BUTTON####
    add_btn=tk.Button(w2,text='UPDATE',font=('Cambria',25),bg='azure',fg='black',command=lambda:pb.updatee(str(entry_name.get()),str(entry_num.get())))
    add_btn.pack(side='top')
    
    exit_btn=tk.Button(w2,text="EXIT",font=('Cambria',25),bg='azure',fg='red',command=w2.destroy)
    exit_btn.pack(side='bottom')
    
    w2.mainloop()    


############SHOW ALL CONTACTS#########
def display():
    w3=tk.Tk()
    w3.config(bg='black')
    w3.title('Contacts')
    w3.geometry('400x500')
    
#####################SHOW ALL CONTACTS##########################
    
    dis=tk.Label(w3,text='All CONTACTS',font=('Cambria',25),bg='azure',fg='black')
    dis.pack(side='top')
    variable=pb.show_all()
    for i in variable:
        lab=tk.Label(w3,text=i,font=('Cambria',25),fg='azure',bg='black')
        lab.pack(side='top')
        
    exit_btn=tk.Button(w3,text="EXIT",font=('Cambria',25),bg='azure',fg='red',command=w3.destroy)
    exit_btn.pack(side='bottom')

#####################MAIN WINDOW#################

welcome=tk.Label(w,text="Welcome to Phonebook",font=('Cambria',25),fg='azure',bg='black')
welcome.grid(row=0,column=0,columnspan=3)

###########ENTRY ,LABEL AND BUTTON##############
search=tk.Entry(w,text='Search',textvariable=textStr,font=('Cambria',40),fg='blue')
search_btn=tk.Button(w,text='Search',font=('Cambria',25),fg='black',command=lambda:searrch(str(search.get())))
search.grid(row=1,column=0,columnspan=3)
search_btn.grid(row=2,column=1)


label_search=tk.Label(w,textvariable=contact,font=('Cambria',25),fg='azure',bg='black')
label_search.grid(row=3,column=0,columnspan=3)
#########FUNCTIONS###################
add_btn=tk.Button(w,text="Add New",font=('Cambria',25),fg='azure',bg='black',command=add)
update_btn=tk.Button(w,text="Update",font=('Cambria',25),fg='azure',bg='black',command=update)
delete_btn=tk.Button(w,text="Delete",font=('Cambria',25),fg='azure',bg='black',command=lambda:pb.delete(str(search.get())))
all_con=tk.Button(w,text="All Contact",font=('Cambria',25),fg='azure',bg='black',command=display)

##########GRID##############
add_btn.grid(row=4,column=0,sticky='nsew')
update_btn.grid(row=4,column=1,sticky='nsew')
delete_btn.grid(row=4,column=2,sticky='nsew')
all_con.grid(row=5,column=1,sticky='nsew')

exit_btn=tk.Button(w,text="EXIT",font=('Cambria',25),bg='azure',fg='red',command=w.destroy)
exit_btn.grid(row=7,column=1,rowspan=5,pady=130)


w.mainloop()
