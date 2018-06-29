#  AUTHOR:  Michael O'Brien
#  CREATED:  25 June 2018
#  UPDATED:  27 June 2018
#  DESCRIPTION:  Bookstore app


#  Import libraries needed for application
from tkinter import *
import backendDb


def get_selected_row(event):
    try:
        global selected_row
        index = lstDisplayBox.curselection()[0]
        selected_row = lstDisplayBox.get(index)
        entryTitle.delete(0, END)
        entryTitle.insert(END, selected_row[1])
        entryAuthor.delete(0, END)
        entryAuthor.insert(END, selected_row[2])
        entryYear.delete(0, END)
        entryYear.insert(END, selected_row[3])
        entryISBN.delete(0, END)
        entryISBN.insert(END, selected_row[4])
    except IndexError:
        pass


def btnView_Data():
    lstDisplayBox.delete(0, END)
    for rows in backendDb.view_data():
        lstDisplayBox.insert(END, rows)


def btnSearch_Data():
    lstDisplayBox.delete(0, END)
    for rows in backendDb.search_data(entryTitle.get(), entryAuthor.get(), entryYear.get(), entryISBN.get()):
        lstDisplayBox.insert(END, rows)

def btnAdd_Data():
    lstDisplayBox.delete(0, END)
    backendDb.insert_data(entryTitle.get(), entryAuthor.get(), entryYear.get(), entryISBN.get())
    lstDisplayBox.insert(END, (entryTitle.get(), entryAuthor.get(), entryYear.get(), entryISBN.get()))


def btnUpdate_Data():
    lstDisplayBox.delete(0, END)
    backendDb.update_data(selected_row[0], entryTitle.get(), entryAuthor.get(), entryYear.get(), entryISBN.get())
    lstDisplayBox.insert(END, (entryTitle.get(), entryAuthor.get(), entryYear.get(), entryISBN.get()))


def btnDelete_Data():
    lstDisplayBox.delete(0, END)
    backendDb.delete_data(selected_row[0])
    for rows in backendDb.view_data():
        lstDisplayBox.insert(END, rows)


#  Creates the main window and assigns the title of the application
master = Tk()
master.wm_title('Book Library')


#  Labels and data entry boxes
lblTitle = Label(master, text = 'TITLE')
lblTitle.grid(row = 0, column = 0)
strTitle = StringVar()
entryTitle = Entry(master, textvariable = strTitle)
entryTitle.grid(row = 0, column = 1)

lblYear = Label(master, text = 'YEAR')
lblYear.grid(row = 1, column = 0)
strYear = StringVar()
entryYear = Entry(master, textvariable = strYear)
entryYear.grid(row = 1, column = 1)

lblAuthor = Label(master, text = 'AUTHOR')
lblAuthor.grid(row = 0, column = 2)
strAuthor = StringVar()
entryAuthor = Entry(master, textvariable = strAuthor)
entryAuthor.grid(row = 0, column = 3)

lblISBN = Label(master, text = 'ISBN')
lblISBN.grid(row = 1, column = 2)
strISBN = StringVar()
entryISBN = Entry(master, textvariable = strISBN)
entryISBN.grid(row = 1, column = 3)


#  List Display Box for output and scrollbax
lstDisplayBox = Listbox(master, height = 25, width = 50)
lstDisplayBox.grid(row = 2, column=0, rowspan = 10, columnspan = 2)

scrollbarDisplayBox = Scrollbar(master)
scrollbarDisplayBox.grid(row = 2, column = 2, rowspan = 10)

lstDisplayBox.configure(yscrollcommand = scrollbarDisplayBox.set)
scrollbarDisplayBox.configure(command = lstDisplayBox.yview)

lstDisplayBox.bind('<<ListboxSelect>>', get_selected_row)

#  Buttons
btnViewAll = Button(master, text = 'View All', width = 12, command = btnView_Data)
btnViewAll.grid(row = 2, column = 3)

btnSearch = Button(master, text = 'Search', width = 12, command = btnSearch_Data)
btnSearch.grid(row = 3, column = 3)

btnAdd = Button(master, text = 'Add', width = 12, command = btnAdd_Data)
btnAdd.grid(row = 4, column = 3)

btnUpdate = Button(master, text = 'Update', width = 12, command = btnUpdate_Data)
btnUpdate.grid(row = 5, column = 3)

btnDelete = Button(master, text = 'Delete', width= 12, command = btnDelete_Data)
btnDelete.grid(row = 6, column = 3)

btnClose = Button(master, text = 'Close', width = 12, command = master.destroy)
btnClose.grid(row = 7, column = 3)


master.mainloop()
