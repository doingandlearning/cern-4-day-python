from tkinter import messagebox

answer = messagebox.askyesno(title='Confirmation',
                             message='Are you sure that you want to exit?')
print(answer)
