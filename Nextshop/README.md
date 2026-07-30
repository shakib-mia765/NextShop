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
NextShop/ │ ├── Nextshop/ │ │ │ ├── Nextshop/ │ │ ├── __pycache__/ │ │ ├── DockerFile │ │ ├── _init_.py │ │ ├── asgi.py │ │ ├── settings.py │ │ ├── urls.py │ │ └── wsgi.py │ │ │ ├── cart/ │ │ ├── __pycache__/ │ │ ├── migrations/ │ │ ├── _init_.py │ │ ├── admin.py │ │ ├── apps.py │ │ ├── models.py │ │ ├── tests.py │ │ ├── urls.py │ │ └── views.py │ │ │ ├── cartitem/ │ │ ├── __pycache__/ │ │ ├── migrations/ │ │ ├── _init_.py │ │ ├── admin.py │ │ ├── apps.py │ │ ├── models.py │ │ ├── tests.py │ │ ├── urls.py │ │ └── views.py │ │ │ ├── category/ │ │ ├── __pycache__/ │ │ ├── migrations/ │ │ ├── _init_.py │ │ ├── admin.py │ │ ├── apps.py │ │ ├── models.py │ │ ├── tests.py │ │ ├── urls.py │ │ └── views.py │ │ │ ├── order/ │ │ ├── __pycache__/ │ │ ├── migrations/ │ │ ├── _init_.py │ │ ├── admin.py │ │ ├── apps.py │ │ ├── models.py │ │ ├── tests.py │ │ ├── urls.py │ │ └── views.py │ │ │ ├── orderitem/ │ │ ├── __pycache__/ │ │ ├── migrations/ │ │ ├── _init_.py │ │ ├── admin.py │ │ ├── apps.py │ │ ├── models.py │ │ ├── tests.py │ │ ├── urls.py │ │ └── views.py │ │ │ ├── payment/ │ │ ├── __pycache__/ │ │ ├── migrations/ │ │ ├── _init_.py │ │ ├── admin.py │ │ ├── apps.py │ │ ├── constants.py │ │ ├── models.py │ │ ├── registry.py │ │ ├── serializers.py │ │ ├── strategies.py │ │ ├── tests.py │ │ ├── urls.py │ │ └── views.py │ │ │ ├── products/ │ │ ├── __pycache__/ │ │ ├── migrations/ │ │ ├── DockerF │ │ ├── _init_.py │ │ ├── admin.py │ │ ├── apps.py │ │ ├── models.py │ │ ├── serializers api.py │ │ ├── tests.py │ │ ├── urls.py │ │ └── views.py │ │ │ ├── seller/ │ │ ├── __pycache__/ │ │ ├── migrations/ │ │ ├── _init_.py │ │ ├── admin.py │ │ ├── apps.py │ │ ├── models.py │ │ ├── tests.py │ │ ├── urls.py │ │ └── views.py │ │ │ ├── user/ │ │ ├── __pycache__/ │ │ ├── migrations/ │ │ ├── _init_.py │ │ ├── admin.py │ │ ├── apps.py │ │ ├── models.py │ │ ├── tests.py │ │ ├── urls.py │ │ └── views.py │ │ │ ├── db.sqlite3 │ └── manage.py │ ├── public/ │ ├── favicon.svg │ └── icons.svg │ ├── src/ │ │ │ ├── .devcontainer/ │ │ └── .devcontainer.json │ │ │ ├── Auth api/ │ │ ├── AI PRODUCT FEED ENGINE.js │ │ ├── FRONTEND API LAYER.js │ │ ├── PROMISE API LAYER.js │ │ ├── SHARED API LAYER.js │ │ └── UNIVERSAL API CLIENT.js │ │ │ ├── REDUX_TOOLKIT/ │ │ ├── REDUX │ │ ├── cartSlice.js │ │ └── store.js │ │ │ ├── assets/ │ │ ├── hero.png │ │ ├── react.svg │ │ └── vite.svg │ │ │ ├── components/ │ │ │ │ │ ├── Products/ │ │ │ ├── DockerFile │ │ │ ├── ProductList.jsx │ │ │ └── ProductPage.jsx │ │ │ │ │ ├── User/ │ │ │ ├── profile/ │ │ │ │ ├── ProfileAvatar.jsx │ │ │ │ ├── ProfileEditForm.jsx │ │ │ │ └── ProfileInfo.jsx │ │ │ │ │ │ │ ├── AuthLogin.jsx │ │ │ ├── LoginPage.jsx │ │ │ ├── NotificationCenter.jsx │ │ │ ├── OrderHistory.jsx │ │ │ ├── Profile.jsx │ │ │ └── Register.jsx │ │ │ │ │ ├── cart/ │ │ │ ├── Cart.jsx │ │ │ ├── CartDrawer.jsx │ │ │ ├── CartItem.jsx │ │ │ ├── CartPage.jsx │ │ │ ├── CartSummary.jsx │ │ │ └── cartSlice.jsx │ │ │ │ │ ├── dashboard/ │ │ │ ├── AboutUs.jsx │ │ │ ├── AiChat.jsx │ │ │ ├── AppShell.jsx │ │ │ ├── DealOfDay.jsx │ │ │ ├── Error.jsx │ │ │ ├── Footer.jsx │ │ │ ├── Header.jsx │ │ │ ├── Invoice.jsx │ │ │ ├── Loader.jsx │ │ │ ├── Pagination.jsx │ │ │ ├── PromoBanner.jsx │ │ │ ├── RecommendationEngine.jsx │ │ │ ├── SmartFilter.jsx │ │ │ └── SupportChat.jsx │ │ │ │ │ ├── search tech/ │ │ │ ├── AdvancedSearch.jsx │ │ │ ├── LocationBar.jsx │ │ │ ├── NavBar.jsx │ │ │ ├── Redis Search Suggestion Cache.jsx │ │ │ ├── SearchBar.jsx │ │ │ └── Voice Search.jsx │ │ │ │ │ ├── CategoryRow.jsx │ │ ├── CategorySidebar.jsx │ │ ├── ProductCard.jsx │ │ ├── ProductCarousel.jsx │ │ ├── ProductDetails.jsx │ │ ├── ProductFilter.jsx │ │ ├── ProductGrid.jsx │ │ └── SmartProductFeed.jsx │ │ │ ├── pages/ │ │ │ │ │ ├── Payment/ │ │ │ ├── CheckoutButton.jsx │ │ │ ├── PaymentFailed.jsx │ │ │ ├── PaymentStatus.jsx │ │ │ └── PaymentSuccess.jsx │ │ │ │ │ ├── admin/ │ │ │ ├── AdminDashboard.jsx │ │ │ ├── AdminPanel.jsx │ │ │ ├── GlobalDataProvider.jsx │ │ │ ├── LiveOrderTracker.jsx │ │ │ ├── ProductModeration.jsx │ │ │ └── UserManagement.jsx │ │ │ │ │ ├── order/ │ │ │ ├── OrderList.jsx │ │ │ ├── OrderTracking.jsx │ │ │ ├── Rating.jsx │ │ │ ├── Review.jsx │ │ │ └── Wishlist.jsx │ │ │ │ │ └── Home.jsx │ │ │ ├── selller/ │ │ ├── ProductUpload.jsx │ │ ├── SellerAnalytics.jsx │ │ ├── SellerDashboard.jsx │ │ ├── SellerProductList.jsx │ │ └── SellerStats.jsx │ │ │ ├── services/ │ │ ├── api Layer.js │ │ └── api.js │ │ │ ├── App.css │ ├── App.jsx │ ├── index.css │ └── main.jsx │ ├── .gitignore ├── README.md ├── eslint.config.js ├── index.html ├── package-lock.json ├── package.json └── vite.config.js
