# keep text as text, not path
import matplotlib.pyplot as plt
plt.rcParams['svg.fonttype'] = 'none'

from cmath import phase
from math import degrees
import skrf
from skrf.media import DefinedAEpTandZ0

import schemdraw
import schemdraw.elements as elm 


def calc(wavelength):
    freq = skrf.frequency.Frequency(start=1e9, stop=1e9, unit='Hz', npoints=1)

    media600 = DefinedAEpTandZ0(freq, z0=600)
    line600 = media600.line(d=360 * wavelength, unit='deg', z0_port=50)
    resistor50 = media600.resistor(50) ** media600.short()
    network = line600 ** resistor50
    network.renormalize(50)

    return [network.s[:,0,0][0], network.z[:,0,0][0]]


def draw(wavelength, output):
    gamma, z = calc(wavelength)
    print(gamma, z)

    with schemdraw.Drawing(file=output) as d:
        source = elm.SourceV().label('$V_G$', loc='top')
        d += source
        
        zg = (elm.Resistor().right()
                           .label(r'$Z_G$', loc='top')
                           .label(r'$50\Omega$', loc="bottom")
        )
        d += zg
        

        if abs(gamma) < 1e-10:
            gamma_deg = 0
        else:
            gamma_deg = degrees(phase(gamma))

        label = "$\Gamma= %.1f\\angle%.1f^\circ$\n$Z_{in} = %.1f\\angle%.1f^\circ \Omega$" % (
            abs(gamma), gamma_deg, abs(z), degrees(phase(z))
        )
        print(
            "A 50 Ω transmitter is connected to a 50 Ω receiver via a "
            "600 Ω transmission line with a length of %.1fλ, its input reflection "
            "coefficient is %.1f∠%.1f°, its input impedance is %.1f∠%.1f° Ω." % (wavelength, abs(gamma), gamma_deg, abs(z), degrees(phase(z)))
        )

        d += (elm.Dot().right()
                      .label(label, loc='top', ofst=(0, -2))
        )
        
        d += (elm.Coax().right()
                       .label(r'$600\Omega$', loc='top')
                       .label(r'$%.1f\lambda$' % wavelength, loc='bottom')
        )
        
        
        zl = (elm.Resistor().down()
                           .label(r'$Z_L$', loc='top')
                           .label(r'$50\Omega$', loc="bottom")
        )
        d += zl
        
        
        d += elm.Line().left().tox(source.start)
    

draw(0.2, "half-wave-1.svg")
draw(0.4, "half-wave-2.svg")
draw(0.5, "half-wave-3.svg")
