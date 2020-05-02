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
window.geometry('300x300+300+300')  # widthxheight (px)
window.vars = []
data_iterable = note_actions.get_note_condition(
    note_actions.data, 'approved', False)


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
    x = 2
    for data_piece in data_iterable:
        var = tk.StringVar(value=data_piece)
        window.vars.append(var)
        data_string = str(data_iterable[data_piece])
        start_string = '\'note\': '
        end_string = ', \'sender\': '
        data_obj = data_iterable[data_piece]
        sender_string = textwrap.fill(data_obj['sender'], 110)
        note_string = textwrap.fill(data_obj['note'], 110)
        cb = tk.Checkbutton(checkbox_pane.interior, var=var, text=note_string + '\n' + sender_string,
                            onvalue=data_piece, offvalue="",
                            anchor='w', width=100, height=len(note_string.split('\n')) + 3,
                            relief='flat', highlightthickness=0
                            )
        cb.grid(row=x, column=0)
        # cb.deselect()

        x += 1

    window.geometry('740x600+300+300')


# function of save process


def save_command():
    approved_keys = getCheckedItems(window)
    note_actions.set_notes_value(
        note_actions.data_loc, approved_keys, 'approved', True)


"""
create scrollable frame
"""
checkbox_pane = scrollable_frame.ScrollableFrame(window, bg='#FFFFFF')
checkbox_pane.pack(expand='true', fill='both')


btn_checkbox = tk.Button(checkbox_pane.interior,
                         text='List: click here to display all unapproved notes', command=button_callback).grid(row=0, column=0)

btn_save = tk.Button(checkbox_pane.interior,
                     text='Save: click here to approve all selected notes', command=save_command).grid(row=1, column=0)


"""
run the window
"""
window.mainloop()
