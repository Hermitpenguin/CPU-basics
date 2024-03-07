from systems import Core, Controller
from cosapp.base import System, Port
from cosapp.drivers import RungeKutta
from cosapp.recorders import DataFrameRecorder
import numpy as np
import matplotlib.pylab as plt

class Assembly(System):
    def setup(self):
        
        self.add_child(Core( 'cpu_core' ))
        self.add_child(Controller( 'fan_controller' ))

        # self.connect(self.cpu_core,self.fan_controller,{'ext_cooling':'Vfan'})
        # self.connect(self.fan_controller,self.cpu_core,{'Vfan': 'ext_cooling'})
        self.connect(self.cpu_core, self.fan_controller, {'T': 'Tcpu'})
        

    def compute(self):
        self.cpu_core.ext_cooling = self.fan_controller.Vfan
        # print(self.fan_controller.Vfan)
        pass