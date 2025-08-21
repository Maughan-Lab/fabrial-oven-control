from pathlib import Path
from typing import Any

from fabrial import SequenceStep, StepRunner

from ... import quince10GCE
from ...constants import TEMPERATURES_FILENAME
from ...utility.sequence import StabilizeTask
from .set_setpoint_widget import BASE_NAME


class SetSetpointStep(SequenceStep):
    """Set the oven's setpoint and stabilize; step."""

    def __init__(
        self,
        port: str,
        setpoint: float,
        measurement_interval_ms: int,
        minimum_measurements: int,
        tolerance: float,
    ):
        self.port = port
        self.setpoint = setpoint
        self.measurement_interval_ms = measurement_interval_ms
        self.minimum_measurements = minimum_measurements
        self.tolerance = tolerance

    async def run(self, runner: StepRunner, data_directory: Path):  # implementation
        oven = await quince10GCE.create_oven(self.port, self, runner)
        await StabilizeTask(
            oven,
            self.measurement_interval_ms,
            self.minimum_measurements,
            self.tolerance,
            self,
            runner,
            data_directory,
            TEMPERATURES_FILENAME,
        ).run(self.setpoint)

    def reset(self):  # implementation
        return  # nothing to do

    def name(self) -> str:
        return BASE_NAME

    def metadata(self) -> dict[str, Any]:
        return {
            "Selected Port": self.port,
            "Selected Setpoint": self.setpoint,
            "Selected Measurement Interval (ms)": self.measurement_interval_ms,
            "Selected Minimum Measurements": self.minimum_measurements,
            "Selected Tolerance": self.tolerance,
        }
