# JOB ALERT

A desktop application project developed using Python and MySQL to help job seekers find employment and assist employers in finding suitable candidates. This project was submitted as the **Computer Science (083) Project Report** for the **All India Senior School Certificate Examination (AISSCE) – 2022-23**.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Technologies Used](#technologies-used)
- [Project Design (SDLC)](#project-design-sdlc)
- [Installation and Setup](#installation-and-setup)
- [Future Development Areas](#future-development-areas)
- [Team](#team)
- [License](#license)

---

## Project Overview

The **JOB ALERT** system is designed to act as a dual platform for job searching. [cite_start]It focuses on connecting **Employers** with qualified **Job Seekers**[cite: 63, 64].

### For Employers
* [cite_start]Allows searching and viewing employee profiles[cite: 64, 68].
* [cite_start]Helps start-up companies find employees quickly[cite: 67, 69].
* [cite_start]Provides a **Request Page** to create and manage job postings with details like job title, qualification, and salary[cite: 1085, 1086, 1087, 1106, 1111, 1116].

### For Job Seekers
* [cite_start]Allows viewing various job offers and opportunities from employers[cite: 72, 74].
* [cite_start]Enables applying for jobs and sending resumes based on skill sets/qualification[cite: 72, 74].
* [cite_start]The main motive is to help freshers and others find their respective jobs[cite: 1526, 1527].
* [cite_start]Includes a **Resume Making** feature as part of the implementation[cite: 328].

---

## Features

The application includes the following core components and functionalities:

* [cite_start]**Sign-Up/Sign-In:** Separate flows for new user registration and existing user login[cite: 316, 318].
* [cite_start]**OTP Verification:** Phone number verification is performed using a One-Time Password (OTP) via the **Twilio API**[cite: 681, 685, 1260, 1539].
* [cite_start]**Email Verification:** Email verification is performed using the **smtplib** library[cite: 865, 1261, 1332, 1537].
* [cite_start]**Role Selection:** Users choose their role as an **Employee** (Job Seeker) or **Employer** during sign-up[cite: 723, 727].
* [cite_start]**User/Employer Pages:** Dedicated pages for viewing job profiles/listings[cite: 321, 323].
* [cite_start]**Database Integration:** Uses **MySQL** for robust data management[cite: 101].

---

## System Requirements

The following software and hardware specifications are recommended for running the project smoothly:

| Category | Recommended Requirements | Minimum Requirements |
| :--- | :--- | :--- |
| **Processor** | Intel® Core™ i3 processor 4300M at 2.60 GHz | [cite_start]Intel Atom® processor or Intel® Core™ i3 processor [cite: 78, 84] |
| **Disk Space** | [cite_start]2 to 4 GB [cite: 79] | [cite_start]1 GB [cite: 85] |
| **Operating System** | [cite_start]Windows® 10, / MAC OS / UBUNTU [cite: 80] | [cite_start]Windows 7 or later / MAC OS / UBUNTU [cite: 86] |
| **Python Version** | [cite_start]3.X.X or Higher [cite: 81] | [cite_start]3.8.X [cite: 87] |
| **Database** | [cite_start]MySQL- 8.0.X [cite: 82] | [cite_start]MySQL- 8.0.X [cite: 88] |

[cite_start]**Note:** Python must be installed and added to the system's PATH for successful execution[cite: 91, 92].

---

## Technologies Used

| Technology | Role |
| :--- | :--- |
| **Python** | [cite_start]High-level, interpreted language for the core application logic and backend[cite: 96]. |
| **Tkinter** | [cite_start]Python library used for creating the Graphical User Interface (GUI)[cite: 332, 1540]. |
| **MySQL** | [cite_start]Relational Database Management System (RDBMS) for storing and managing user, employer, and job request data[cite: 101, 1263]. |
| **Twilio** | [cite_start]Third-party service used for generating and sending OTPs for phone verification[cite: 1260, 1539]. |
| **smtplib** | [cite_start]Python standard library used for sending emails for mail verification[cite: 1261, 1537]. |
| **openpyxl** | [cite_start]Python library used for reading and writing to the Resume Excel file[cite: 1264, 1467]. |

---

## Project Design (SDLC)

[cite_start]The project followed the **System Development Life Cycle (SDLC)** methodology[cite: 148, 149]. The key phases involved were:

1.  [cite_start]**Requirements Analysis:** Defining detailed functional user requirements, data requirements, system performance, security, and maintainability needs[cite: 221, 224].
2.  **Design:** Converting requirements into unified design specifications. [cite_start]This included designing the program structure, application screens, and database layouts[cite: 240, 244].
3.  [cite_start]**Development:** Converting the design specifications into executable Python programs (code implementation)[cite: 270].
4.  [cite_start]**Testing:** Included unit testing, system testing, security testing, and user acceptance testing[cite: 281, 282, 289].
5.  [cite_start]**Maintenance:** The ongoing operation, monitoring, and incorporating system modifications for continued performance[cite: 304, 306].

[cite_start]The user interface was designed around key functional windows: Sign-up, Sign-in, OTP verification, Employee Page, Employer Page, and the Resume Making Page[cite: 316, 318, 321, 323, 328, 696].

---

## Installation and Setup

To run the project locally, you need to set up the Python environment and the MySQL database.

### 1. Database Setup

1.  [cite_start]Install **MySQL Server (version 8.0.X)**[cite: 82, 88].
2.  Log in to the MySQL command-line client.
3.  Create the database: `CREATE DATABASE jobalert;`
4.  The backend code connects with the following credentials (modify as needed in `backend.py`):
    * `host='localhost'`
    * `user='root'`
    * `password='Sch00l@'`
    * [cite_start]`database='jobalert'` [cite: 1266, 1313, 1351, 1359, 1367, 1383, 1400, 1408, 1418, 1436, 1444, 1451, 1459, 1469, 1502]
5.  The backend implicitly uses `employee`, `employer`, and `request` tables. You will need to execute the schema setup queries (not provided in the documentation) or allow the application to create initial tables on first run, depending on the full setup script.

### 2. Python Environment Setup

1.  [cite_start]Ensure **Python (3.8.X or higher)** is installed[cite: 81, 87].
2.  Install required Python libraries:
    ```bash
    pip install mysql-connector-python
    pip install twilio
    pip install openpyxl
    ```
    *(Note: `tkinter` and `smtplib` are usually included with Python's standard installation)*[cite: 1260, 1261, 1263, 1264].

### 3. Run the Application

Execute the main frontend file:

```bash
python frontend.py # or the equivalent filename for the main GUI code
