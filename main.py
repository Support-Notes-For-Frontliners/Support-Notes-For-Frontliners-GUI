import tkinter
import scrollable_frame
import note_actions
tk = tkinter

print('hello world')  # yeah, this is a symbolic blessing. don't remove this.

window = tk.Tk()
window.geometry("100x600+300+300")  # widthxheight (px)

"""
create scrollable frame 
"""
checkbox_pane = scrollable_frame.ScrollableFrame(window, bg='#444444')
checkbox_pane.pack(expand="true", fill="both")


# function that creates a checklist button


def button_callback():
    for x in range(1, 100):
        tk.Checkbutton(checkbox_pane.interior,
                       text="This is line %s" % x).grid(row=x, column=0)
    window.geometry("125x600+300+300")


btn_checkbox = tk.Button(checkbox_pane.interior,
                         text="List", command=button_callback)
btn_checkbox.grid(row=0, column=0)

"""
run the window
"""
window.mainloop()
# print("choices:", checklist.getCheckedItems())
