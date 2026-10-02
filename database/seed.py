# e.g. scripts/create_user.py  (or main.py at project root)
from database.database import SessionLocal, engine
from database.repository import UserRepository
from models.user import User

def create_user_2() -> None:
    session = SessionLocal()
    try:
        existing = session.query(User).filter(User.id == 2).first()

        if existing:
            print("User already exists. Updating first name to Michael.")
            existing.first_name = "Michael"  
            existing.last_name = "Williams"
            existing.email = "michael.williams@x.dummyjson.com"   # just assign — ORM tracks the change
            session.commit()                    # UPDATE is issued here
            return

        user = User(
            id=2,
            first_name="Nancy",
            last_name="Johnson",
            email="nancy.johnson@x.dummyjson.com",
        )
        session.add(user)
        session.commit()
        print("User inserted.")

    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":
    create_user_2()