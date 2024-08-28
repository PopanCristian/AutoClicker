import tkinter as tk


class Clicker:
    def __init__(self,app):
        self.app = app
        self.app.title("MyAutoClicker")
        self.frame = tk.Frame(app)
        self.frame.pack(pady=120, padx=120) #dimensions of frame


        self.delay_entry = tk.Entry(self.frame, width=15, fg='grey', justify='center')
        self.delay_entry.insert(0, "Delay")
        self.delay_entry.bind('<FocusIn>', self.dataIN)
        self.delay_entry.pack()

        self.button_to_start = tk.Button(self.frame, width=12, text="Start")
        self.button_to_start.pack()

        self.button_to_stop = tk.Button(self.frame, width=12, text="Stop", command=app.destroy)
        self.button_to_stop.pack()

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
