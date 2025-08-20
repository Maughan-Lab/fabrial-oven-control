from fabrial.custom_widgets import ComboBox, DoubleSpinBox, SpinBox, Widget
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QShowEvent
from PyQt6.QtWidgets import QComboBox, QFormLayout, QWidget

from .utility import ports

# class ComboBox(QComboBox):
#     """`QComboBox` that doesn't show all entries at once."""

#     # signal to detect when the combobox is pressed
#     pressed = pyqtSignal()

#     def __init__(self, items: Iterable[str]):
#         QComboBox.__init__(self)
#         self.setStyleSheet("combobox-popup: 0")
#         self.setMaxVisibleItems(20)

#     def setCurrentIndexSilent(self, index: int):
#         """Update the current index without emitting signals."""
#         self.blockSignals(True)
#         self.setCurrentIndex(index)
#         self.blockSignals(False)

#     def setCurrentTextSilent(self, text: str | None):
#         """Update the current text without emitting signals."""
#         self.blockSignals(True)
#         self.setCurrentText(text)
#         self.blockSignals(False)

#     def clearSilent(self):
#         """Clear the combobox entries without emitting signals."""
#         self.blockSignals(True)
#         self.clear()
#         self.blockSignals(False)

#     def addItemsSilent(self, items: Iterable[str | None]):
#         """Add items to the combobox without emitting signals."""
#         self.blockSignals(True)
#         self.addItems(items)
#         self.blockSignals(False)

#     # ----------------------------------------------------------------------------------------------
#     # overridden methods
#     def showPopup(self):
#         self.pressed.emit()
#         QComboBox.showPopup(self)


OVEN_PORT_LABEL = "Oven Port"
INTERVAL_LABEL = "Measurement Interval"
MINIMUM_MEASUREMENTS_LABEL = "Minimum Measurements for Stability"
TOLERANCE_LABEL = "Stability Tolerance"


class OvenStabilizationWidget(Widget):
    """Contains entries for running a temperature stabilization step."""

    def __init__(
        self,
        temperature_label: str,
        minimum_temperature: float,
        maximum_temperature: float,
        decimal_precision: int,
    ):
        layout = QFormLayout()
        Widget.__init__(self, layout)

        self.port_combo_box = QComboBox()
        self.temperature_spinbox = DoubleSpinBox(
            decimal_precision, minimum_temperature, maximum_temperature
        )
        self.interval_spinbox = SpinBox(10)
        self.minimum_measurements_spinbox = SpinBox(2)
        self.tolerance_spinbox = DoubleSpinBox(2)

        for label, widget in (
            (OVEN_PORT_LABEL, self.port_combo_box),
            (temperature_label, self.temperature_spinbox),
            (INTERVAL_LABEL, self.interval_spinbox),
            (MINIMUM_MEASUREMENTS_LABEL, self.minimum_measurements_spinbox),
            (TOLERANCE_LABEL, self.tolerance_spinbox),
        ):
            layout.addRow(label, widget)

    def showEvent(self, event: QShowEvent | None):  # overridden
        # refresh the list of ports every time this widget is shown
        self.port_combo_box.clear()
        self.port_combo_box.addItems(ports.list_ports())
        Widget.showEvent(self, event)
