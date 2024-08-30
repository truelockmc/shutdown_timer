import time
import os
from datetime import datetime, timedelta
import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import math

shutdown_cancelled = False

def shutdown_system():
    if not shutdown_cancelled:
        print("\nDer Computer wird jetzt heruntergefahren...")
        os.system("shutdown /s /t 1")
    else:
        print("\nShutdown abgebrochen!")

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours)} Stunden, {int(minutes)} Minuten, {int(seconds)} Sekunden"

def show_progress_gui(total_seconds):
    """Zeigt die GUI mit dem Fortschrittsbalken und der Zeit an."""
    progress_window = tk.Toplevel(root)
    progress_window.geometry("450x400")  # Größere Standardgröße für das Fortschrittsfenster
    progress_window.minsize(450, 400)  # Mindestgröße setzen
    progress_window.title("Shutdown Timer")
    progress_window.configure(bg="#333333")  # Dark Mode Hintergrundfarbe

    tk.Label(progress_window, text="Shutdown Timer", font=("Helvetica", 16, "bold"), bg="#333333", fg="#ffffff").pack(pady=10)

    canvas = tk.Canvas(progress_window, width=200, height=200, bg="#333333", highlightthickness=0)
    canvas.pack()

    time_label = tk.Label(progress_window, text="", font=("Helvetica", 12), bg="#333333", fg="#ffffff")
    time_label.pack(pady=10)

    def draw_arc(percentage):
        """Zeichnet einen Kreisbogen entsprechend des Fortschritts in Prozent."""
        canvas.delete("all")
        canvas.create_oval(10, 10, 190, 190, outline="#555555", width=2)
        canvas.create_arc(10, 10, 190, 190, start=90, extent=-3.6 * percentage, fill="#008000", outline="")

    def update_progress():
        """Aktualisiert das Kreisdiagramm und die verbleibende Zeit."""
        nonlocal total_seconds
        start_time = time.time()
        while total_seconds > 0 and not shutdown_cancelled:
            elapsed_time = time.time() - start_time
            remaining_time = total_seconds - elapsed_time
            if remaining_time < 0:
                remaining_time = 0
            percentage = (remaining_time / total_seconds) * 100

            draw_arc(percentage)
            time_label.config(text=f"Verbleibende Zeit: {format_time(remaining_time)}")
            time.sleep(1)
            root.update_idletasks()

            if remaining_time <= 0:
                break

        if not shutdown_cancelled:
            shutdown_system()

    cancel_button = tk.Button(progress_window, text="Cancel Shutdown", command=lambda: cancel_shutdown(progress_window), bg="#DC143C", fg="white", font=("Helvetica", 12, "bold"))
    cancel_button.pack(pady=20)

    progress_thread = threading.Thread(target=update_progress)
    progress_thread.start()

def start_timer():
    global shutdown_cancelled
    shutdown_cancelled = False
    try:
        minutes = int(entry_minutes.get())
        total_seconds = minutes * 60
        root.withdraw()  # Verstecke das Hauptfenster
        show_progress_gui(total_seconds)
    except ValueError:
        messagebox.showerror("Fehler", "Bitte eine gültige Zahl eingeben!")

def start_countdown():
    global shutdown_cancelled
    shutdown_cancelled = False
    try:
        target_hour = int(entry_hour.get())
        target_minute = int(entry_minute.get())

        now = datetime.now()
        target_time = now.replace(hour=target_hour, minute=target_minute)

        # Falls die Zielzeit in der Vergangenheit liegt, füge einen Tag hinzu
        if target_time < now:
            target_time += timedelta(days=1)

        total_seconds = (target_time - now).total_seconds()
        root.withdraw()  # Verstecke das Hauptfenster
        show_progress_gui(total_seconds)

    except ValueError:
        messagebox.showerror("Fehler", "Bitte eine gültige Uhrzeit eingeben!")

def cancel_shutdown(progress_window):
    global shutdown_cancelled
    shutdown_cancelled = True
    progress_window.destroy()  # Schließt das Fortschrittsfenster
    root.deiconify()  # Zeigt das Hauptfenster wieder an
    messagebox.showinfo("Abbruch", "Shutdown abgebrochen!")

# GUI-Setup
root = tk.Tk()
root.title("Shutdown Timer")
root.geometry("450x250")  # Größere Standardgröße für das Hauptfenster
root.minsize(450, 250)  # Mindestgröße setzen
root.configure(bg="#333333")  # Dark Mode Hintergrundfarbe

# Überschrift
header_label = tk.Label(root, text="Shutdown Timer & Alarm", font=("Helvetica", 16, "bold"), bg="#333333", fg="#ffffff")
header_label.pack(pady=10)

# Timer-Einstellungen
frame_timer = tk.Frame(root, bg="#333333")
frame_timer.pack(pady=10)

tk.Label(frame_timer, text="Set Timer (Minutes):", bg="#333333", fg="#ffffff", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
entry_minutes = tk.Entry(frame_timer, width=5, font=("Helvetica", 12), bg="#444444", fg="#ffffff")
entry_minutes.pack(side=tk.LEFT, padx=5)

button_set_timer = tk.Button(frame_timer, text="Start Timer", command=start_timer, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
button_set_timer.pack(side=tk.LEFT, padx=10)

# Countdown-Einstellungen
frame_countdown = tk.Frame(root, bg="#333333")
frame_countdown.pack(pady=10)

tk.Label(frame_countdown, text="Hour (0-23):", bg="#333333", fg="#ffffff", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
entry_hour = tk.Entry(frame_countdown, width=5, font=("Helvetica", 12), bg="#444444", fg="#ffffff")
entry_hour.pack(side=tk.LEFT, padx=5)

tk.Label(frame_countdown, text="Minute (0-59):", bg="#333333", fg="#ffffff", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
entry_minute = tk.Entry(frame_countdown, width=5, font=("Helvetica", 12), bg="#444444", fg="#ffffff")
entry_minute.pack(side=tk.LEFT, padx=5)

button_set_countdown = tk.Button(frame_countdown, text="Set Alarm", command=start_countdown, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
button_set_countdown.pack(side=tk.LEFT, padx=10)

root.mainloop()