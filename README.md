# 🔐 Keystroke Dynamics Authentication System

A Python-based user authentication system that uses **Keystroke Dynamics** to verify users based on their unique typing behavior.

Instead of checking only whether a password is correct, the system analyzes **how the user types** by measuring keystroke timing patterns such as dwell time, flight time, typing speed, and total typing time.

---

## 📌 Overview

Traditional authentication systems primarily depend on usernames and passwords. However, passwords can be stolen, guessed, or shared.

This project demonstrates an additional layer of security using **behavioral biometrics**.

The system captures the user's typing pattern during enrollment and creates a behavioral typing profile. During login, the new typing pattern is compared with the registered profile to determine whether the user is genuine or unauthorized.

> **The password itself is not validated. The system focuses on the user's typing behavior.**

---

## 🎯 Aim

To implement a user authentication system using **keystroke dynamics** for identifying legitimate users based on their typing behavior.

---

## ✨ Features

- 🔑 Login ID-based user identification
- ⌨️ Keystroke timing analysis
- 🧠 Behavioral biometric authentication
- 📊 Dwell time calculation
- ⏱️ Flight time calculation
- ⚡ Typing speed calculation
- 🕐 Total typing time calculation
- 💾 User profile storage using CSV
- 🖥️ Dark-themed Tkinter GUI
- ✅ Authentication success/failure detection
- 📋 Registered user viewing
- 🗑️ Dataset clearing option

---

## 🧠 How Keystroke Dynamics Works

Every person has a slightly different typing style.

The system records:

- When a key is pressed
- When a key is released
- Time between consecutive keystrokes
- Overall typing duration

These measurements are converted into numerical features and used to create the user's typing profile.

### Features Used

| Feature | Description |
|---|---|
| **Dwell Time** | Time for which a key remains pressed |
| **Flight Time** | Time between releasing one key and pressing the next |
| **Total Typing Time** | Total time taken to type the input |
| **Typing Speed** | Number of keystrokes typed per second |

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
 Store Typing Profile   Compare Profile
                             │
                             ▼
                    Authentication Decision
                       │              │
                       ▼              ▼
                    SUCCESS          FAILED
