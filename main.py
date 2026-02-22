"""
Simple Book API with FastAPI.
"""

import shutil
from datetime import datetime
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, File, Form, Query, UploadFile
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

app = FastAPI(title="Book API")

# Setup uploads directory
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
app.mount("/images", StaticFiles(directory="uploads"), name="images")

# In-memory storage
books_db: list[dict] = []
book_id_counter: int = 1


class Book(BaseModel):
    """Book model with Pydantic validation."""
    
    id: Optional[int] = None
    title: str = Field(..., min_length=3, max_length=100)
    author: str
    publisher: str
    image_url: Optional[str] = None
    created_at: Optional[str] = None


@app.post("/books")
async def create_book(
    title: str = Form(..., min_length=3, max_length=100),
    author: str = Form(...),
    publisher: str = Form(...),
    image: UploadFile = File(...)
) -> dict:
    """Create a new book with image upload."""
    global book_id_counter
    
    # Save image
    ext = Path(image.filename).suffix
    filename = f"book_{book_id_counter}{ext}"
    filepath = UPLOAD_DIR / filename
    
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    # Create book
    book = Book(
        id=book_id_counter,
        title=title,
        author=author,
        publisher=publisher,
        image_url=f"/images/{filename}",
        created_at=datetime.now().isoformat()
    )
    
    books_db.append(book.model_dump())
    book_id_counter += 1
    
    return {"success": True, "data": book}


@app.get("/books/search")
def search_books(
    query: str = Query(..., min_length=3, max_length=100),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100)
) -> dict:
    """Search books by title, author, or publisher with pagination."""
    q = query.lower()
    
    # Filter
    filtered = [
        b for b in books_db
        if q in b["title"].lower() 
        or q in b["author"].lower() 
        or q in b["publisher"].lower()
    ]
    
    # Paginate
    total = len(filtered)
    start = (page - 1) * page_size
    end = start + page_size
    items = filtered[start:end]
    
    return {
        "success": True,
        "data": {
            "books": items,
            "pagination": {
                "page": page,
                "page_size": page_size,
                "total": total,
                "total_pages": (total + page_size - 1) // page_size
            }
        }
    }