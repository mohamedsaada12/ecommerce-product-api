# Ecommerce Product API
🛒 E-commerce Product API

This is a Django REST Framework (DRF) API for managing products in an e-commerce platform.
It provides CRUD operations for products and users, authentication, product search, filtering, and pagination.

🚀 Features

Product Management (CRUD): Create, Read, Update, and Delete products.

Fields: Name, Description, Price, Category, Stock Quantity, Image URL, Created Date

User Management (CRUD): Manage users with username, email, and password.

Authentication: Only authenticated users can manage products.

Search & Filtering: Search products by name or category, filter by price range, category, or stock.

Pagination: Paginated product lists for scalability.

🛠️ Tech Stack

Backend Framework: Django 5.x

API Framework: Django REST Framework (DRF)

Database: SQLite (default, can be swapped for PostgreSQL/MySQL)

Authentication: Django Auth (with optional JWT support)

📂 Project Structure
ecommerce-product-api/
│── ecommerce/       # Django project settings
│── products/        # Products app (models, views, serializers, urls)
│── manage.py        # Django management script
│── requirements.txt # Dependencies
│── db.sqlite3       # Database (local)

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/<your-username>/ecommerce-product-api.git
cd ecommerce-product-api

2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py migrate

5. Run the development server
python manage.py runserver

📌 API Endpoints
Method	Endpoint	Description	Auth Required
POST	/api/products/	Create new product	✅ Yes
GET	/api/products/	List all products (with pagination)	❌ No
GET	/api/products/{id}/	Retrieve product by ID	❌ No
PUT	/api/products/{id}/	Update product	✅ Yes
DELETE	/api/products/{id}/	Delete product	✅ Yes
GET	/api/products/search/	Search products by name/category	❌ No
POST	/api/users/	Register new user	❌ No
POST	/api/auth/login/	Login user (JWT or Session)	❌ No
🌟 Future Enhancements

Product reviews & ratings

Wishlist functionality

Discount & promotions system

Stock auto-reduction on orders

👨‍💻 Author

Mohamed Saada – Backend Developer
📧 My Email : mohamedsaada432@gmail.com
🔗 My LinkedIn : www.linkedin.com/in/mohamed-saada-61459b179
🔗 My GitHub profile : https://github.com/mohamedsaada12/ecommerce-product-api]
🔗 Portfolio: https://sites.google.com/view/mohamedsaada/home
