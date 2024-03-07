from systems import Core, Controller
from cosapp.drivers import RungeKutta
from cosapp.recorders import DataFrameRecorder
import numpy as np
import matplotlib.pylab as plt
from assembly import Assembly

# vcpu = 0.1 # in Volts, max 5 Volts

CPU = Assembly('CPU')

CPU_driver = CPU.add_driver(RungeKutta(order=4))
CPU_driver.time_interval = (0,1000)
CPU_driver.dt = 0.1

# Initial conditions
T0 = 273. + 20.
CPU.cpu_core.vcpu = .2
CPU_driver.add_recorder(DataFrameRecorder(includes=['cpu_core.T', 'cpu_core.dT', 'fan_controller.Vfan','cpu_core.ext_cooling']),period=1)
CPU_driver.set_scenario(init = {'cpu_core.T': T0})
CPU.run_drivers()

data = CPU_driver.recorder.export_data()

print(data)

time = np.asarray(data['time'])
temp = np.asarray(data['cpu_core.T'])
Vfan = np.asarray(data['fan_controller.Vfan'])

fig, ax = plt.subplots(1,2)
ax[0].plot(time, temp,'.')
ax[0].set_title('CPU temperature')
ax[0].set_xlabel('time (s)')
ax[0].set_ylabel('Temperature (K)')

ax[1].plot(time, Vfan,'.')
ax[1].set_title('Fan voltage with CPU temperature')
ax[1].set_xlabel('time (s)')
ax[1].set_ylabel('Fan Voltage (V))')

fig.savefig("T.png")

# cosapp cpu-fmu, composant en control commande
# modelica

