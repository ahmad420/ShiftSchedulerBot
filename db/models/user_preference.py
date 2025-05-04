"""
User preference model representing user preferences for shift assignments.
"""
from typing import Optional

from sqlalchemy import Column, ForeignKey, JSON, String
from sqlalchemy.orm import relationship

from .base import Base


class UserPreference(Base):
    """
    User preference model representing user preferences for shift assignments.
    """
    user_id = Column(Integer, ForeignKey("user.id"), unique=True, nullable=False)
    preferred_shifts = Column(JSON, nullable=True)  # List of preferred shift types
    unavailable_days = Column(JSON, nullable=True)  # List of days when user is unavailable
    max_shifts_per_week = Column(Integer, nullable=True)
    min_rest_days = Column(Integer, nullable=True)
    notes = Column(String, nullable=True)

    # Relationships
    user = relationship("User", back_populates="preferences")

    def __repr__(self) -> str:
        """
        String representation of the user preference.
        """
        return f"<UserPreference user_id={self.user_id}>" 