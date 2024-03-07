from systems import Core, Controller
from cosapp.drivers import RungeKutta
from cosapp.recorders import DataFrameRecorder
import numpy as np
import matplotlib.pylab as plt
from assembly import Assembly

vcpu = 3. # in Volts, max 5 Volts

CPU = Assembly('CPU')

# core = Core( name = 'cpu_core' )
# controller = Controller( name = 'fan_controller' )

# cosapp cpu-fmu, composant en control commande
# modelica

