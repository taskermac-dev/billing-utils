"""Misc billing helpers."""


def to_cents(amount: float) -> int:
    return int(round(amount * 100))


def apply_tax(amount: float, rate: float) -> float:
    return round(amount * (1 + rate), 2)
