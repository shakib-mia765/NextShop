# 🛒 NextShop

> Enterprise-grade Full Stack E-Commerce Platform built with React, Vite, Django, Redux Toolkit, and REST APIs.

![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)
![Vite](https://img.shields.io/badge/Vite-Latest-646CFF?logo=vite)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python)
![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django)
![Redux Toolkit](https://img.shields.io/badge/Redux-Toolkit-764ABC?logo=redux)
![License](https://img.shields.io/badge/License-MIT-green)

---

# Overview

NextShop is a modular full-stack e-commerce platform designed with a clean separation between frontend, backend, business logic, payment processing, seller operations, customer experience, and administration.

The project demonstrates modern software engineering practices by combining a React frontend with a Django backend to deliver a scalable shopping experience supporting customers, sellers, and administrators from a single codebase.

---

# Highlights

- Full Stack Architecture
- Modular Django Backend
- React + Vite Frontend
- Redux Toolkit State Management
- REST API Driven Design
- AI Product Feed
- Smart Search
- Voice Search
- Recommendation Engine
- Seller Dashboard
- Admin Dashboard
- Order Management
- Shopping Cart
- Wishlist
- Review System
- Customer Profiles
- Notification Center
- Multiple Payment Architecture
- Docker Ready

---

# Architecture

```
React + Redux Toolkit
        │
        ▼
 REST API Layer
        │
        ▼
 Django REST Backend
        │
 ┌──────┼─────────┐
 │      │         │
Products Orders Payments
 │      │         │
Users Sellers Categories
        │
        ▼
 SQLite / PostgreSQL
```

---

# Backend

```
User
Seller
Products
Category
Cart
CartItem
Order
OrderItem
Payment
```

---

# Frontend

```
Authentication
Products
Cart
Checkout
Payment
Orders
Seller Dashboard
Admin Dashboard
AI Recommendation
Smart Search
Voice Search
Wishlist
Reviews
```

---

# Technology Stack

## Frontend

- React
- Vite
- JavaScript
- Redux Toolkit
- CSS

## Backend

- Python
- Django
- Django REST Framework

## Database

- SQLite
- PostgreSQL Ready

## DevOps

- Docker
- Git
- GitHub

---

# Folder Structure

```
NextShop
│
├── Django Backend
├── React Frontend
├── Public Assets
├── Redux Toolkit
├── Shared API Layer
├── Smart Search
└── AI Components
```

---

# Getting Started

## Clone

```bash
git clone https://github.com/shakib-mia765/NextShop.git
```

## Frontend

```bash
npm install
npm run dev
```

## Backend

```bash
cd Nextshop
python -m venv venv
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

# Roadmap

- Stripe
- PayPal
- bKash
- Nagad
- Redis
- Elasticsearch
- Docker Compose
- Kubernetes
- AWS Deployment
- CI/CD
- Unit Testing
- Integration Testing

---

# Repository Goals

- Scalable Architecture
- Modular Design
- Clean Code
- Maintainability
- Performance
- Extensibility

---

# Author

## Shakib Mia

**Senior Full Stack Engineer**

I specialize in designing and building scalable full-stack web applications using Python, Django, React, JavaScript, and modern cloud-native development practices. My focus is on clean architecture, maintainable codebases, API-driven systems, and delivering reliable software solutions.

**Core Skills**

- Python
- Django
- Django REST Framework
- React
- JavaScript
- Redux Toolkit
- REST APIs
- SQL
- Docker
- Git & GitHub

**GitHub**

https://github.com/shakib-mia765

---

# License

Licensed under the MIT License.
NextShop/

│

├── Nextshop.venv/

│

├── Nextshop/

│   ├── manage.py

│   ├── db.sqlite3

│   │

│   ├── Nextshop/

│   │   ├── **init**.py

│   │   ├── asgi.py

│   │   ├── settings.py

│   │   ├── urls.py

│   │   └── wsgi.py

│   │

│   ├── user/

│   │   ├── migrations/

│   │   │   └── **init**.py

│   │   ├── **init**.py

│   │   ├── admin.py

│   │   ├── apps.py

│   │   ├── models.py

│   │   ├── serializers.py

│   │   ├── tests.py

│   │   ├── urls.py

│   │   └── views.py

│   │

│   ├── seller/

│   │   ├── migrations/

│   │   │   └── **init**.py

│   │   ├── **init**.py

│   │   ├── admin.py

│   │   ├── apps.py

│   │   ├── models.py

│   │   ├── serializers.py

│   │   ├── tests.py

│   │   ├── urls.py

│   │   └── views.py

│   │

│   ├── category/

│   │   ├── migrations/

│   │   │   └── **init**.py

│   │   ├── **init**.py

│   │   ├── admin.py

│   │   ├── apps.py

│   │   ├── models.py

│   │   ├── serializers.py

│   │   ├── tests.py

│   │   ├── urls.py

│   │   └── views.py

│   │

│   ├── products/

│   │   ├── migrations/

│   │   │   └── **init**.py

│   │   ├── **init**.py

│   │   ├── admin.py

│   │   ├── ai\_service.py

│   │   ├── apps.py

│   │   ├── models.py

│   │   ├── serializers.py

│   │   ├── support\_api.py

│   │   ├── tests.py

│   │   ├── urls.py

│   │   └── views.py

│   │

│   ├── cart/

│   │   ├── migrations/

│   │   │   └── **init**.py

│   │   ├── **init**.py

│   │   ├── admin.py

│   │   ├── apps.py

│   │   ├── models.py

│   │   ├── serializers.py

│   │   ├── tests.py

│   │   ├── urls.py

│   │   └── views.py

│   │

│   ├── cartitem/

│   │   ├── migrations/

│   │   │   └── **init**.py

│   │   ├── **init**.py

│   │   ├── admin.py

│   │   ├── apps.py

│   │   ├── models.py

│   │   ├── serializers.py

│   │   ├── tests.py

│   │   ├── urls.py

│   │   └── views.py

│   │

│   ├── order/

│   │   ├── migrations/

│   │   │   └── **init**.py

│   │   ├── **init**.py

│   │   ├── admin.py

│   │   ├── apps.py

│   │   ├── models.py

│   │   ├── serializers.py

│   │   ├── services.py

│   │   ├── tests.py

│   │   ├── urls.py

│   │   └── views.py

│   │

│   ├── orderitem/

│   │   ├── migrations/

│   │   │   └── **init**.py

│   │   ├── **init**.py

│   │   ├── admin.py

│   │   ├── apps.py

│   │   ├── models.py

│   │   ├── serializers.py

│   │   ├── tests.py

│   │   ├── urls.py

│   │   └── views.py

│   │

│   └── payment/

│       ├── migrations/

│       │   └── **init**.py

│       ├── **init**.py

│       ├── admin.py

│       ├── apps.py

│       ├── constants.py

│       ├── models.py

│       ├── registry.py

│       ├── serializers.py

│       ├── strategies.py

│       ├── tests.py

│       ├── urls.py

│       └── views.py

│

├── public/

│   ├── favicon.svg

│   └── icons.svg

│

├── src/

│   ├── app/

│   │   └── store.js

│   │

│   ├── assets/

│   │   ├── hero.png

│   │   ├── react.svg

│   │   └── vite.svg

│   │

│   ├── components/

│   │   ├── dashboard/

│   │   │   ├── AboutUs.jsx

│   │   │   ├── DealOfDay.jsx

│   │   │   ├── Footer.jsx

│   │   │   ├── Header.jsx

│   │   │   └── PromoBanner.jsx

│   │   ├── ProductCard.jsx

│   │   ├── ProductDetails.jsx

│   │   ├── ProductGrid.jsx

│   │   ├── SupportChat.jsx

│   │   └── VoiceSearch.jsx

│   │

│   ├── pages/

│   │   ├── admin/

│   │   │   ├── AdminDashboard.jsx

│   │   │   ├── ProductModeration.jsx

│   │   │   └── UserManagement.jsx

│   │   ├── seller/

│   │   │   ├── ProductUpload.jsx

│   │   │   ├── SellerAnalytics.jsx

│   │   │   ├── SellerDashboard.jsx

│   │   │   └── SellerProductList.jsx

│   │   ├── AccountPages.jsx

│   │   ├── AuthPage.jsx

│   │   ├── CartPage.jsx

│   │   ├── CheckoutPage.jsx

│   │   ├── Home.jsx

│   │   ├── OrdersPage.jsx

│   │   ├── PaymentPage.jsx

│   │   └── WishlistPage.jsx

│   │

│   ├── services/

│   │   ├── api.js

│   │   └── supportApi.js

│   │

│   ├── App.jsx

│   ├── index.css

│   └── main.jsx

│

├── .gitignore

├── Dockerfile

├── README.md

├── eslint.config.js

├── index.html

├── nginx.conf

├── package-lock.json

├── package.json

└── vite.config.js purtatre kmne aksathe run korabo
