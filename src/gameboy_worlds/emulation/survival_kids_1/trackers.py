"""State trackers for Survival Kids 1."""

from gameboy_worlds.emulation.tracker import StateTracker
from gameboy_worlds.emulation.survival_kids_1.base_metrics import (
    CoreSurvivalKidsMetrics,
    SurvivalKidsExploreMetrics,
    SurvivalKidsVitalMetrics,
)


class SurvivalKidsTracker(StateTracker):
    def start(self):
        super().start()
        self.metric_classes.extend([CoreSurvivalKidsMetrics, SurvivalKidsExploreMetrics])


class SurvivalKidsVitalsTracker(SurvivalKidsTracker):
    def start(self):
        super().start()
        self.metric_classes.extend([SurvivalKidsVitalMetrics])
