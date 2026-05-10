"""Emulation registry for Survival Kids 2 (GBC, 2000 Konami)."""

from typing import Dict, Type

from gameboy_worlds.emulation.parser import StateParser
from gameboy_worlds.emulation.tracker import StateTracker
from gameboy_worlds.emulation.emulator import Emulator

from gameboy_worlds.emulation.survival_kids_2.parsers import SurvivalKids2Parser
from gameboy_worlds.emulation.survival_kids_1.trackers import (
    SurvivalKidsTracker,
    SurvivalKidsVitalsTracker,
)

GAME_TO_GB_NAME: Dict[str, str] = {
    "survival_kids_2": "SurvivalKids2CN.gbc",
}

STRONGEST_PARSERS: Dict[str, Type[StateParser]] = {
    "survival_kids_2": SurvivalKids2Parser,
}

AVAILABLE_STATE_TRACKERS: Dict[str, Dict[str, Type[StateTracker]]] = {
    "survival_kids_2": {
        "default": SurvivalKidsTracker,
        "vitals": SurvivalKidsVitalsTracker,
    },
}

AVAILABLE_EMULATORS: Dict[str, Dict[str, Type[Emulator]]] = {
    "survival_kids_2": {
        "default": Emulator,
    },
}
