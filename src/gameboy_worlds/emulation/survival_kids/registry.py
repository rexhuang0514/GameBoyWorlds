"""Emulation registry for Survival Kids games."""

from typing import Dict, Type

from gameboy_worlds.emulation.parser import StateParser
from gameboy_worlds.emulation.tracker import StateTracker
from gameboy_worlds.emulation.emulator import Emulator
from gameboy_worlds.emulation.survival_kids.parsers import (
    SurvivalKids2Parser,
    SurvivalKidsParser,
)
from gameboy_worlds.emulation.survival_kids.trackers import (
    SurvivalKidsAnimalKilledTracker,
    SurvivalKidsBagIconTracker,
    SurvivalKidsCanteenActionMenuTracker,
    SurvivalKidsCanteenChosenTracker,
    SurvivalKidsCanteenDrinkSelectedTracker,
    SurvivalKidsCanteenPickupDialogueTracker,
    SurvivalKidsCanteenTakeLeaveMenuTracker,
    SurvivalKidsCanteenUseSelectedTracker,
    SurvivalKidsChapter1PathClearedTracker,
    SurvivalKidsFeatherTakeLeaveMenuTracker,
    SurvivalKidsGameViewportChangedTracker,
    SurvivalKidsHpChangedTracker,
    SurvivalKidsHudTracker,
    SurvivalKidsHungerChangedTracker,
    SurvivalKidsInventoryOpenTracker,
    SurvivalKidsKnifeChosenTracker,
    SurvivalKidsKnifeEquippedTracker,
    SurvivalKidsMeatActionMenuTracker,
    SurvivalKidsMeatEatenDialogueTracker,
    SurvivalKidsMeatEatSelectedTracker,
    SurvivalKidsPickupItemDialogueTracker,
    SurvivalKidsPathAfterBlockingGrassTracker,
    SurvivalKidsStaminaChangedTracker,
    SurvivalKidsStatusBarChangedTracker,
    SurvivalKidsTakeLeaveMenuTracker,
    SurvivalKidsThirstChangedTracker,
    SurvivalKidsTracker,
    SurvivalKidsVitalsTracker,
)


GAME_TO_GB_NAME: Dict[str, str] = {
    "survival_kids_1": "SurvivalKids.gbc",
    "survival_kids_2": "SurvivalKids2CN.gbc",
}

STRONGEST_PARSERS: Dict[str, Type[StateParser]] = {
    "survival_kids_1": SurvivalKidsParser,
    "survival_kids_2": SurvivalKids2Parser,
}

AVAILABLE_STATE_TRACKERS: Dict[str, Dict[str, Type[StateTracker]]] = {
    "survival_kids_1": {
        "default": SurvivalKidsTracker,
        "hud": SurvivalKidsHudTracker,
        "vitals": SurvivalKidsVitalsTracker,
        "status_bar_changed_test": SurvivalKidsStatusBarChangedTracker,
        "hp_changed_test": SurvivalKidsHpChangedTracker,
        "hunger_changed_test": SurvivalKidsHungerChangedTracker,
        "thirst_changed_test": SurvivalKidsThirstChangedTracker,
        "stamina_changed_test": SurvivalKidsStaminaChangedTracker,
        "game_viewport_changed_test": SurvivalKidsGameViewportChangedTracker,
        "inventory_open_test": SurvivalKidsInventoryOpenTracker,
        "pickup_item_dialogue_test": SurvivalKidsPickupItemDialogueTracker,
        "canteen_pickup_dialogue_test": SurvivalKidsCanteenPickupDialogueTracker,
        "bag_icon_test": SurvivalKidsBagIconTracker,
        "knife_equipped_test": SurvivalKidsKnifeEquippedTracker,
        "knife_chosen_test": SurvivalKidsKnifeChosenTracker,
        "canteen_chosen_test": SurvivalKidsCanteenChosenTracker,
        "take_leave_menu_test": SurvivalKidsTakeLeaveMenuTracker,
        "canteen_take_leave_menu_test": SurvivalKidsCanteenTakeLeaveMenuTracker,
        "canteen_action_menu_test": SurvivalKidsCanteenActionMenuTracker,
        "canteen_drink_selected_test": SurvivalKidsCanteenDrinkSelectedTracker,
        "canteen_use_selected_test": SurvivalKidsCanteenUseSelectedTracker,
        "animal_killed_test": SurvivalKidsAnimalKilledTracker,
        "chapter1_path_cleared_test": SurvivalKidsChapter1PathClearedTracker,
        "path_after_blocking_grass_test": SurvivalKidsPathAfterBlockingGrassTracker,
        "feather_take_leave_menu_test": SurvivalKidsFeatherTakeLeaveMenuTracker,
        "meat_action_menu_test": SurvivalKidsMeatActionMenuTracker,
        "meat_eat_selected_test": SurvivalKidsMeatEatSelectedTracker,
        "meat_eaten_dialogue_test": SurvivalKidsMeatEatenDialogueTracker,
    },
    "survival_kids_2": {
        "default": SurvivalKidsTracker,
        "hud": SurvivalKidsHudTracker,
        "vitals": SurvivalKidsVitalsTracker,
        "status_bar_changed_test": SurvivalKidsStatusBarChangedTracker,
        "hp_changed_test": SurvivalKidsHpChangedTracker,
        "hunger_changed_test": SurvivalKidsHungerChangedTracker,
        "thirst_changed_test": SurvivalKidsThirstChangedTracker,
        "stamina_changed_test": SurvivalKidsStaminaChangedTracker,
        "game_viewport_changed_test": SurvivalKidsGameViewportChangedTracker,
    },
}

AVAILABLE_EMULATORS: Dict[str, Dict[str, Type[Emulator]]] = {
    "survival_kids_1": {
        "default": Emulator,
    },
    "survival_kids_2": {
        "default": Emulator,
    },
}
