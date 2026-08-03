from database.database import engine
from models.user import Base

Base.metadata.create_all(engine)

print("Database created successfully.")