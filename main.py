import threading
import time
import tkinter as tk
import pyautogui
import keyboard



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

        self.button_to_start = tk.Button(self.frame, bg="#cab287", fg="red", width=12, text="Start", command= self.start_app)
        self.button_to_start.pack(pady=10)

        self.button_to_stop = tk.Button(self.frame, bg="#cab287", fg="#404040", width=12, text="Stop", command=self.stop_clicking)
        self.button_to_stop.pack(pady=10)

        self.app.bind('<q>', lambda event: self.stop_clicking()) #regarding how user can stop faster the autoclicker I create a event that create a temp event that calls the function that stop de program when key q is pressed

    def dataIN(self, event): #I need to delete the informational text and put the timer
        if self.delay_entry.get() == "Delay":
            self.delay_entry.delete(0, tk.END)
            self.delay_entry.config(fg='black')

    def start_app(self): #function take the delay from user or automatically set to 1 sec, then create a thread to anticipate blocking points in interface
        try:
            self.delay = float(self.delay_entry.get())
        except:
            self.delay = 1.0
        self.clicker = True
        timer = 10
        for i in range (timer, 0 , -1):
            print(f"Will start in {i} seconds")
            time.sleep(1)
        self.thread = threading.Thread(target=self.clicking)
        self.thread.start()

    def clicking(self): #function that automatically click using pyautogui module for certain delay between clicks
        while self.clicker:
            if keyboard.is_pressed('q'): #if the user press q from the keyboard will automatically call function stop
                self.stop_clicking()
                break
            pyautogui.click()
            time.sleep(self.delay)

    def stop_clicking(self):
        self.clicker = False
        try:
            self.thread.join()
        except AttributeError:
            pass

        print("Auto-clicker stoped")

if __name__ == "__main__":
    app = tk.Tk() # app will be main and only frame for application
    application = Clicker(app)
    app.mainloop() 
