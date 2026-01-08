import uuid
from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped,mapped_column
from datetime import datetime
from backend.app.db.base import Base

class User(Base):
    __tablename__ = "users"

    #gives a unique id to every user
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    email: Mapped[str] = mapped_column(
        String(320),
        unique=True,
        index=True,
        nullable=False,#means this is necessary, this is needed, this is a must
    )

    hashed_password: Mapped[str] = mapped_column(
        String(1024),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,default=True,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )