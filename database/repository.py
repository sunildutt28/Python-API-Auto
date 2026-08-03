from database.database import SessionLocal
from models.user import User


class UserRepository:

    def get_user_by_id(self, user_id):

        session = SessionLocal()

        try:
            return session.query(User).filter(User.id == user_id).first()

        finally:
            session.close()