from systems import Core, Controller
from cosapp.drivers import RungeKutta
from cosapp.recorders import DataFrameRecorder
import numpy as np
import matplotlib.pylab as plt

vcpu = 3. # in Volts, max 5 Volts



core = Core( name = 'cpu_core' )
controller = Controller( name = 'fan_controller' )


core.vcpu = vcpu

core_driver = core.add_driver(RungeKutta(order=4))
core_driver.time_interval = (0,300)
core_driver.dt = 0.1

# Initial conditions
T0 = 273.+20.
core_driver.add_recorder(DataFrameRecorder(includes=['T', 'dT']),period=0.1)
core_driver.set_scenario(init = {'T': T0})

core.run_drivers()
data = core_driver.recorder.export_data()

time = np.asarray(data['time'])
temp = np.asarray(data['T'])

fig, ax = plt.subplots()
ax.plot(time, temp,'.')
ax.set_title('CPU temperature')
ax.set_xlabel('time (s)')
ax.set_ylabel('Temperature (K)')

fig.savefig("T.png")