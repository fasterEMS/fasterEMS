# keep text as text, not path
import matplotlib.pyplot as plt
plt.rcParams['svg.fonttype'] = 'none'


import schemdraw
import schemdraw.elements as elm


with schemdraw.Drawing(file='vna-shunt-thru.svg'):
    elm.Ground()
    elm.SourceV().length(2).label('V1')
    elm.Resistor().length(2).label('50Ω')
    line = elm.Line().length(2).right()
    elm.ResistorIEC().length(4).at(line.end).down().label('$Z_\mathrm{DUT}$')
    elm.Ground()
    line = elm.Line().length(2).at(line.end).right()
    elm.Resistor().length(4).down().label('50Ω')
    elm.Ground()
    elm.Line().length(2).at(line.end).right()
    elm.MeterV().length(4).down().label('V2')
    elm.Ground()
