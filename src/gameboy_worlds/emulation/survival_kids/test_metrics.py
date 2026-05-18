"""Test metrics for Survival Kids benchmark tasks."""

from gameboy_worlds.emulation.survival_kids.parsers import SurvivalKidsParser
from gameboy_worlds.emulation.tracker import (
    RegionChangedTerminationMetric,
    RegionMatchTerminationMetric,
    TerminationMetric,
)


class StatusBarChangedTerminateMetric(RegionChangedTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _CHANGED_NAMED_REGION = "status_bar"
    _CHANGE_MAE_THRESHOLD = 10


class HpChangedTerminateMetric(RegionChangedTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _CHANGED_NAMED_REGION = "hp_area"
    _CHANGE_MAE_THRESHOLD = 10


class HungerChangedTerminateMetric(RegionChangedTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _CHANGED_NAMED_REGION = "hunger_area"
    _CHANGE_MAE_THRESHOLD = 10


class ThirstChangedTerminateMetric(RegionChangedTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _CHANGED_NAMED_REGION = "thirst_area"
    _CHANGE_MAE_THRESHOLD = 10


class StaminaChangedTerminateMetric(RegionChangedTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _CHANGED_NAMED_REGION = "stamina_area"
    _CHANGE_MAE_THRESHOLD = 10


class GameViewportChangedTerminateMetric(
    RegionChangedTerminationMetric, TerminationMetric
):
    REQUIRED_PARSER = SurvivalKidsParser
    _CHANGED_NAMED_REGION = "game_viewport"
    _CHANGE_MAE_THRESHOLD = 10


class AnimalKilledTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "game_viewport"
    _TERMINATION_TARGET_NAME = "animal_killed"


class Chapter1PathClearedTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "game_viewport"
    _TERMINATION_TARGET_NAME = "chapter1_path_cleared"


class PathAfterBlockingGrassTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "game_viewport"
    _TERMINATION_TARGET_NAME = "path_after_blocking_grass"


class InventoryOpenTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "menu_area"
    _TERMINATION_TARGET_NAME = "inventory_open"


class PickupItemDialogueTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "dialogue_area"
    _TERMINATION_TARGET_NAME = "pickup_item_dialogue"


class CanteenPickupDialogueTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "dialogue_area"
    _TERMINATION_TARGET_NAME = "canteen_pickup_dialogue"


class BagIconTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "bag_icon_area"
    _TERMINATION_TARGET_NAME = "bag_icon"


class KnifeEquippedTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "equipped_items_area"
    _TERMINATION_TARGET_NAME = "knife_equipped"


class KnifeChosenTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "choose_item_area"
    _TERMINATION_TARGET_NAME = "knife_chosen"


class CanteenEquippedTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "equipped_items_area"
    _TERMINATION_TARGET_NAME = "canteen_equipped"


class CanteenChosenTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "choose_item_area"
    _TERMINATION_TARGET_NAME = "canteen_chosen"


class TakeLeaveMenuTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "item_action_menu_two_options"
    _TERMINATION_TARGET_NAME = "take_leave_menu"


class CanteenTakeLeaveMenuTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "item_action_menu_two_options"
    _TERMINATION_TARGET_NAME = "canteen_take_leave_menu"


class CanteenActionMenuTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "item_use_menu_area"
    _TERMINATION_TARGET_NAME = "canteen_action_menu"


class CanteenUseSelectedTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "item_use_menu_area"
    _TERMINATION_TARGET_NAME = "canteen_use_selected"


class CanteenDrinkSelectedTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "item_use_menu_area"
    _TERMINATION_TARGET_NAME = "canteen_drink_selected"


class FeatherTakeLeaveMenuTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "item_action_menu_two_options"
    _TERMINATION_TARGET_NAME = "feather_take_leave_menu"


# Condensed tasks not yet in benchmark/tests/survival_kids.csv:
# - Pick up the feather: needs a stable feather_pickup_dialogue or inventory signal.
# - Eat the meat: needs meat_eat_selected and meat_eaten_dialogue captures.
# - Drink from the canteen: needs final drink success/HUD signal, not just menu selection.
# - Clear blocking grass and move forward: needs a tighter grass/path metric or subgoals.
class MeatActionMenuTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "item_action_menu"
    _TERMINATION_TARGET_NAME = "meat_take_eat_leave_menu"


class MeatEatSelectedTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "item_action_menu"
    _TERMINATION_TARGET_NAME = "meat_eat_selected"


class MeatEatenDialogueTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = SurvivalKidsParser
    _TERMINATION_NAMED_REGION = "dialogue_area"
    _TERMINATION_TARGET_NAME = "meat_eaten_dialogue"
