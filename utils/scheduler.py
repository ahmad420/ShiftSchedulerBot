"""
Shift scheduling logic for the IT team.
"""
from datetime import datetime, time, timedelta
from typing import List, Dict, Optional
from enum import Enum


class ShiftType(Enum):
    """Types of shifts available."""
    MORNING_CALLS = "Morning - Calls"
    MORNING_TICKETS = "Morning - Tickets"
    EVENING = "Evening"
    NIGHT = "Night"
    FRIDAY = "Friday"
    WEEKEND = "Weekend"


class ShiftRequirements:
    """Requirements for each shift type."""
    def __init__(self, min_staff: int, max_staff: Optional[int] = None):
        self.min_staff = min_staff
        self.max_staff = max_staff


# Shift requirements for each type
SHIFT_REQUIREMENTS = {
    ShiftType.MORNING_CALLS: ShiftRequirements(min_staff=4),
    ShiftType.MORNING_TICKETS: ShiftRequirements(min_staff=4),
    ShiftType.EVENING: ShiftRequirements(min_staff=2, max_staff=3),
    ShiftType.NIGHT: ShiftRequirements(min_staff=1),
    ShiftType.FRIDAY: ShiftRequirements(min_staff=4),
    ShiftType.WEEKEND: ShiftRequirements(min_staff=1)
}


class Shift:
    """Represents a work shift."""
    def __init__(
        self,
        date: datetime,
        shift_type: ShiftType,
        start_time: time,
        end_time: time,
        description: str
    ):
        self.date = date
        self.shift_type = shift_type
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        self.assigned_staff: List[str] = []


def get_shift_schedule(start_date: datetime, end_date: datetime) -> List[Shift]:
    """
    Generate shift schedule for the given date range.
    """
    schedule: List[Shift] = []
    current_date = start_date

    while current_date <= end_date:
        # Check if it's a weekend (Friday or Saturday)
        if current_date.weekday() in [4, 5]:  # 4 is Friday, 5 is Saturday
            if current_date.weekday() == 4:  # Friday
                # Friday shift
                schedule.append(Shift(
                    date=current_date,
                    shift_type=ShiftType.FRIDAY,
                    start_time=time(8, 0),
                    end_time=time(14, 0),
                    description="Friday Shift (08:00 - 14:00)"
                ))
                # Extended Friday shift
                schedule.append(Shift(
                    date=current_date,
                    shift_type=ShiftType.FRIDAY,
                    start_time=time(14, 0),
                    end_time=time(17, 0),
                    description="Extended Friday Shift (14:00 - 17:00)"
                ))
                # Weekend shift starts
                schedule.append(Shift(
                    date=current_date,
                    shift_type=ShiftType.WEEKEND,
                    start_time=time(17, 0),
                    end_time=time(23, 59),
                    description="Weekend Shift (17:00 - 08:00)"
                ))
            else:  # Saturday
                # Weekend shift continues
                schedule.append(Shift(
                    date=current_date,
                    shift_type=ShiftType.WEEKEND,
                    start_time=time(0, 0),
                    end_time=time(18, 30),
                    description="Weekend Shift (00:00 - 18:30)"
                ))
                # Additional Saturday evening shift
                schedule.append(Shift(
                    date=current_date,
                    shift_type=ShiftType.WEEKEND,
                    start_time=time(18, 30),
                    end_time=time(22, 30),
                    description="Saturday Evening Shift (18:30 - 22:30)"
                ))
                # Weekend shift continues
                schedule.append(Shift(
                    date=current_date,
                    shift_type=ShiftType.WEEKEND,
                    start_time=time(22, 30),
                    end_time=time(23, 59),
                    description="Weekend Shift (22:30 - 08:00)"
                ))
        else:  # Sunday to Thursday
            # Morning shifts
            schedule.append(Shift(
                date=current_date,
                shift_type=ShiftType.MORNING_CALLS,
                start_time=time(8, 0),
                end_time=time(17, 0),
                description="Morning Shift - Calls Team (08:00 - 17:00)"
            ))
            schedule.append(Shift(
                date=current_date,
                shift_type=ShiftType.MORNING_TICKETS,
                start_time=time(8, 0),
                end_time=time(17, 0),
                description="Morning Shift - Tickets Team (08:00 - 17:00)"
            ))
            # Evening shift
            schedule.append(Shift(
                date=current_date,
                shift_type=ShiftType.EVENING,
                start_time=time(13, 0),
                end_time=time(22, 0),
                description="Evening Shift (13:00 - 22:00)"
            ))
            # Night shift
            schedule.append(Shift(
                date=current_date,
                shift_type=ShiftType.NIGHT,
                start_time=time(22, 0),
                end_time=time(8, 0),
                description="Night Shift (22:00 - 08:00)"
            ))

        current_date += timedelta(days=1)

    return schedule


def validate_shift_assignment(shift: Shift, staff_count: int) -> bool:
    """
    Validate if the number of assigned staff meets the shift requirements.
    """
    requirements = SHIFT_REQUIREMENTS[shift.shift_type]
    if staff_count < requirements.min_staff:
        return False
    if requirements.max_staff and staff_count > requirements.max_staff:
        return False
    return True


def get_shift_description(shift_type: ShiftType) -> str:
    """
    Get a detailed description of the shift type.
    """
    descriptions = {
        ShiftType.MORNING_CALLS: "Morning Shift - Calls Team (4 staff)",
        ShiftType.MORNING_TICKETS: "Morning Shift - Tickets Team (4 staff)",
        ShiftType.EVENING: "Evening Shift - Calls Team (2-3 staff)",
        ShiftType.NIGHT: "Night Shift - Emergency Support (1 staff)",
        ShiftType.FRIDAY: "Friday Shift - Calls Team (4 staff)",
        ShiftType.WEEKEND: "Weekend Shift - Emergency Support (1 staff)"
    }
    return descriptions.get(shift_type, "Unknown shift type") 