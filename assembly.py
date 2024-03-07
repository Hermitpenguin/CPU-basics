from systems import Core, Controller, Fan, HeatSink
from cosapp.base import System, Port
from cosapp.drivers import RungeKutta
from cosapp.recorders import DataFrameRecorder
import numpy as np
import matplotlib.pylab as plt

class Assembly(System):
    def setup(self):
        
        self.add_child(Core( 'cpu_core' ))
        self.add_child(Controller( 'fan_controller' ))
        self.add_child(Fan( 'fan' ))
        self.add_child(HeatSink( 'heatsink' ))

        self.connect(self.cpu_core, self.fan_controller, {'T': 'Tcpu'})
        self.connect(self.fan_controller,self.fan, {'Vfan':'Vfan'})
        self.connect(self.fan, self.heatsink, {'airspeed'})
        self.connect(self.cpu_core,self.heatsink,{'T':'Tcpu'})
        self.connect(self.cpu_core, self.heatsink, {'cooling_power'})

    def compute(self):
        self.cpu_core.cooling_power = self.heatsink.cooling_power
