from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user import UserRepository
from app.core.security import hash_password

class UserService:
    @staticmethod
    def create_user(db: Session, email: str, password: str) -> User:

        existing = UserRepository.get_by_email(db, email)
        if existing:
            raise ValueError("Email already registered")

        user = User(
            email=email,
            hashed_password=hash_password(password),
        )
        return UserRepository.create(db, user)
