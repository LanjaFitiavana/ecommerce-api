# 🛒 Ecommerce API

> A professional backend API for e-commerce platforms, powered by **Django REST Framework** and **PostgreSQL**.

---

## 📋 Table of Contents

- [Description](#-description)
- [Technologies Used](#-technologies-used)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Running the Project](#-running-the-project)
- [API Endpoints](#-api-endpoints)
- [Documentation & Tests](#-documentation--tests)
- [Author](#-author)

---

## 📌 Description

This REST API provides a robust architecture for managing an online store:
- **Product Management**: Full CRUD for items and categories.
- **Security**: Stateless authentication via **JWT** (JSON Web Tokens).
- **Orders**: Order processing system and shopping cart logic.
- **Production-Ready**: Optimized configuration for deployment (WhiteNoise, environment variables).

---

## 🛠 Technologies Used

| Technology | Version | Role |
| :--- | :--- | :--- |
| **Python** | 3.10+ | Core Language |
| **Django** | 5.2.x | Web Framework |
| **Django REST Framework** | 3.16+ | API Construction |
| **PostgreSQL** | 14+ | Relational Database |
| **SimpleJWT** | 5.5+ | Authentication Management |
| **WhiteNoise** | 6.11+ | Static Files Serving |

---

## ✅ Prerequisites

Before getting started, ensure you have the following installed:
- [Python 3.10+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Git](https://git-scm.com/)

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone [https://github.com/LanjaFitiavana/ecommerce-api.git](https://github.com/LanjaFitiavana/ecommerce-api.git)
cd ecommerce-api



2. Create virtual environment
Bash
# Creation
python -m venv env

# Activation (Windows)
env\Scripts\activate

# Activation (Mac/Linux)
source env/bin/activate



3. Install dependencies
Bash

pip install -r requirements.txt



⚙️ Configuration

Create a .env file in the root directory and configure your variables:
Extrait de code

# Django Settings
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings
DB_NAME=ecommerce_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432



🚀 Running the Project
Bash

# 1. Apply database migrations
python manage.py migrate

# 2. Create an admin account
python manage.py createsuperuser

# 3. Start the development server
python manage.py runserver



🔗 Production Base URL: https://ecommerces-api3.onrender.com
🔗 API Endpoints
🔐 Authentication
Method	Endpoint	Description
POST	/users/register/	Register a new user
POST	/users/login/	Login and obtain JWT token
POST	/users/refresh/	Refresh access token


📦 Products
Method	Endpoint	Description
GET	/products/	List all products
GET	/products/{id}/	Get specific product details
POST	/products/	Create a product (Admin only)
DELETE	/products/{id}/	Delete a product


🛒 Orders
Method	Endpoint	Description
POST	/orders/	Place a new order
GET	/orders/{id}/	View order details
🧪 Documentation & Tests




The API is fully documented with Swagger. You can test the endpoints directly from your browser:

    Swagger UI: https://ecommerces-api3.onrender.com/api/docs/

    Redoc: https://ecommerces-api3.onrender.com/api/redoc/

Run automated tests:
Bash

python manage.py test





👤 Author

    GitHub: LanjaFitiavana

    Email: 010rabeza@gmail.com