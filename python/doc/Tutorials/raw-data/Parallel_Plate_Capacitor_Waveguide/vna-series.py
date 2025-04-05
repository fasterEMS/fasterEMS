import schemdraw
import schemdraw.elements as elm


with schemdraw.Drawing(file='vna-series.svg'):
    elm.Ground()
    elm.SourceV().length(2).label('V1')
    elm.Resistor().length(2).label('50Ω')
    elm.Line().length(1).right()
    elm.ResistorIEC().right().label('$Z_\mathrm{DUT}$')
    line = elm.Line().length(1).right()
    elm.Resistor().length(4).down().label('50Ω')
    elm.Ground()
    elm.Line().length(2).at(line.end).right()
    elm.MeterV().length(4).down().label('V2')
    elm.Ground()
