from faker import Faker
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.user import User

fake = Faker()

def seed_users(db: Session, num_users: int = 10):
    db.query(User).delete()
    db.commit()
    for _ in range(num_users):
        name = fake.name()
        email = fake.unique.email()
        password = fake.password(length=12)

        user = User(
            name=name,
            email=email,
            hashed_password=password,  
            is_active=True
        )
        db.add(user)
    db.commit()
    print(f"Seeded {num_users} users to the database.")

if __name__ == "__main__":
    db = SessionLocal()
    try:
        seed_users(db, num_users=100)
    except Exception as e:
        print(f"Error seeding users: {e}")
    finally:
        db.close()