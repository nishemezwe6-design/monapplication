from fastapi import FastAPI, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Product
import models
import shutil
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

if not os.path.exists("uploads"):
    os.makedirs("uploads")

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.post("/products")
async def create_product(
    name:str = Form(...),
    price:int = Form(...),
    description:str = Form(...),
    image:UploadFile = File(...)
):

    filepath = f"uploads/{image.filename}"

    with open(filepath,"wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    db = SessionLocal()

    product = Product(
        name=name,
        price=price,
        description=description,
        image_url=filepath
    )

    db.add(product)
    db.commit()

    return {"message":"Produit ajouté"}

@app.get("/products")
def get_products():

    db = SessionLocal()

    products = db.query(Product).all()

    return products