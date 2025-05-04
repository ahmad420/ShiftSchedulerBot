"""
Swap request model representing requests to swap shifts between users.
"""
from enum import Enum
from typing import Optional

from sqlalchemy import Column, Enum as SQLEnum, ForeignKey, String
from sqlalchemy.orm import relationship

from .base import Base


class SwapRequestStatus(str, Enum):
    """
    Enum for swap request statuses.
    """
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    CANCELLED = "cancelled"


class SwapRequest(Base):
    """
    Swap request model representing a request to swap shifts between users.
    """
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    shift_id = Column(Integer, ForeignKey("shift.id"), nullable=False)
    requested_shift_id = Column(Integer, ForeignKey("shift.id"), nullable=False)
    status = Column(SQLEnum(SwapRequestStatus), nullable=False, default=SwapRequestStatus.PENDING)
    approved_by = Column(Integer, ForeignKey("user.id"), nullable=True)
    reason = Column(String, nullable=True)

    # Relationships
    user = relationship("User", back_populates="swap_requests", foreign_keys=[user_id])
    shift = relationship("Shift", back_populates="swap_requests", foreign_keys=[shift_id])
    requested_shift = relationship("Shift", foreign_keys=[requested_shift_id])
    approver = relationship("User", foreign_keys=[approved_by])

    def __repr__(self) -> str:
        """
        String representation of the swap request.
        """
        return f"<SwapRequest user_id={self.user_id} shift_id={self.shift_id}>" 