# popup.py
import tkinter as tk

def create_popup():
    def submit_value():
        entered_value = entry.get()
        popup.destroy()
        popup_return.set(entered_value)

    def close_popup():
        popup.destroy()

    # Create Tkinter popup window
    popup = tk.Tk()
    popup.title("Value Input")
    popup.geometry("300x100")

    label = tk.Label(popup, text="Enter value:")
    label.pack()

    entry = tk.Entry(popup)
    entry.pack()

    submit_button = tk.Button(popup, text="Submit", command=submit_value)
    submit_button.pack()

    close_button = tk.Button(popup, text="Close", command=close_popup)
    close_button.pack()

    popup_return = tk.StringVar()
    popup_return.set(None)

    popup.mainloop()

    return popup_return.get()
