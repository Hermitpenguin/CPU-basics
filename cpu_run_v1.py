from systems import Core, Controller
from cosapp.drivers import RungeKutta
from cosapp.recorders import DataFrameRecorder
from cosapp.drivers import Optimizer, NonLinearSolver
import numpy as np
import matplotlib.pylab as plt
from assembly import Assembly

# vcpu = 0.1 # in Volts, max 5 Volts

CPU = Assembly('CPU')

CPU_driver = CPU.add_driver(RungeKutta(order=4))
CPU_driver.time_interval = (0,500)
CPU_driver.dt = 0.05
CPU_driver.add_driver(NonLinearSolver('nonlinearsolve'))

# Initial conditions
T0 = 273. + 30.
CPU.cpu_core.T = T0
CPU.cpu_core.Troom = T0
CPU.heatsink.T = T0
CPU.heatsink.Troom = T0
CPU.heatsink.Tcpu = T0
CPU.fan_controller.Tcpu = T0
CPU.cpu_core.vcpu = 4.
CPU_driver.add_recorder(DataFrameRecorder(includes=['cpu_core.T', 'heatsink.T', 'fan.airspeed','heatsink.cooling_power','cpu_core.cooling_power']),period=1.)
CPU_driver.set_scenario(init = {'cpu_core.T': T0, 'heatsink.T': T0})


# optim = CPU.add_driver(Optimizer('optim', method='SLSQP', tol=1e-12, verbose=1))
# optim.add_child(NonLinearSolver('solver', tol=1e-12))  # to solve cyclic dependencies

# # optim.add_unknown('a', lower_bound=0, upper_bound=1)
# optim.add_unknown('heatsink.area', lower_bound=0.0, upper_bound=1.)
# # optim.set_minimum('heatsink.area**2')
# optim.set_minimum('(1 + fan_controller.tempcheck)*heatsink.area**2')

# optim.add_constraints([
#     'cpu_core.T < 81'])

# optim.add_constraints([
#     'fan_controller.tempcheck >= 0'])


CPU.run_drivers()
# print(optim.solution)

# print(CPU.inwards.items())

data = CPU_driver.recorder.export_data()

print(data)
# print(CPU.heatsink.cooling_power.unit)
time = np.asarray(data['time'])
temp = np.asarray(data['cpu_core.T'])
Vfan = np.asarray(data['fan.airspeed'])
hstemp = np.asarray(data['heatsink.T'])

fig, ax = plt.subplots(1,2)
ax[0].plot(time, temp,'.')
ax[0].plot(time, hstemp,'.')
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

