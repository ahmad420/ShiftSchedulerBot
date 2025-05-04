"""
User model for the Shift Scheduler Bot.
"""
from datetime import datetime
from enum import Enum
from typing import Optional

from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship

from db.base import Base
from utils.translations import Language


class UserRole(Enum):
    """User roles in the system."""
    ADMIN = "admin"
    DEPARTMENT_MANAGER = "dept_manager"
    SHIFT_MANAGER = "shift_manager"
    EMPLOYEE = "employee"


class User(Base):
    """User model representing a team member."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(SQLEnum(UserRole), nullable=False)
    department_id = Column(Integer, nullable=False)
    language = Column(SQLEnum(Language), default=Language.ENGLISH)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    shifts = relationship("ShiftAssignment", back_populates="user")
    preferences = relationship("UserPreference", back_populates="user")
    swap_requests = relationship("SwapRequest", back_populates="user")

    def __repr__(self) -> str:
        """
        String representation of the user.
        """
        return f"<User {self.username or self.telegram_id}>" 