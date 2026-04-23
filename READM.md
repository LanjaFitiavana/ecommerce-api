# 🛒 Ecommerce API

> A professional backend API for an e-commerce platform, built with **Django REST Framework** and **PostgreSQL**.

---

## 📋 Table of Contents

- [Description](#description)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Tests](#tests)
- [Project Structure](#project-structure)
- [Author](#author)

---

## 📌 Description

This REST API provides full management of an e-commerce platform:
- Product and category management
- User authentication and account management
- Order and shopping 

---

## 🛠 Technologies Used

| Technology | Version | Role |
|---|---|---|
| Python | 3.10+ | Main language |
| Django | 4.x | Web framework |
| Django REST Framework | 3.x | API construction |
| PostgreSQL | 14+ | Database |
| JWT | - | Authentication |

---

## ✅ Prerequisites

Before getting started, make sure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [PostgreSQL 14+](https://www.postgresql.org/download/)
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ecommerce-api.git
cd ecommerce-api
```

### 2. Create and activate the virtual environment

```bash
# Create the environment
python -m venv env

# Activate on Windows
env\Scripts\activate

# Activate on Mac/Linux
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### 1. Create the `.env` file

Copy the example file and fill in the variables:

```bash
cp .env.example .env
```

### 2. Contents of the `.env` file

```env
# Django
SECRET_KEY=your_secret_key_here
DEBUG=True

# PostgreSQL Database
DB_NAME=ecommerce_db
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 3. Create the PostgreSQL database

```sql
CREATE DATABASE ecommerce_db;
```

---

## 🚀 Running the Project

```bash
# Apply migrations
python manage.py migrate

# Create a superuser (admin)
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

The API will be available at: **http://localhost:8000**

---

## 🔗 API Endpoints

### 🔐 Authentication
| Method | Endpoint | Description |
|---|---|---|
| POST | `/user/register/` | User registration |
| POST | `/users/login/` | Login (JWT token) |
| POST | `/users/refresh/` | Refresh (JWT token) |
| GET | `/users/list/` | List all users|

### 📦 Products
| Method | Endpoint | Description |
|---|---|---|
| GET | `/products/` | List all products |
| GET | `/products/{id}/` | Get product details |
| POST | `/products/` | Create a product  |
| PUT | `/products/{id}/` | Update a product  |
| DELETE | `//products/{id}/` | Delete a product |

### Orders
| Method | Endpoint | Description |
|---|---|---|
| POST | `/orders/` | Place an order |
| GET | `/orders/{id}/` | Get order details |

---

## 🧪 Tests

```bash
# Run all tests
python manage.py test



---

## 📁 Project Structure

```
ecommerce-api/
│
├── ecommerce/          # Main Django configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── products/           # Products app
├── orders/             # Orders app
├── users/              # Users app
│
├── requirements.txt    # Python dependencies
├── manage.py
└── README.md
```
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.x-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-316192?logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 👤 Author

- GitHub: https://github.com/LanjaFitiavana
- Email: 010rabeza@gmail.com


> 📝 *This project is developed for professional client/business use.*
