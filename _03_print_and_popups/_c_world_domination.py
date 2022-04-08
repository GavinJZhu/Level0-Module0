from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__=='__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Ask the user if they know how to write code.
    UA = simpledialog.askstring(title='Hmmmmm', prompt= "Know how 2 code?" )
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
    if UA == 'yes':
        messagebox.showinfo(title= 'Uh oh..', message= "Well have fun ruling the world...   ( ⁰д⁰)" )
    # 2. If they say
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    else:
        messagebox.showerror(title= 'What r u doing?', message= "Sign up for The League to learn... now!")
    # Run the window's .mainloop() method
    window.mainloop()
