# Host Fitness Test Application

A simple Flask web application that displays host system information. Perfect for learning Docker and Flask basics.

## 🎯 Overview

This application shows:
- Hostname of your machine
- Operating System details
- OS Release version
- Beautiful fitness-themed UI

## 📋 Prerequisites

Before you begin, make sure you have the following installed on your macBook:

- **Python 3.7+** - [Download](https://www.python.org/downloads/)
- **pip** - Usually comes with Python
- **Git** - [Download](https://git-scm.com/download/mac)
- **Docker** (optional, for containerization) - [Download](https://www.docker.com/products/docker-desktop)

## 🚀 Local Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/ytiwari41/docker-projects.git
cd docker-projects/host-fitness-app
```

### Step 2: Create a Virtual Environment

```bash
python3 -m venv venv
```

### Step 3: Activate the Virtual Environment

```bash
source venv/bin/activate
```

You should see `(venv)` at the beginning of your terminal prompt.

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python app.py
```

You should see output like:
```
 * Running on http://0.0.0.0:8080
```

### Step 6: Access the Application

Open your web browser and navigate to:

```
http://localhost:8080
```

You should see the Host Fitness Test page displaying your system information.

## 🐳 Docker Setup (Optional)

If you prefer to run this in a Docker container:

### Build the Docker Image

```bash
docker build -t host-fitness-app .
```

### Run the Docker Container

```bash
docker run -p 8080:8080 host-fitness-app
```

Then access the application at `http://localhost:8080`

## 📁 Project Structure

```
host-fitness-app/
├── app.py                 # Flask application
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── static/
    └── images/
        └── fitness.png    # UI image
```

## 🛑 Stop the Application

To stop the running application:
- Press `Ctrl + C` in your terminal

To deactivate the virtual environment:
```bash
deactivate
```

## 📝 Technologies Used

- **Flask** - Python web framework
- **Docker** - Containerization (optional)

## 🎓 Learning Resources

This project is great for learning:
- Python web development with Flask
- Docker basics
- Web application deployment
- Git and version control

## ❓ Troubleshooting

**Port 8080 already in use?**
```bash
python app.py  # Change port or kill the process using 8080
```

**Virtual environment not activating?**
Make sure you're in the project directory and run:
```bash
source venv/bin/activate
```

**Module not found errors?**
Ensure the virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

## 📄 License

This project is for learning purposes only.

---

**Created by:** Yogendra Tiwari 🇮🇳
