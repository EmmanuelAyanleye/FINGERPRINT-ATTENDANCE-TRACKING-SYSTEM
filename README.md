# 🎯 Fingerprint-Based Attendance Tracking System

> A Django-powered application for secure and automated student attendance using fingerprint biometrics.  
> **Case Study:** ESPAM Formation University, Benin Republic.


---

## 📚 Project Overview

This system modernizes attendance management by integrating fingerprint verification. It eliminates proxy attendance, minimizes errors, and improves operational efficiency.

---

## 🛠️ Features

- Admin, Lecturer, and Student dashboards
- Fingerprint-based attendance marking
- Secure login authentication
- Real-time attendance tracking
- Attendance reports (PDF export)
- Timetable and course management
- Fingerprint enrollment and verification
- Local server deployment for testing and use

---

## 🚀 Technologies Used

- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Django (Python)
- **Database:** SQLite
- **Biometric Integration:** C# (DigitalPersona U.are.U 4500 SDK)
- **Server:** Local Django Development Server

---

## 🔐 Admin Login Credentials

- **Email:** `admin@gmail.com`  
- **Password:** `admin`

---

## 📦 Setup Instructions

### Prerequisites

- Python 3.10+
- Django 4.x
- SQLite
- Visual Studio (for C# biometric integration)
- DigitalPersona SDK
- U.are.U 4500 Fingerprint Scanner

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/EmmanuelAyanleye/FINGERPRINT-ATTENDANCE-TRACKING-SYSTEM.git
cd your-repository

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Start the local server
python manage.py runserver
```

Open your browser and visit: [http://127.0.0.1:8000/admin_dashboard/](http://127.0.0.1:8000/admin_dashboard/)

---

## 🖐️ Fingerprint Scanner Integration

- Built using **C#** with the **DigitalPersona SDK**.
- Captures and verifies fingerprints.
- Fingerprint data is securely stored in Base64 format inside the database.

> Ensure the DigitalPersona U.are.U 4500 scanner is properly connected before enrolling or verifying fingerprints.

---

## 🏠 System Architecture

| Layer            | Technology                                |
| :--------------- | :---------------------------------------- |
| Presentation     | HTML, CSS, JavaScript, Bootstrap          |
| Application      | Django                                    |
| Data             | SQLite                                    |
| Biometric        | C# with DigitalPersona Fingerprint SDK    |

---

## 📸 Screenshots

| Admin Dashboard | Attendance Report | List of Students |
| :-------------- | :----------------- | :--------------- |
| ![Admin Dashboard](https://github.com/user-attachments/assets/b2fe7723-e371-47e7-ad7e-b837281b91d4) | ![Attendance Report](https://github.com/user-attachments/assets/dcd93724-6016-4cd5-9488-4ebaec5dacc9) | ![List of Students](https://github.com/user-attachments/assets/17e9dc6d-6c3a-4294-92ac-f50d99353a72) |

| Login Page | Add Student |
| :--------- | :----------- |
| ![Login Page](https://github.com/user-attachments/assets/a5f5ea58-bb09-48a8-b3ce-ffa9c1e79f5b) | ![Add Student](https://github.com/user-attachments/assets/416a6d5e-a919-4d2b-953a-ffe580d25694) |

---

## 📈 Future Improvements

- Deployment to cloud servers (AWS, Azure, or Heroku)
- Mobile application version (Android/iOS)
- Multi-biometric support (Face + Fingerprint)
- SMS notifications for attendance updates

---

## 👨‍💻 Developer Information

| Field              | Information                                                              |
| :----------------- | :----------------------------------------------------------------------- |
| **Name**           | AYANLEYE EMMANUEL IYANUOLUWA                                              |
| **Matric No**      | ESPAM/CSC/22/1005                                                         |
| **Course**         | COMPUTER SCIENCE                                                         |
| **Institution**    | ESPAM-FORMATION UNIVERSITY                                               |
| **Skill(s)**       | UI/UX Designer (Intermediate), Frontend Developer (Intermediate)         |
| **Year of Study**  | 2022                                                                     |
| **Project Title**  | DESIGN AND IMPLEMENTATION OF STUDENT ATTENDANCE MONITORING SYSTEM USING FINGERPRINT |
| **Duration**       | 7 Months                                                                 |
| **Supervisor**     | DR. VICTOR POPOOLA                                                       |
| **Graduating Class** | CLASS OF 2025!!!                                                      |


---

# 🌟 Thank you for checking out this project!

---
