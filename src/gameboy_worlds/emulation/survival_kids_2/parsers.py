"""
Survival Kids 2 (GBC, 2000 Konami) game state parser.
Inherits all logic from Survival Kids 1; only the VARIANT tag differs.
"""

from gameboy_worlds.emulation.survival_kids_1.parsers import SurvivalKidsParser


class SurvivalKids2Parser(SurvivalKidsParser):
    """Game state parser for Survival Kids 2 (GBC)."""

    VARIANT = "survival_kids_2"

    def __repr__(self) -> str:
        return f"<SurvivalKids2Parser(variant={self.VARIANT})>"
