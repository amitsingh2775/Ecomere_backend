#  Ecommerce Backend - FastAPI + MongoDB

This is a simple backend API built using **FastAPI** and **MongoDB**. It simulates a basic e-commerce system with two main features:

- **Product Management** (Add/List products)
- **Order Management** (Create/List orders by user)

---
## ScreenShots

    <img width="1760" height="861" alt="image" src="https://github.com/user-attachments/assets/84f2364d-d80b-4512-b608-816e9c584bb6" />

    <img width="1657" height="952" alt="image" src="https://github.com/user-attachments/assets/3f5045da-24d5-4050-a506-890660d5b5fe" />
    <img width="1698" height="924" alt="image" src="https://github.com/user-attachments/assets/a41164c0-d4b9-46a2-bebd-c6a6966fb12e" />



##  Features

- Create and list products with filters
- Place orders with a list of product IDs
- Fetch all orders by user ID
- MongoDB integration using `motor` (async MongoDB client)

---

##  Tech Stack

- **Python** (3.11+)
- **FastAPI**
- **MongoDB Atlas**
- **Motor** (MongoDB async driver)
- **Uvicorn** (for local development)

---


---

##  Installation & Run Locally

```bash
# Clone the repo
git clone <repo-url>
cd ecommerce-backend

# Create virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your MongoDB URI in .env
MONGO_URL=your_mongodb_uri

# Run server
uvicorn app.main:app --reload


