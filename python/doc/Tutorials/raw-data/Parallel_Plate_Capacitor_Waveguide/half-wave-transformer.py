# keep text as text, not path
import matplotlib.pyplot as plt
plt.rcParams['svg.fonttype'] = 'none'

from cmath import phase
from math import degrees
import skrf
from skrf.media import DefinedAEpTandZ0

import schemdraw
import schemdraw.elements as elm 


def calc(wavelength, zport):
    freq = skrf.frequency.Frequency(start=1e9, stop=1e9, unit='Hz', npoints=1)

    media = DefinedAEpTandZ0(freq, z0=50)
    line = media.line(d=360 * wavelength, unit='deg', z0_port=50)
    resistor = media.resistor(600) ** media.short()
    network = line ** resistor
    print(network.s, network.z)
    if zport != 50:
        network.renormalize(zport)

    return [network.s[:,0,0][0], network.z[:,0,0][0]]


def draw(wavelength, zport, output):
    gamma, z = calc(wavelength, zport)
    print(gamma, z)

    with schemdraw.Drawing(file=output) as d:
        source = elm.SourceV().label('$V_G$', loc='top')
        d += source
        
        zg = (elm.Resistor().right()
                           .label(r'$Z_G$', loc='top')
                           .label(r'$%d\Omega$' % zport, loc="bottom")
        )
        d += zg
        

        if abs(gamma) < 1e-10:
            gamma_deg = 0
        else:
            gamma_deg = degrees(phase(gamma))
            if -0.1 < gamma_deg < 0.1:
                gamma_deg = 0

        if abs(z) < 1e-10:
            phase_deg = 0
        else:
            phase_deg = degrees(phase(z))
            if -0.1 < phase_deg < 0.1:
                phase_deg = 0

        label = "$\Gamma= %.1f\\angle%.1f^\circ$\n$Z_{in} = %.1f\\angle%.1f^\circ \Omega$" % (
            abs(gamma), gamma_deg, abs(z), phase_deg
        )
        print(
            "A %d Ω transmitter is connected to a 600 Ω receiver via a "
            "50 Ω transmission line with a length of %.1fλ, its input reflection "
            "coefficient is %.1f∠%.1f°, its input impedance is %.1f∠%.1f° Ω." % (zport, wavelength, abs(gamma), gamma_deg, abs(z), phase_deg)
        )

        d += (elm.Dot().right()
                      .label(label, loc='top', ofst=(0, -2))
        )
        
        d += (elm.Coax().right()
                       .label(r'$50\Omega$', loc='top')
                       .label(r'$%.1f\lambda$' % wavelength, loc='bottom')
        )
        
        
        zl = (elm.Resistor().down()
                           .label(r'$Z_L$', loc='top')
                           .label(r'$600\Omega$', loc="bottom")
        )
        d += zl
        
        
        d += elm.Line().left().tox(source.start)
    

draw(0.2, 50, "half-wave-1.svg")
draw(0.4, 50, "half-wave-2.svg")
draw(0.5, 50, "half-wave-3.svg")
draw(0.2, 600, "half-wave-4.svg")
draw(0.4, 600, "half-wave-5.svg")
draw(0.5, 600, "half-wave-6.svg")
