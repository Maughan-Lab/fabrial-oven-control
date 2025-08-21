from fabrial import PluginCategory

from .items import SetSetpointItem
from .oven import Oven


# Fabrial entry point
def categories() -> list[PluginCategory]:
    return [PluginCategory("Quince 10 GCE Lab Oven", [SetSetpointItem("", 0, 5000, 150, 1)])]
