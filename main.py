import tkinter as tk


class Clicker:
    def __init__(self,app):
        self.app = app
        self.app.title("MyAutoClicker")
        self.frame = tk.Frame(app)
        self.frame.pack(pady=50, padx=80) #dimensions of frame


        self.delay_entry = tk.Entry(self.frame, bg="#cab287", width=15, fg='grey', justify='center')
        self.delay_entry.insert(0, "Delay")
        self.delay_entry.bind('<FocusIn>', self.dataIN)
        self.delay_entry.pack(pady=10)

        self.button_to_start = tk.Button(self.frame, bg="#cab287", fg="red", width=12, text="Start")
        self.button_to_start.pack(pady=10)

        self.button_to_stop = tk.Button(self.frame, bg="#cab287", fg="#404040", width=12, text="Stop", command=app.destroy)
        self.button_to_stop.pack(pady=10)

    def dataIN(self, event): #I need to delete the informational text and put the timer
        if self.delay_entry.get() == "Delay":
            self.delay_entry.delete(0, tk.END)
            self.delay_entry.config(fg='black')
    def start_app(self):
        try:
            self.delay = float(self.delay_entry.get())
        except:
            self.delay = 1.0



if __name__ == "__main__":
    app = tk.Tk() # app will be main and only frame for application
    application = Clicker(app)
    app.mainloop() #
