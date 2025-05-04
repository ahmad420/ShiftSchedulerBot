"""
Shift assignment model representing the assignment of shifts to users.
"""
from typing import Optional

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from .base import Base


class ShiftAssignment(Base):
    """
    Shift assignment model representing the assignment of a shift to a user.
    """
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    shift_id = Column(Integer, ForeignKey("shift.id"), nullable=False)
    status = Column(String, nullable=False, default="assigned")  # assigned, swapped, cancelled

    # Relationships
    user = relationship("User", back_populates="shift_assignments")
    shift = relationship("Shift", back_populates="assignments")

    def __repr__(self) -> str:
        """
        String representation of the shift assignment.
        """
        return f"<ShiftAssignment user_id={self.user_id} shift_id={self.shift_id}>" 