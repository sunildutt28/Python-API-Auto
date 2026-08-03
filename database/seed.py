from database.database import SessionLocal
from models.user import User

session = SessionLocal()

try:

    existing = session.query(User).filter(User.id == 1).first()

    if not existing:

        user = User(
            id=1,
            first_name="Emily",
            last_name="Johnson",
            email="emily.johnson@x.dummyjson.com"
        )

        session.add(user)
        session.commit()

        print("User inserted.")

    else:

        print("User already exists.")

finally:

    session.close()