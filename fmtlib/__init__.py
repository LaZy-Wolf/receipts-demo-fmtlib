"""Tiny formatting helpers."""

_UNITS = ["B", "KB", "MB", "GB", "TB"]
_SUFFIX = {1: "st", 2: "nd", 3: "rd"}


def human_bytes(n: int) -> str:
    """Format a byte count: 1536 -> '1.5 KB'."""
    size = float(n)
    for unit in _UNITS:
        if abs(size) < 1024 or unit == _UNITS[-1]:
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024


def percent(fraction: float, digits: int = 0) -> str:
    """Format a fraction as a percentage: 0.125 -> '12%'."""
    return f"{fraction * 100:.{digits}f}%"


def ordinal(n: int) -> str:
    """1 -> '1st', 2 -> '2nd', 11 -> '11th', 23 -> '23rd'."""
    suffix = "th" if 10 <= n % 100 <= 20 else _SUFFIX.get(n % 10, "th")
    return f"{n}{suffix}"


def format_number(n, sep: str = ",") -> str:
    """Group thousands: 1234567 -> '1,234,567'."""
    return f"{n:,}".replace(",", sep)
