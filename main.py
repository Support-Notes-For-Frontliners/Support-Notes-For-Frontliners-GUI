import tkinter as tk
import scrollable_frame
import note_actions
import textwrap


print(str(note_actions.get_note_amt(note_actions.data)) + ' notes received')

"""
creating main window and defining necessary variables
"""
window = tk.Tk()
window.title('Support For Frontliners GUI')
window.geometry('180x300+300+300')  # widthxheight (px)


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

# function to create Checkbuttons for every data piece


def button_callback():
    data_iterable = note_actions.get_note_condition(
        note_actions.data, 'approved', False)
    window.vars = []
    x = 0
    for data_piece in data_iterable:
        var = tk.StringVar(value=data_piece)
        window.vars.append(var)
        data_string = str(data_iterable[data_piece])
        data_obj = data_iterable[data_piece]
        sender_string = textwrap.fill(data_obj['sender'], 110)
        note_string = textwrap.fill(data_obj['note'], 110)
        cb = tk.Checkbutton(checkbox_pane.interior, var=var, text=note_string + '\n' + sender_string,
                            onvalue=data_piece, offvalue="",
                            anchor='w', width=100, height=len(note_string.split('\n')) + 3,
                            relief='flat', highlightthickness=0
                            )
        cb.grid(row=x, column=1)
        cb.deselect()

        x += 1

    window.geometry('740x600+300+300')


# function of save process


def save_command():
    approved_keys = getCheckedItems(window)
    note_actions.set_notes_value(
        note_actions.data_loc, approved_keys, 'approved', [True])
    button_callback()

# function to randomize name


def rename_command():
    name_list = ['Bellevue resident', 'a thankful member of the community',
                 'patron of the frontliners', 'someone who looks up to you']  # list of good random names
    rename_keys = getCheckedItems(window)
    note_actions.set_notes_value(
        note_actions.data_loc, rename_keys, 'sender', name_list)
    button_callback()


"""
create scrollable frame
"""

topframe = tk.Frame(window)
topframe.pack(side=tk.TOP)
checkbox_pane = scrollable_frame.ScrollableFrame(window, bg='#FFFFFF')
checkbox_pane.pack(expand=tk.TRUE, fill=tk.BOTH)


btn_checkbox = tk.Button(topframe,
                         text='List: display all unapproved notes', command=button_callback).grid(row=0, column=0)

btn_save = tk.Button(topframe,
                     text='Save: approve all selected notes', command=save_command).grid(row=0, column=1)

btn_rename = tk.Button(topframe, text='Rename: randomly renames selected notes',
                       command=rename_command).grid(row=0, column=2)
"""
run the window
"""
window.mainloop()
