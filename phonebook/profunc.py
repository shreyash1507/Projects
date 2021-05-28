#########IMPORTING REQUIRE LIBRARIES###############
import tkinter as tk
import tkinter.messagebox
import sqlite3 as sl

class phone():
    def __init__(self):
        #############CONNECTING TO DATABASE#############
        conn=sl.connect('phone.db');
        c=conn.cursor();
        ##############CREATING TABLE###################
        
        c.execute("""CREATE TABLE IF NOT EXISTS phonebook(
            names TEXT,
            num TEXT)""");

        conn.commit();
        conn.close();
        ################FUNCTION TO ADD NEW CONTACT###################
    def add_num(self,nam,numm):
        conn=sl.connect('phone.db');
        c=conn.cursor();
        c.execute("INSERT INTO phonebook VALUES(?,?)",(nam,numm));
        conn.commit();
        conn.close();
        tkinter.messagebox.showinfo("New","New contact added")
        ################FUNCTION TO SEACRCH CONTACT#################
    def search(self,nummm):
        conn=sl.connect('phone.db');
        c=conn.cursor();
        c.execute("SELECT * from phonebook where num= (?)",(nummm,));
        items=c.fetchall();
        conn.commit();
        conn.close();
        return items
        ################FUNCTION TO UPDATE CONTACT#################
    def updatee(self,names,num):
        conn=sl.connect('phone.db');
        c=conn.cursor()
        c.execute("UPDATE phonebook set num =(?) where names = (?)",(num,names));
        conn.commit();
        conn.close();
        tkinter.messagebox.showinfo("Update","Contact Updated") 
        ##############FUNCTION TO DELETE CONTACT#####################
    def delete(self,num):
        conn=sl.connect('phone.db');
        c=conn.cursor();
        c.execute("DELETE FROM phonebook where num= (?)",(num,));
        conn.commit();
        conn.close();
        tkinter.messagebox.showinfo("Del","Contact Deleted")
        ###############FUNCTION TO DISPLAY ALL CONTACTS###############
    def show_all(self):
        conn=sl.connect('phone.db');
        c=conn.cursor();
        
        c.execute("SELECT * FROM phonebook");
        items=c.fetchall()
        for i in items:
            yield i
        conn.commit();
        conn.close();
    