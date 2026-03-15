from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

DATABASE_URL = "postgresql://postgres:root@localhost:5432/yt_01"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

# TEST CONNECTION
if __name__ == "__main__":
    try:
        db = SessionLocal()
        print("Connection to the database was successful!")
        # users = db.execute(text("SELECT * FROM users")).fetchall()
        users = db.execute(text("SELECT * FROM users")).mappings().all()
        print(f"Users in the database: {users}")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
    finally:
        db.close()
