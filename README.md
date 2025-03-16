# **Blog API - Flask Backend**

This is a simple **Flask-based REST API** for managing blog posts. It provides functionality to **list, add, delete, update, and search** blog posts.

## **📌 Features**
- **List all posts** (`GET /api/posts`)
- **Add a new post** (`POST /api/posts`)
- **Delete a post** (`DELETE /api/posts/<id>`)
- **Update a post** (`PUT /api/posts/<id>`)
- **Search for posts** (`GET /api/posts/search?title=...&content=...`)
- **Sorting functionality** (`GET /api/posts?sort=title&direction=asc`)

## **⚙️ Setup & Run**

### **1️⃣ Clone the repository**
```bash
git clone https://github.com/dimitar27/masterblog-API.git
cd blog-api
```

### **2️⃣ Install dependencies**
```bash
pip install flask flask-cors
```

### **3️⃣ Run the backend**
```bash
python backend_app.py
```

### **4️⃣ Access the API**
```
http://127.0.0.1:5002/api/posts
```

## **🛠 Technologies Used**
- **Python** 🐍
- **Flask** 🔥
- **Flask-CORS** 🌍 (to allow frontend integration)

