import os
import tkinter as tk
import timer


def start_timer():
    time = get_entry_time()
    os.system(f'shutdown -s -t {time}')


def stop_timer():
    os.system('shutdown /a')


def get_entry_time(event=None):
    minutes = entry_minutes.get()
    hours = entry_hours.get()
    if not minutes and not hours:
        time = 3600
    if minutes:
        try:
            minutes = float(minutes)
        except ValueError:
            tk.Label(root, text='Input error').grid(row=1, column=0)
        if not hours:
            time = minutes * 60
    if hours:
        try:
            hours = float(hours)
        except ValueError:
            tk.Label(root, text='Input error').grid(row=0, column=0)
        if not minutes and hours > 0:
            time = hours * 60 * 60
        elif minutes and hours and hours > 0:
            time = (hours * 60 + minutes) * 60

    return int(time)

def get_h_m_s():
    pass


root = tk.Tk()
root.title('Sleep timer')
hours_lbl = tk.Label(root, text='Hours')
hours_lbl.grid(row=0, column=0)

minutes_lbl = tk.Label(root, text='Minutes')
minutes_lbl.grid(row=1, column=0)

entry_hours = tk.Entry(root)
entry_hours.grid(row=0, column=1)
entry_hours.bind('<Return>', get_entry_time)

entry_minutes = tk.Entry(root)
entry_minutes.grid(row=1, column=1)
entry_minutes.bind('<Return>', get_entry_time)

button1 = tk.Button(root, text='Start timer', command=start_timer).grid(row=2, column=3)
button2 = tk.Button(root, text='Stop timer', command=stop_timer).grid(row=2, column=4)

root.mainloop()
