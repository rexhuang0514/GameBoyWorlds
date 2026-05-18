"""State trackers for Survival Kids."""

from gameboy_worlds.emulation.tracker import StateTracker
from gameboy_worlds.emulation.tracker import DummySubGoalMetric, TestTrackerMixin
from gameboy_worlds.emulation.survival_kids.base_metrics import (
    CoreSurvivalKidsMetrics,
    SurvivalKidsExploreMetrics,
    SurvivalKidsHudMetrics,
    SurvivalKidsVitalMetrics,
)
from gameboy_worlds.emulation.survival_kids.test_metrics import (
    BagIconTerminateMetric,
    AnimalKilledTerminateMetric,
    CanteenActionMenuTerminateMetric,
    CanteenChosenTerminateMetric,
    CanteenDrinkSelectedTerminateMetric,
    CanteenPickupDialogueTerminateMetric,
    CanteenTakeLeaveMenuTerminateMetric,
    CanteenUseSelectedTerminateMetric,
    Chapter1PathClearedTerminateMetric,
    FeatherTakeLeaveMenuTerminateMetric,
    GameViewportChangedTerminateMetric,
    HpChangedTerminateMetric,
    HungerChangedTerminateMetric,
    InventoryOpenTerminateMetric,
    KnifeChosenTerminateMetric,
    KnifeEquippedTerminateMetric,
    MeatActionMenuTerminateMetric,
    MeatEatenDialogueTerminateMetric,
    MeatEatSelectedTerminateMetric,
    PickupItemDialogueTerminateMetric,
    PathAfterBlockingGrassTerminateMetric,
    StaminaChangedTerminateMetric,
    StatusBarChangedTerminateMetric,
    TakeLeaveMenuTerminateMetric,
    ThirstChangedTerminateMetric,
)


class SurvivalKidsTracker(StateTracker):
    def start(self):
        super().start()
        self.metric_classes.extend([CoreSurvivalKidsMetrics, SurvivalKidsExploreMetrics])


class SurvivalKidsVitalsTracker(SurvivalKidsTracker):
    def start(self):
        super().start()
        self.metric_classes.extend([SurvivalKidsVitalMetrics])


class SurvivalKidsHudTracker(SurvivalKidsTracker):
    def start(self):
        super().start()
        self.metric_classes.extend([SurvivalKidsHudMetrics])


class SurvivalKidsTestTracker(TestTrackerMixin, SurvivalKidsHudTracker):
    TERMINATION_TRUNCATION_METRIC = StatusBarChangedTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class SurvivalKidsStatusBarChangedTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = StatusBarChangedTerminateMetric


class SurvivalKidsHpChangedTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = HpChangedTerminateMetric


class SurvivalKidsHungerChangedTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = HungerChangedTerminateMetric


class SurvivalKidsThirstChangedTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = ThirstChangedTerminateMetric


class SurvivalKidsStaminaChangedTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = StaminaChangedTerminateMetric


class SurvivalKidsGameViewportChangedTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = GameViewportChangedTerminateMetric


class SurvivalKidsInventoryOpenTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = InventoryOpenTerminateMetric


class SurvivalKidsPickupItemDialogueTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = PickupItemDialogueTerminateMetric


class SurvivalKidsCanteenPickupDialogueTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = CanteenPickupDialogueTerminateMetric


class SurvivalKidsBagIconTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = BagIconTerminateMetric


class SurvivalKidsKnifeEquippedTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = KnifeEquippedTerminateMetric


class SurvivalKidsKnifeChosenTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = KnifeChosenTerminateMetric


class SurvivalKidsCanteenChosenTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = CanteenChosenTerminateMetric


class SurvivalKidsTakeLeaveMenuTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = TakeLeaveMenuTerminateMetric


class SurvivalKidsCanteenTakeLeaveMenuTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = CanteenTakeLeaveMenuTerminateMetric


class SurvivalKidsCanteenActionMenuTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = CanteenActionMenuTerminateMetric


class SurvivalKidsCanteenUseSelectedTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = CanteenUseSelectedTerminateMetric


class SurvivalKidsCanteenDrinkSelectedTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = CanteenDrinkSelectedTerminateMetric


class SurvivalKidsAnimalKilledTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = AnimalKilledTerminateMetric


class SurvivalKidsChapter1PathClearedTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = Chapter1PathClearedTerminateMetric


class SurvivalKidsPathAfterBlockingGrassTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = PathAfterBlockingGrassTerminateMetric


class SurvivalKidsFeatherTakeLeaveMenuTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = FeatherTakeLeaveMenuTerminateMetric


class SurvivalKidsMeatActionMenuTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = MeatActionMenuTerminateMetric


class SurvivalKidsMeatEatSelectedTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = MeatEatSelectedTerminateMetric


class SurvivalKidsMeatEatenDialogueTracker(SurvivalKidsTestTracker):
    TERMINATION_TRUNCATION_METRIC = MeatEatenDialogueTerminateMetric
