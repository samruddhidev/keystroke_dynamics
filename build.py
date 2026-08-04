import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import time
import os

CSV_FILE = "users.csv"

COLUMNS = [
    "UserID",
    "Username",
    "DwellTime",
    "FlightTime",
    "TotalTime",
    "TypingSpeed"
]

if not os.path.exists(CSV_FILE):
    pd.DataFrame(columns=COLUMNS).to_csv(
        CSV_FILE,
        index=False
    )

key_press_times = {}
key_data = []

start_time = None
last_release_time = None
capturing = False


def start_typing(event=None):

    global start_time
    global capturing
    global key_data
    global key_press_times
    global last_release_time

    if not capturing:

        start_time = time.perf_counter()
        last_release_time = None
        key_data = []
        key_press_times = {}
        capturing = True

        status_label.config(
            text="Recording typing pattern...",
            fg="#38BDF8"
        )


def key_pressed(event):

    global start_time
    global capturing

    if event.keysym == "Return":
        return

    if not capturing:
        start_typing()

    key = event.keysym

    if key not in key_press_times:

        key_press_times[key] = time.perf_counter()


def key_released(event):

    global last_release_time

    if not capturing:
        return

    if event.keysym == "Return":
        return

    key = event.keysym
    current_time = time.perf_counter()

    if key in key_press_times:

        press_time = key_press_times.pop(key)

        dwell_time = (
            current_time - press_time
        )

        flight_time = 0

        if last_release_time is not None:

            flight_time = (
                press_time - last_release_time
            )

            if flight_time < 0:
                flight_time = 0

        key_data.append(
            (
                dwell_time,
                flight_time
            )
        )

        last_release_time = current_time


def finish_typing():

    global capturing

    if not capturing:
        return None

    capturing = False

    if start_time is None:
        return None

    end_time = time.perf_counter()

    total_time = (
        end_time - start_time
    )

    if len(key_data) < 2:
        return None

    dwell_values = [
        item[0]
        for item in key_data
    ]

    flight_values = [
        item[1]
        for item in key_data[1:]
    ]

    average_dwell = (
        sum(dwell_values)
        / len(dwell_values)
    )

    if flight_values:

        average_flight = (
            sum(flight_values)
            / len(flight_values)
        )

    else:
        average_flight = 0

    typing_speed = (
        len(key_data)
        / total_time
        if total_time > 0
        else 0
    )

    return {
        "DwellTime": average_dwell,
        "FlightTime": average_flight,
        "TotalTime": total_time,
        "TypingSpeed": typing_speed
    }


def enroll():

    username_value = username.get().strip()
    password_value = password.get()

    if username_value == "":

        messagebox.showerror(
            "Error",
            "Please enter Login ID."
        )

        return

    if password_value == "":

        messagebox.showerror(
            "Error",
            "Please type the password."
        )

        return

    features = finish_typing()

    if features is None:

        messagebox.showerror(
            "Error",
            "Typing data could not be captured.\n\n"
            "Type the password and press ENTER."
        )

        return

    if os.path.exists(CSV_FILE):

        df = pd.read_csv(
            CSV_FILE
        )

    else:

        df = pd.DataFrame(
            columns=COLUMNS
        )

    existing_user = (
        df["Username"] == username_value
    )

    if existing_user.any():

        df.loc[
            existing_user,
            "DwellTime"
        ] = round(
            features["DwellTime"],
            4
        )

        df.loc[
            existing_user,
            "FlightTime"
        ] = round(
            features["FlightTime"],
            4
        )

        df.loc[
            existing_user,
            "TotalTime"
        ] = round(
            features["TotalTime"],
            4
        )

        df.loc[
            existing_user,
            "TypingSpeed"
        ] = round(
            features["TypingSpeed"],
            2
        )

    else:

        new_id = len(df) + 1

        new_user = pd.DataFrame(
            [[
                new_id,
                username_value,
                round(
                    features["DwellTime"],
                    4
                ),
                round(
                    features["FlightTime"],
                    4
                ),
                round(
                    features["TotalTime"],
                    4
                ),
                round(
                    features["TypingSpeed"],
                    2
                )
            ]],
            columns=COLUMNS
        )

        df = pd.concat(
            [
                df,
                new_user
            ],
            ignore_index=True
        )

    df.to_csv(
        CSV_FILE,
        index=False
    )

    status_label.config(
        text="User profile saved successfully.",
        fg="#22C55E"
    )

    messagebox.showinfo(
        "Enrollment Successful",
        "Typing profile registered successfully.\n\n"
        f"Dwell Time  : "
        f"{features['DwellTime']:.4f} sec\n"
        f"Flight Time : "
        f"{features['FlightTime']:.4f} sec\n"
        f"Total Time  : "
        f"{features['TotalTime']:.2f} sec\n"
        f"Typing Speed: "
        f"{features['TypingSpeed']:.2f} keys/sec"
    )

    clear_fields()


def login():

    username_value = username.get().strip()
    password_value = password.get()

    if username_value == "":

        messagebox.showerror(
            "Error",
            "Please enter Login ID."
        )

        return

    if password_value == "":

        messagebox.showerror(
            "Error",
            "Please type the password."
        )

        return

    if not os.path.exists(CSV_FILE):

        messagebox.showerror(
            "Error",
            "No registered users found."
        )

        return

    df = pd.read_csv(
        CSV_FILE
    )

    user = df[
        df["Username"] == username_value
    ]

    if user.empty:

        messagebox.showerror(
            "Authentication Failed",
            "User is not enrolled."
        )

        return

    features = finish_typing()

    if features is None:

        messagebox.showerror(
            "Error",
            "Typing data could not be captured.\n\n"
            "Type the password and press ENTER."
        )

        return

    stored = user.iloc[0]

    dwell_difference = abs(
        features["DwellTime"]
        - float(stored["DwellTime"])
    )

    flight_difference = abs(
        features["FlightTime"]
        - float(stored["FlightTime"])
    )

    speed_difference = abs(
        features["TypingSpeed"]
        - float(stored["TypingSpeed"])
    )

    total_difference = abs(
        features["TotalTime"]
        - float(stored["TotalTime"])
    )

    dwell_tolerance = (
        max(
            float(stored["DwellTime"])
            * 0.50,
            0.03
        )
    )

    flight_tolerance = (
        max(
            float(stored["FlightTime"])
            * 0.50,
            0.03
        )
    )

    speed_tolerance = (
        max(
            float(stored["TypingSpeed"])
            * 0.50,
            1.0
        )
    )

    total_tolerance = (
        max(
            float(stored["TotalTime"])
            * 0.50,
            0.5
        )
    )

    matched_features = 0

    if dwell_difference <= dwell_tolerance:
        matched_features += 1

    if flight_difference <= flight_tolerance:
        matched_features += 1

    if speed_difference <= speed_tolerance:
        matched_features += 1

    if total_difference <= total_tolerance:
        matched_features += 1

    if matched_features >= 3:

        result_label.config(
            text="✓ AUTHENTICATION SUCCESSFUL",
            fg="#22C55E"
        )

        status_label.config(
            text="Typing pattern matched.",
            fg="#22C55E"
        )

        messagebox.showinfo(
            "Authentication Successful",
            "ACCESS GRANTED\n\n"
            f"Login ID: {username_value}\n\n"
            f"Matching Features: "
            f"{matched_features}/4\n\n"
            "Authentication was based on "
            "typing behavior."
        )

    else:

        result_label.config(
            text="✗ AUTHENTICATION FAILED",
            fg="#EF4444"
        )

        status_label.config(
            text="Typing pattern did not match.",
            fg="#EF4444"
        )

        messagebox.showerror(
            "Authentication Failed",
            "ACCESS DENIED\n\n"
            f"Matching Features: "
            f"{matched_features}/4\n\n"
            "Typing behavior did not match "
            "the registered profile."
        )

    clear_fields()


def clear_fields():

    global capturing
    global key_data
    global key_press_times
    global start_time

    capturing = False
    key_data = []
    key_press_times = {}
    start_time = None

    username.delete(
        0,
        tk.END
    )

    password.delete(
        0,
        tk.END
    )


def show_users():

    if not os.path.exists(CSV_FILE):

        messagebox.showinfo(
            "Users",
            "No users registered."
        )

        return

    df = pd.read_csv(
        CSV_FILE
    )

    if df.empty:

        messagebox.showinfo(
            "Users",
            "No users registered."
        )

        return

    window = tk.Toplevel(
        root
    )

    window.title(
        "Registered Users"
    )

    window.geometry(
        "750x350"
    )

    window.configure(
        bg="#0F172A"
    )

    columns = (
        "UserID",
        "Username",
        "Dwell",
        "Flight",
        "Total",
        "Speed"
    )

    table = ttk.Treeview(
        window,
        columns=columns,
        show="headings"
    )

    for column in columns:

        table.heading(
            column,
            text=column
        )

        table.column(
            column,
            width=110,
            anchor="center"
        )

    table.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )

    for _, row in df.iterrows():

        table.insert(
            "",
            tk.END,
            values=(
                row["UserID"],
                row["Username"],
                row["DwellTime"],
                row["FlightTime"],
                row["TotalTime"],
                row["TypingSpeed"]
            )
        )


def clear_users():

    answer = messagebox.askyesno(
        "Clear Data",
        "Delete all registered users?"
    )

    if not answer:
        return

    pd.DataFrame(
        columns=COLUMNS
    ).to_csv(
        CSV_FILE,
        index=False
    )

    messagebox.showinfo(
        "Data Cleared",
        "All registered users have been removed."
    )


root = tk.Tk()

root.title(
    "Keystroke Dynamics Authentication"
)

root.geometry(
    "900x650"
)

root.configure(
    bg="#0F172A"
)

root.resizable(
    False,
    False
)


header = tk.Frame(
    root,
    bg="#0F172A"
)

header.pack(
    pady=(35, 10)
)


tk.Label(
    header,
    text="KEYSTROKE DYNAMICS",
    font=("Segoe UI", 27, "bold"),
    fg="#38BDF8",
    bg="#0F172A"
).pack()


tk.Label(
    header,
    text="BEHAVIORAL BIOMETRIC AUTHENTICATION",
    font=("Segoe UI", 11),
    fg="#94A3B8",
    bg="#0F172A"
).pack(
    pady=5
)


card = tk.Frame(
    root,
    bg="#1E293B"
)

card.place(
    relx=0.5,
    rely=0.55,
    anchor="center",
    width=600,
    height=430
)


tk.Label(
    card,
    text="User Authentication",
    font=("Segoe UI", 21, "bold"),
    fg="#F8FAFC",
    bg="#1E293B"
).pack(
    pady=(25, 5)
)


tk.Label(
    card,
    text="Enter Login ID and type your password",
    font=("Segoe UI", 10),
    fg="#94A3B8",
    bg="#1E293B"
).pack(
    pady=(0, 20)
)


tk.Label(
    card,
    text="LOGIN ID",
    font=("Segoe UI", 10, "bold"),
    fg="#CBD5E1",
    bg="#1E293B"
).pack(
    anchor="w",
    padx=100
)


username = tk.Entry(
    card,
    font=("Segoe UI", 12),
    bg="#334155",
    fg="#F8FAFC",
    insertbackground="#F8FAFC",
    relief="flat"
)

username.pack(
    fill="x",
    padx=100,
    pady=(5, 15),
    ipady=7
)


tk.Label(
    card,
    text="PASSWORD",
    font=("Segoe UI", 10, "bold"),
    fg="#CBD5E1",
    bg="#1E293B"
).pack(
    anchor="w",
    padx=100
)


password = tk.Entry(
    card,
    font=("Segoe UI", 12),
    bg="#334155",
    fg="#F8FAFC",
    insertbackground="#F8FAFC",
    show="*",
    relief="flat"
)

password.pack(
    fill="x",
    padx=100,
    pady=(5, 5),
    ipady=7
)


tk.Label(
    card,
    text="Password correctness is not checked.",
    font=("Segoe UI", 9),
    fg="#64748B",
    bg="#1E293B"
).pack(
    pady=5
)


button_frame = tk.Frame(
    card,
    bg="#1E293B"
)

button_frame.pack(
    pady=15
)


tk.Button(
    button_frame,
    text="ENROLL",
    command=enroll,
    font=("Segoe UI", 10, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    width=15,
    pady=8
).grid(
    row=0,
    column=0,
    padx=7
)


tk.Button(
    button_frame,
    text="LOGIN",
    command=login,
    font=("Segoe UI", 10, "bold"),
    bg="#16A34A",
    fg="white",
    activebackground="#15803D",
    activeforeground="white",
    relief="flat",
    width=15,
    pady=8
).grid(
    row=0,
    column=1,
    padx=7
)


result_label = tk.Label(
    card,
    text="Authentication Result: Not Tested",
    font=("Segoe UI", 11, "bold"),
    fg="#94A3B8",
    bg="#1E293B"
)

result_label.pack(
    pady=5
)


status_label = tk.Label(
    root,
    text="Ready",
    font=("Segoe UI", 10),
    fg="#94A3B8",
    bg="#0F172A"
)

status_label.pack(
    side="bottom",
    pady=15
)


menu_frame = tk.Frame(
    root,
    bg="#0F172A"
)

menu_frame.pack(
    side="bottom",
    pady=(0, 15)
)


tk.Button(
    menu_frame,
    text="VIEW REGISTERED USERS",
    command=show_users,
    font=("Segoe UI", 9),
    bg="#334155",
    fg="#E2E8F0",
    relief="flat",
    padx=10,
    pady=5
).pack(
    side="left",
    padx=5
)


tk.Button(
    menu_frame,
    text="CLEAR DATA",
    command=clear_users,
    font=("Segoe UI", 9),
    bg="#334155",
    fg="#E2E8F0",
    relief="flat",
    padx=10,
    pady=5
).pack(
    side="left",
    padx=5
)


password.bind(
    "<KeyPress>",
    key_pressed
)

password.bind(
    "<KeyRelease>",
    key_released
)

password.bind(
    "<Return>",
    lambda event: (
        enroll()
        if False
        else None
    )
)


username.focus()

root.mainloop()
