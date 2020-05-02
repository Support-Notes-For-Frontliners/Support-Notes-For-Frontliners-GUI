import tkinter
import scrollable_frame
import note_actions
import textwrap
tk = tkinter

print('hello world')  # yeah, this is a symbolic blessing. don't remove this.
print(str(note_actions.get_note_amt(note_actions.data)))
window = tk.Tk()
window.geometry("300x300+300+300")  # widthxheight (px)
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
        text_string = str(data_iterable[data_piece])
        start_string = '\'note\': '
        end_string = ', \'sender\': '
        text_string = text_string[text_string.index(
            start_string) + len(start_string):text_string.index(end_string)]
        cb = tk.Checkbutton(checkbox_pane.interior, var=var, text=textwrap.fill(text_string, 110),
                            onvalue=data_piece, offvalue="",
                            anchor="w", width=100, height=8,
                            relief="flat", highlightthickness=0
                            )
        cb.grid(row=x, column=0)
        # cb.deselect()

        x += 1

    window.geometry("740x600+300+300")

# function of save process


def save_command():
    approved_keys = getCheckedItems(window)
    note_actions.set_notes_value(
        note_actions.data_loc, approved_keys, 'approved', True)


"""
create scrollable frame
"""
checkbox_pane = scrollable_frame.ScrollableFrame(window, bg='#FFFFFF')
checkbox_pane.pack(expand="true", fill="both")


btn_checkbox = tk.Button(checkbox_pane.interior,
                         text="List: click here to display all unapproved notes", command=button_callback).grid(row=0, column=0)

btn_save = tk.Button(checkbox_pane.interior,
                     text="Save: click here to approve all selected notes", command=save_command).grid(row=1, column=0)


"""
run the window
"""
window.mainloop()
