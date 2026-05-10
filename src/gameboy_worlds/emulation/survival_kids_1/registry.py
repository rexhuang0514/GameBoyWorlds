"""Emulation registry for Survival Kids 1 (GBC, 1999 Konami)."""

from typing import Dict, Type

from gameboy_worlds.emulation.parser import StateParser
from gameboy_worlds.emulation.tracker import StateTracker
from gameboy_worlds.emulation.emulator import Emulator

from gameboy_worlds.emulation.survival_kids_1.parsers import SurvivalKidsParser
from gameboy_worlds.emulation.survival_kids_1.trackers import (
    SurvivalKidsTracker,
    SurvivalKidsVitalsTracker,
)

GAME_TO_GB_NAME: Dict[str, str] = {
    "survival_kids_1": "SurvivalKids.gbc",
}

STRONGEST_PARSERS: Dict[str, Type[StateParser]] = {
    "survival_kids_1": SurvivalKidsParser,
}

AVAILABLE_STATE_TRACKERS: Dict[str, Dict[str, Type[StateTracker]]] = {
    "survival_kids_1": {
        "default": SurvivalKidsTracker,
        "vitals": SurvivalKidsVitalsTracker,
    },
}

AVAILABLE_EMULATORS: Dict[str, Dict[str, Type[Emulator]]] = {
    "survival_kids_1": {
        "default": Emulator,
    },
}
