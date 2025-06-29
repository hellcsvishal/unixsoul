import os
import subprocess
from . import errors

class baseMonitor:
    def __init__(self):
        pass

    def _capture_monitors(self):
        "Capture all the monitors available in the system using xrandr"
        command = ["xrandr", "--listmonitors"]
        output = subprocess.run(command, capture_output=True)
        err = output.stderr.decode('utf-8') # Log it
        if err:
            return # TODO: handle the exceptions
        return output.stdout.decode('utf-8')
            
    def __get_monitor_resolution__(self, monitor_id):
        pass

    def __get_monitor_size__(self, monitor_id):
        pass

    def __get_monitor_refresh_rate__(self, monitor_id):
        pass

class hyprlandMontior(baseMonitor):
    def __init__(self):
        self.hyprctlmonitors = self._capture_monitors() 
        # Need a parser to parse the output

    def _capture_monitors(self):
        "Capture all the monitors available in the system using hyprctl"
        command = ["hyprctl", "monitors", "all"]
        output = subprocess.run(command, capture_output=True)
        err = output.stderr.decode('utf-8') # Log it
        if err:
            return super()._capture_monitors()
        return output.stdout.decode('utf-8')
