import tkinter as tk
import scrollable_frame
import note_actions
import textwrap
import sys
import os
from tkinter import *


"""
creating main window and defining necessary variables
"""
window = tk.Tk()
window.title('Support For Frontliners GUI')
window.configure(bg='#f0f0f0')
window.geometry('180x300+300+300')  # widthxheight (px)
first = True

# region stuff
region_list = ['Seattle', 'don\'t press this',
               'don\'t press this', 'don\'t press this']  # //TODO
region = StringVar(window)
region.set(region_list[0])  # default value

"""
function definitions
"""
# function to get checked items


def getCheckedItems(self):
    values = []
    for var in self.vars:
        value = var.get()
        if value:
            values.append(value)
    return values

# main function


def button_callback():
    # clear window
    global first
    global topframe
    global checkbox_pane
    # initial condition
    if first:
        selector.destroy()
        select_button.destroy()
        print('--initialized--')
        topframe = tk.Frame(window)
        topframe.pack(side=tk.TOP)
        checkbox_pane = scrollable_frame.ScrollableFrame(window)
        checkbox_pane.pack(expand=tk.TRUE, fill=tk.BOTH)

        btn_checkbox = tk.Button(topframe,
                                 text='List: display all unapproved notes', command=button_callback).grid(row=0, column=0)

        btn_save = tk.Button(topframe,
                             text='Save: approve all selected notes', command=save_command).grid(row=0, column=1)

        btn_rename = tk.Button(topframe, text='Rename: renames selected notes',
                               command=rename_command).grid(row=0, column=2)
        first = False
    # every other condition
    else:
        topframe.destroy()
        topframe = tk.Frame(window)
        topframe.pack(side=tk.TOP)
        checkbox_pane.destroy()
        checkbox_pane = scrollable_frame.ScrollableFrame(window)
        checkbox_pane.pack(expand=tk.TRUE, fill=tk.BOTH)

        btn_checkbox = tk.Button(topframe,
                                 text='List: display all unapproved notes', command=button_callback).grid(row=0, column=0)
        btn_save = tk.Button(topframe,
                             text='Save: approve all selected notes', command=save_command).grid(row=0, column=1)
        btn_rename = tk.Button(topframe, text='Rename: renames selected notes',
                               command=rename_command).grid(row=0, column=2)

    # iterate data into checkbox_pane
    print('region is ' + region.get())
    data_iterable = note_actions.get_note_condition(
        note_actions.firebase.database().child("formData").get(), 'approved', False)
    window.vars = []

    x = 0
    for data_piece in data_iterable:
        var = tk.StringVar(value=data_piece)
        window.vars.append(var)
        data_string = str(data_iterable[data_piece])
        data_obj = data_iterable[data_piece]
        sender_string = textwrap.fill(data_obj['sender'], 120)
        note_string = textwrap.fill(data_obj['note'], 120)
        location_string = textwrap.fill(data_obj['facility'], 120)
        cb = tk.Checkbutton(checkbox_pane.interior, var=var, text=note_string + '\n' + sender_string + '\n' + location_string,
                            onvalue=data_piece, offvalue="",
                            anchor='w', width=110, height=len(note_string.split('\n')) + 4,
                            relief='flat', highlightthickness=0
                            )
        cb.grid(row=x, column=1)
        cb.deselect()

        x += 1
    window.geometry('800x600+300+300')

    btn_notes_total = tk.Button(topframe, text='Total: ' + str(note_actions.get_note_amt(
        note_actions.firebase.database().child("formData").get())),
        state=tk.DISABLED).grid(row=0, column=3)

    btn_notes_unapproved = tk.Button(topframe, text='Unapproved: ' + str(len(data_iterable)),
                                     state=tk.DISABLED).grid(row=0, column=4)

    btn_home = tk.Button(topframe, text='Home',
                         command=restart).grid(row=0, column=5)


# function of save process


def save_command():
    approved_keys = getCheckedItems(window)
    print(approved_keys)
    note_actions.set_notes_value(
        note_actions.firebase.database().child("formData"), approved_keys, 'approved', [True])
    button_callback()

# function to randomize name


def rename_command():
    name_list = ['Bellevue resident', 'a thankful member of the community',
                 'patron of the frontliners', 'someone who looks up to you']  # list of good random names
    rename_keys = getCheckedItems(window)
    note_actions.set_notes_value(
        note_actions.firebase.database().child("formData"), rename_keys, 'sender', name_list)
    button_callback()


# restart

def restart():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


"""
starting screen
"""
topframe = tk.Frame(window)
# topframe.pack(side=tk.TOP)
checkbox_pane = scrollable_frame.ScrollableFrame(window)
#checkbox_pane.pack(expand=tk.TRUE, fill=tk.BOTH)

btn_checkbox = tk.Button(topframe,
                         text='List: display all unapproved notes', command=button_callback).grid(row=0, column=0)

btn_save = tk.Button(topframe,
                     text='Save: approve all selected notes', command=save_command).grid(row=0, column=1)

btn_rename = tk.Button(topframe, text='Rename: renames selected notes',
                       command=rename_command).grid(row=0, column=2)


selector = OptionMenu(window, region, *region_list)
selector.pack()

select_button = Button(window, text='OK', command=button_callback)
select_button.pack()

"""
run the window
"""
window.mainloop()
