# 🔐 Keystroke Dynamics Authentication System

A Python-based **behavioral biometric authentication system** that verifies users based on their unique typing behavior. The system analyzes keystroke patterns such as **dwell time, flight time, typing speed, and total typing time** to determine whether a login attempt matches the registered user's typing profile.

---

## 📌 Overview

Traditional authentication systems mainly depend on a username and password. This project demonstrates an additional layer of authentication using **Keystroke Dynamics**, a behavioral biometric technique.

Instead of checking whether the entered password is correct, the system analyzes **how the user types** the password.

During enrollment, the user's typing pattern is captured and stored as a behavioral profile. During login, a new typing sample is captured and compared with the registered profile.

> **The password value itself is not verified. Authentication is based on the user's typing behavior.**

---

## 🎯 Aim

To implement a user authentication system using **keystroke dynamics** for identifying legitimate users based on their typing behavior.

---

## ✨ Features

* 🔑 Login ID-based authentication
* ⌨️ Keystroke timing analysis
* 🧠 Behavioral biometric authentication
* 📊 Dwell time calculation
* ⏱️ Flight time calculation
* 🕐 Total typing time calculation
* ⚡ Typing speed calculation
* 💾 Automatic user profile storage using CSV
* 🖥️ Dark-themed graphical user interface
* ✅ Authentication success/failure detection
* 👥 Registered user viewing
* 🗑️ Dataset clearing option

---

## 🧠 What is Keystroke Dynamics?

Keystroke Dynamics is a **behavioral biometric authentication technique** that identifies a person based on their unique typing pattern.

Different users naturally type differently because of differences in:

* Typing speed
* Key-holding duration
* Time between keystrokes
* Typing rhythm
* Finger movement
* Typing consistency

The system uses these characteristics to create a behavioral typing profile.

---

## 📊 Features Used

| Feature               | Description                                          |
| --------------------- | ---------------------------------------------------- |
| **Dwell Time**        | Time for which a key remains pressed                 |
| **Flight Time**       | Time between releasing one key and pressing the next |
| **Total Typing Time** | Total time taken to type the input                   |
| **Typing Speed**      | Number of keystrokes typed per second                |

These features are used together to represent the user's typing behavior.

---

## 🔄 System Workflow

```text
                    USER
                     │
                     ▼
               Enter Login ID
                     │
                     ▼
               Type Password
                     │
                     ▼
          Capture Keystroke Timing
                     │
                     ▼
           Extract Typing Features
                     │
          ┌──────────┴──────────┐
          │                     │
       ENROLL                  LOGIN
          │                     │
          ▼                     ▼
    Store User Profile     Compare Profile
                                │
                                ▼
                       Typing Pattern Match
                           │           │
                           ▼           ▼
                       SUCCESS       FAILED
```

---

## 🖥️ User Interface

The application is developed using **Tkinter** and uses a dark-themed interface.

The GUI contains:

* Login ID field
* Password field
* Enroll button
* Login button
* Authentication status
* Registered users viewer
* Clear data option

The dark interface provides a simple and modern cybersecurity-style appearance.

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – GUI development
* **Pandas** – Data handling and CSV storage
* **NumPy** – Numerical processing
* **CSV** – User profile storage

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Keystroke-Dynamics-Authentication.git
```

### 2. Open the Project Folder

```bash
cd Keystroke-Dynamics-Authentication
```

### 3. Install Required Libraries

```bash
pip install pandas numpy
```

Tkinter is included with most standard Python installations. On Windows, it is generally available by default.

### 4. Run the Application

```bash
python app.py
```

---

## 🚀 How to Use

### 👤 Step 1: Enroll a User

1. Enter a **Login ID**.
2. Type a password or passphrase.
3. Click **ENROLL**.
4. The system captures the user's typing behavior.
5. The typing features are calculated.
6. The user's behavioral profile is saved in `users.csv`.

The actual password is **not stored or checked**.

---

### 🔐 Step 2: Login

1. Enter the registered Login ID.
2. Type a password or passphrase.
3. Click **LOGIN**.
4. The system captures the new typing pattern.
5. The new features are compared with the registered profile.
6. If the typing behavior is sufficiently similar, authentication is successful.

---

## 🔍 Authentication Logic

The system compares four behavioral characteristics:

```text
             Dwell Time
                  +
             Flight Time
                  +
           Typing Speed
                  +
          Total Typing Time
                  │
                  ▼
        Typing Pattern Comparison
                  │
                  ▼
       ┌──────────┴──────────┐
       │                     │
    3 or more              Less than
      match                  3 match
       │                     │
       ▼                     ▼
   AUTHENTICATED          ACCESS DENIED
```

If at least **3 out of 4 features** fall within the acceptable tolerance, the user is authenticated successfully.

---

## 📁 Dataset

The application stores user typing profiles in:

```text
users.csv
```

Example:

| UserID | Username | DwellTime | FlightTime | TotalTime | TypingSpeed |
| -----: | -------- | --------: | ---------: | --------: | ----------: |
|      1 | User1    |    0.0821 |     0.0452 |      2.31 |        4.33 |
|      2 | User2    |    0.0954 |     0.0618 |      2.84 |        3.52 |

These values represent the behavioral characteristics of the registered users.

---

## 🧪 Experiment Demonstration

The project demonstrates the following cybersecurity concepts:

* Behavioral biometrics
* User authentication
* Keystroke dynamics
* Feature extraction
* Typing pattern analysis
* GUI-based authentication
* User profile storage
* Behavioral verification

---

## 🔐 Why Keystroke Dynamics?

Passwords can be stolen, guessed, or shared. Keystroke dynamics provides an additional authentication factor by analyzing the user's behavior while entering information.

For example, two users may type the same password:

```text
hello123
```

but their typing patterns may differ:

```text
User A → Faster typing, shorter key holds
User B → Slower typing, longer key holds
```

The system uses these differences to distinguish between users.

---

## ⚠️ Limitations

This project is an educational prototype and has some limitations:

* Typing behavior can change because of fatigue, stress, or injury.
* Different keyboards can affect typing patterns.
* Only a limited number of behavioral features are currently used.
* Fixed tolerance values may not work equally well for every user.
* A single typing profile may not represent all variations in a user's typing behavior.
* The system is not intended to replace production-grade authentication systems.

---

## 🔮 Future Enhancements

The system can be further improved by implementing:

* 🤖 K-Nearest Neighbors (KNN)
* 🌳 Decision Tree
* 🌲 Random Forest
* 📈 Support Vector Machine (SVM)
* 🧠 Neural Networks
* Multiple enrollment samples
* Continuous authentication
* More advanced keystroke features
* False Acceptance Rate (FAR)
* False Rejection Rate (FRR)
* Authentication accuracy evaluation
* SQLite/MySQL database integration
* Web-based authentication
* Real-time behavioral anomaly detection

---

## 👩‍💻 Author

**Samruddhi Jain**

B.Tech – Artificial Intelligence & Data Science

---

## ⭐ Conclusion

The **Keystroke Dynamics Authentication System** demonstrates the use of behavioral biometrics as an additional layer of user authentication. By analyzing features such as dwell time, flight time, typing speed, and total typing time, the system creates a behavioral profile for a registered user and compares future login attempts against that profile.

The project provides a practical implementation of **Python, GUI development, behavioral biometrics, and cybersecurity concepts** to demonstrate how user identity can be verified through typing behavior.

---

## 🔐 Key Idea

> **Don't just verify what the user knows — verify how the user types.**
