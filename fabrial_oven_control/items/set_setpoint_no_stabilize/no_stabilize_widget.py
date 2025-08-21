from pathlib import Path

from fabrial import ItemWidget
from fabrial.custom_widgets import DoubleSpinBox, Widget
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFormLayout

from ...constants import OVEN_PORT_LABEL, SETPOINT_LABEL
from ...quince10gce import MAXIMUM_SETPOINT, MINIMUM_SETPOINT
from ...widgets import PortComboBox

BASE_NAME = "Set Setpoint No Stabilization"
DIRECTORY = Path(__file__).parent
ICON = QIcon(str(DIRECTORY.joinpath("thermometer.png")))
DESCRIPTIONS_DIRECTORY = DIRECTORY.joinpath("descriptions")


class NoStabilizeWidget(ItemWidget):
    """Set the oven's setpoint without waiting for the temperature to stabilize; widget."""

    def __init__(self, port: str, setpoint: float):
        layout = QFormLayout()
        parameter_widget = Widget(layout)
        self.port_combo_box = PortComboBox(port)
        self.setpoint_spinbox = DoubleSpinBox(2, MINIMUM_SETPOINT, MAXIMUM_SETPOINT, setpoint)
        layout.addRow(OVEN_PORT_LABEL, self.port_combo_box)
        layout.addRow(SETPOINT_LABEL, self.setpoint_spinbox)

        ItemWidget.__init__(self, parameter_widget, BASE_NAME, ICON, None)
