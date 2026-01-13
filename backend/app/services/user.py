from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user import UserRepository


class UserService:
    @staticmethod
    def create_user(db: Session, email: str, hashed_password: str) -> User:
        existing = UserRepository.get_by_email(db, email)
        if existing:
            raise ValueError("Email already registered")

        user = User(
            email=email,
            hashed_password=hashed_password,
        )
        return UserRepository.create(db, user)
