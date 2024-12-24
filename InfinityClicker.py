import time
import pyautogui
import threading
import random
import keyboard
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

clicking = False
hotkey = 'F6'

# Add your .ico file path here
icon_path=(r"F:\AutoClicker Program\Infinity_Clicker.ico")


def auto_click(interval):
    button = button_choice.get()
    clicks = 2 if click_type_choice.get() == "Double" else 1
    if repeat_var.get() == 1:
        try:
            repeats = int(repeat_entry.get())
            for _ in range(repeats):
                if not clicking:
                    break
                pyautogui.click(button=button, clicks=clicks)
                time.sleep(interval)
        except ValueError:
            print("Invalid repeat count")
    elif repeat_var.get() == 2:
        while clicking:
            if not clicking:
                break
            pyautogui.click(button=button, clicks=clicks)
            time.sleep(interval)

def random_click(min_interval, max_interval):
    button = button_choice.get()
    clicks = 2 if click_type_choice.get() == "Double" else 1
    while clicking:
        if not clicking:
            break
        pyautogui.click(button=button, clicks=clicks)
        interval = random.uniform(min_interval, max_interval)
        time.sleep(interval)

def start_clicking():
    global clicking
    clicking = True
    try:
        if interval_var.get() == 2:
            min_interval = float(rand_min_entry.get() or 0)
            max_interval = float(rand_max_entry.get() or 0.1)
            if min_interval > max_interval:
                print("Min interval cannot be greater than max interval")
                clicking = False
                return
            threading.Thread(target=random_click, args=(min_interval, max_interval), daemon=True).start()
        elif interval_var.get() == 1:
            hours = int(hours_entry.get() or 0)
            mins = int(mins_entry.get() or 0)
            secs = int(secs_entry.get() or 0)
            millis = int(millis_entry.get() or 0)
            interval = (hours * 3600) + (mins * 60) + secs + (millis / 1000)
            threading.Thread(target=auto_click, args=(interval,), daemon=True).start()
    except ValueError:
        print("Invalid input")
        clicking = False

def stop_clicking():
    global clicking
    clicking = False

def get_mouse_position():
    x, y = pyautogui.position()
    x_entry.delete(0, ctk.END)
    y_entry.delete(0, ctk.END)
    x_entry.insert(0, x)
    y_entry.insert(0, y)

def open_settings():
    settings_window = ctk.CTkToplevel(window)
    settings_window.title("Settings")
    settings_window.geometry("300x200")

    ctk.CTkLabel(settings_window, text="Settings", font=("Arial", 16)).pack(pady=10)
    ctk.CTkSwitch(settings_window, text="Light Theme", command=toggle_theme).pack(pady=10)
    ctk.CTkSwitch(settings_window, text="TopMost", command=toggle_topmost).pack(pady=10)

def change_hotkey():
    hotkey_dialog = ctk.CTkToplevel(window)
    hotkey_dialog.title("Change Hotkey")
    hotkey_dialog.geometry("300x150")

    ctk.CTkLabel(hotkey_dialog, text="Enter new hotkey:").pack(pady=10)
    hotkey_entry = ctk.CTkEntry(hotkey_dialog, width=40)
    hotkey_entry.pack(pady=5)
    hotkey_entry.insert(0, hotkey)

    def update_hotkey():
        global hotkey
        hotkey = hotkey_entry.get()
        keyboard.clear_all_hotkeys()
        keyboard.add_hotkey(hotkey, lambda: (start_clicking() if not clicking else stop_clicking()))
        start_button.configure(text=f"Start ({hotkey})")
        stop_button.configure(text=f"Stop ({hotkey})")
        hotkey_dialog.destroy()

    ctk.CTkButton(hotkey_dialog, text="Set Hotkey", command=update_hotkey).pack(pady=10)

def toggle_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")

def toggle_topmost():
    window.attributes("-topmost", not window.attributes("-topmost"))

keyboard.add_hotkey(hotkey, lambda: (start_clicking() if not clicking else stop_clicking()))

window = ctk.CTk()
window.title("Infinity Clicker")
window.geometry('460x500')

# Set the app icon
window.iconbitmap(icon_path)

interval_var = ctk.IntVar(value=1)

interval_frame = ctk.CTkFrame(window)
interval_frame.grid(row=0, column=0, columnspan=4, pady=10)

ctk.CTkRadioButton(interval_frame, text="Fixed Interval", variable=interval_var, value=1).grid(row=0, column=0)
ctk.CTkLabel(interval_frame, text="Hours").grid(row=0, column=1, padx=5)
hours_entry = ctk.CTkEntry(interval_frame, width=40)
hours_entry.grid(row=0, column=2, padx=5)

ctk.CTkLabel(interval_frame, text="Mins").grid(row=0, column=3, padx=5)
mins_entry = ctk.CTkEntry(interval_frame, width=40)
mins_entry.grid(row=0, column=4, padx=5)

ctk.CTkLabel(interval_frame, text="Secs").grid(row=0, column=5, padx=5)
secs_entry = ctk.CTkEntry(interval_frame, width=40)
secs_entry.grid(row=0, column=6, padx=5)

ctk.CTkLabel(interval_frame, text="Millis.").grid(row=0, column=7, padx=5)
millis_entry = ctk.CTkEntry(interval_frame, width=40)
millis_entry.grid(row=0, column=8, padx=5)

random_frame = ctk.CTkFrame(window)
random_frame.grid(row=1, column=0, columnspan=4, pady=10)

ctk.CTkRadioButton(random_frame, text="Random Click Interval Between", variable=interval_var, value=2).grid(row=0, column=0, columnspan=2)
rand_min_entry = ctk.CTkEntry(random_frame, width=50)
rand_min_entry.grid(row=0, column=2, padx=5)
rand_max_entry = ctk.CTkEntry(random_frame, width=50)
rand_max_entry.grid(row=0, column=3, padx=5)

button_frame = ctk.CTkFrame(window)
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

ctk.CTkLabel(button_frame, text="Mouse Button").grid(row=0, column=0, padx=5)
button_choice = ctk.CTkComboBox(button_frame, values=["left", "right", "middle"])
button_choice.grid(row=0, column=1, padx=5)
button_choice.set("left")

ctk.CTkLabel(button_frame, text="Click Type").grid(row=1, column=0, padx=5)
click_type_choice = ctk.CTkComboBox(button_frame, values=["Single", "Double"])
click_type_choice.grid(row=1, column=1, padx=5)

repeat_frame = ctk.CTkFrame(window)
repeat_frame.grid(row=3, column=0, columnspan=4, pady=10)

repeat_var = ctk.IntVar()
ctk.CTkRadioButton(repeat_frame, text="Repeat", variable=repeat_var, value=1).grid(row=0, column=0, padx=10)
repeat_entry = ctk.CTkEntry(repeat_frame, width=50)
repeat_entry.grid(row=0, column=1, padx=5)

ctk.CTkRadioButton(repeat_frame, text="Repeat Until Stopped", variable=repeat_var, value=2).grid(row=0, column=2, padx=10)

location_frame = ctk.CTkFrame(window)
location_frame.grid(row=4, column=0, columnspan=4, pady=10)

ctk.CTkLabel(location_frame, text="Current Location").grid(row=0, column=0, padx=5)
x_entry = ctk.CTkEntry(location_frame, width=50)
x_entry.grid(row=0, column=1, padx=5)
y_entry = ctk.CTkEntry(location_frame, width=50)
y_entry.grid(row=0, column=2, padx=5)
ctk.CTkButton(location_frame, text="Get", command=get_mouse_position).grid(row=0, column=3, padx=5)

start_button = ctk.CTkButton(window, text=f"Start ({hotkey})", command=start_clicking, fg_color="green", width=120)
start_button.grid(row=5, column=0, columnspan=2, pady=10)

stop_button = ctk.CTkButton(window, text=f"Stop ({hotkey})", command=stop_clicking, fg_color="red", width=120)
stop_button.grid(row=5, column=2, columnspan=2, pady=10)

settings_button = ctk.CTkButton(window, text="Window Settings", command=open_settings)
settings_button.grid(row=6, column=0, columnspan=2, pady=10)

change_hotkey_button = ctk.CTkButton(window, text="Change Hotkey", command=change_hotkey)
change_hotkey_button.grid(row=6, column=2, columnspan=2, pady=10)

window.mainloop()
