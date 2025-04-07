import sys
import skrf
import matplotlib.pyplot as plt
skrf.stylely()

network1 = skrf.Network(sys.argv[1])
network1_dc = network1.extrapolate_to_dc(kind='linear')

network2 = skrf.Network(sys.argv[2])
network2_dc = network2.extrapolate_to_dc(kind='linear')

plt.figure()
plt.title("Time Domain Reflectometry")
network1_dc.s11.plot_z_time_step(window='hamming', label="simulation")
network2_dc.s11.plot_z_time_step(window='hamming', label="experiment")
plt.ylabel("Impedance Magnitude (Ω)")
plt.xlim((-0.5, 1.5))

plt.tight_layout()
plt.show()
