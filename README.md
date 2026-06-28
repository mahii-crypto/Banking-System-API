# 🏦 Banking System API

A full-stack Banking System built using **Django REST Framework** for the backend and **React.js (Vite)** for the frontend. The application enables customer management, bank account management, deposits, withdrawals, and transaction tracking through a modern REST API.

---

## 🚀 Live Demo

**Frontend:**
https://banking-frontend-omega-ten.vercel.app

**Backend API:**
https://banking-system-api-ntid.onrender.com

---

## 📌 Features

* 👤 Customer Management

  * Create Customer
  * View Customers
  * Update Customer
  * Delete Customer

* 💳 Bank Account Management

  * Create Bank Account
  * View Accounts
  * Update Account Details
  * Delete Account

* 💰 Transactions

  * Deposit Money
  * Withdraw Money
  * Transaction History

* 🔍 Search Customers

* 🌐 RESTful APIs

* 📱 Responsive User Interface

---

## 🛠 Tech Stack

### Backend

* Python
* Django
* Django REST Framework
* SQLite
* Gunicorn
* Render

### Frontend

* React.js
* Vite
* Bootstrap 5
* Axios
* React Router
* Vercel

---

## 📂 Project Structure

```
Banking-System/

├── Banking-System-API/
│   ├── accounts/
│   ├── customers/
│   ├── transactions/
│   ├── config/
│   ├── manage.py
│   └── requirements.txt
│
└── banking-frontend/
    ├── src/
    │   ├── components/
    │   ├── pages/
    │   ├── services/
    │   └── assets/
    ├── package.json
    └── vite.config.js
```

---

## ⚙️ Backend Installation

```bash
git clone https://github.com/mahii-crypto/Banking-System-API.git

cd Banking-System-API

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

Backend runs at:

```
http://127.0.0.1:8000/
```

---

## ⚙️ Frontend Installation

```bash
git clone https://github.com/mahii-crypto/banking-frontend.git

cd banking-frontend

npm install

npm run dev
```

Frontend runs at:

```
http://localhost:5173/
```

---

## 📡 API Endpoints

### Customers

```
GET     /api/accounts/customers/
POST    /api/accounts/customers/
PUT     /api/accounts/customers/{id}/
DELETE  /api/accounts/customers/{id}/
```

### Bank Accounts

```
GET     /api/accounts/bank-accounts/
POST    /api/accounts/bank-accounts/
PUT     /api/accounts/bank-accounts/{id}/
DELETE  /api/accounts/bank-accounts/{id}/
```

### Transactions

```
GET     /api/accounts/transactions/
POST    /api/accounts/transactions/
```

---

## 📸 Screenshots

Add screenshots here after uploading them.

Example:

```
screenshots/

home.png
customers.png
accounts.png
transactions.png
deposit.png
withdraw.png
```

---

## 📈 Future Improvements

* JWT Authentication
* Role-based Access Control
* Email Notifications
* Dashboard Analytics
* Charts and Reports
* PostgreSQL Database
* Docker Support

---

## 👨‍💻 Author

**Manga Mahesh**

GitHub:
https://github.com/mahii-crypto

LinkedIn:
(Add your LinkedIn URL)

Email:
[mahiimahesh02@gmail.com](mailto:mahiimahesh02@gmail.com)

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
