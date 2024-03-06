from systems import Core

Vcpu = 2.5 # in Volts, max 5 Volts


core = Core( name = 'cpu_core' )



Core.Vcpu = Vcpu
core.run_once()


print(core.Wcpu)
