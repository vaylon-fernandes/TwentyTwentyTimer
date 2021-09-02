import time
from tkinter import Tk, Button, Label, Frame, IntVar, messagebox
import pyttsx3


class TimerTwentyTwenty:
    def __init__(self, root):
        self.root = root
        root.title('20-20-20 Timer')
        width = 450
        height = 300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        center_align_window = f'{width}x{height}+{(screenwidth - width) // 2}+{(screenheight - height) // 2}'
        root.geometry(center_align_window)
        root.resizable(False, False)
        root.config(bg="black")

        self.minutes = IntVar()
        self.seconds = IntVar()
        self.minutes.set("20")
        self.seconds.set("0")

        title_lbl = Label(root, text="20-20-20 Timer", pady=10)
        title_font = ("Comic Sans MS", 24, "bold")
        title_lbl.configure(font=title_font, foreground="white", bg="black")

        time_frame = Frame(root, borderwidth=2, relief="groove")
        minutes_label = Label(time_frame, textvariable=self.minutes)
        separator_label = Label(time_frame, text=":")
        seconds_label = Label(time_frame, textvariable=self.seconds)
        time_font = ("OCR A Extended", 100, "bold")
        time_elements = [minutes_label, separator_label, seconds_label]

        for element in time_elements:
            element.configure(font=time_font, foreground="white", bg="black")

        button_font = ("Comic Sans MS", 14)
        start_button = Button(root, text="Start", font=button_font, command=self.start)
        reset_button = Button(root, text="Reset", font=button_font, command=self.reset)

        title_lbl.pack()
        time_frame.pack()
        minutes_label.pack(side="left")
        separator_label.pack(side="left")
        seconds_label.pack(side="right")
        start_button.pack(pady=10, side="left")
        reset_button.pack(pady=10, side="right")

        self.reset_timer = False
        # Initialize text to speech engine
        self.engine = pyttsx3.init()

    def start(self):
        self.reset_timer = False
        temp = int(self.minutes.get())*60 + int(self.seconds.get())
        count_minutes = True
        while temp > -1 and not self.reset_timer:
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins, secs = divmod(temp, 60)

            self.minutes.set(mins)
            self.seconds.set(secs)

            # updating the GUI window after decrementing the
            # temp value every time
            self.root.update()
            time.sleep(1)

            if temp == 0:
                # Toggle State to count 20 minutes or 20 seconds
                count_minutes = not count_minutes
                if not count_minutes:
                    self.engine.say("20 minutes up. Time to look away!")
                    self.engine.runAndWait()
                    start_seconds = messagebox.askyesno("Start 20 secs timer",
                                                        "Want to start the 20 seconds timer?")
                    if start_seconds:
                        self.seconds.set(20)
                        temp = int(self.seconds.get())
                        self.root.update()
                        continue
                else:
                    self.engine.say("20 seconds up. Time to get back to work!")
                    self.engine.runAndWait()
                    start_minutes = messagebox.askyesno("Start 20 mins timer",
                                                        "Want to start the 20 minutes timer?")
                    if start_minutes:
                        self.minutes.set(20)
                        temp = int(self.minutes.get())*60
                        self.root.update()
                        continue
            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1

    def reset(self):
        self.minutes.set(20)
        self.seconds.set(0)
        self.reset_timer = True


def main():
    root = Tk()
    gui = TimerTwentyTwenty(root)
    root.mainloop()


if __name__ == '__main__':
    main()
