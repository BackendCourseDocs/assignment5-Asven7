# 📚 Book API (FastAPI)

A simple Book Management API built with **FastAPI**.

This project supports:
- 📖 Create book with image upload
- 🔍 Search books (by title, author, publisher)
- 📄 Pagination
- 🖼 Static image serving

---

## 🚀 Features

- FastAPI backend
- Image upload support
- In-memory database
- Pagination system
- Pydantic validation
- Clean project structure
- requirements.txt support

---

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/BackendCourseDocs/assignment5-Asven7
cd book-api
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows
```bash
venv\Scripts\activate
```

### Linux / Mac
```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Server

```bash
uvicorn main:app --reload
```

Server will run at:  
http://127.0.0.1:8000

Interactive API docs:
- Swagger UI → http://127.0.0.1:8000/docs
- ReDoc → http://127.0.0.1:8000/redoc

---

## 📂 Project Structure

```
book-api/
│
├── main.py
├── requirements.txt
├── uploads/
└── README.md
```

---

## 📌 API Endpoints

### 🔹 Create Book

**POST /books**

Form Data:
- title
- author
- publisher
- image (file upload)

---

### 🔹 Search Books

**GET /books/search**

Query Parameters:
- query (min 3 chars)
- page (default: 1)
- page_size (default: 10)

Example:
```
/books/search?query=harry&page=1&page_size=5
```

---

## 🖼 Image Access

Uploaded images are available at:

```
/images/{filename}
```

Example:
```
http://127.0.0.1:8000/images/book_1.jpg
```

---

## 📌 Future Improvements

- Add SQLite or PostgreSQL database
- Add authentication (JWT)
- Add delete/update endpoints
- Add Docker support
- Add unit tests (pytest)
- Add CI/CD

---

## 👨‍💻 Author

Ali Ayoumnan  
GitHub: https://github.com/Asven7