from systems import Core, Controller
from cosapp.base import System, Port
from cosapp.drivers import RungeKutta
from cosapp.recorders import DataFrameRecorder
import numpy as np
import matplotlib.pylab as plt

class Assembly(System):
    def setup(self):
        
        self.add_child(Core( name = 'cpu_core' ))
        self.add_child(Controller( name = 'fan_controller' ))

    def compute(self):

        pass
    