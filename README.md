<<<<<<< HEAD
# DevOps-Engineer-Assessment-by-Better
=======
# Task Tracker

A minimal Flask web application to track tasks. Suitable for CI/CD pipeline demos and easy deployment on Render.

## Features
- List all tasks (in-memory)
- Add new tasks
- Delete tasks

## Setup & Run Locally

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the app:**
   ```bash
   python app.py
   ```
3. **Visit:**
   Open [http://localhost:5000](http://localhost:5000) in your browser.

## Deploy on Render
1. Push this repo to GitHub.
2. Create a new Web Service on [Render](https://render.com/).
3. Set the build and start commands:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
4. Set environment to Python 3.7+.

## Folder Structure
```
DevOps Assignment/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    ├── index.html
    └── add.html
```

---

**Note:** Tasks are stored in memory and will reset on app restart. 
>>>>>>> bca6d02 (Flask Appliation)
