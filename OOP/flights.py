from typing import List


class Segment:
    def __init__(self,departure,destination):
        self.departure = departure
        self.destination = destination


class Flight:
    def __init__(self,segments:List[Segment]):
        self.segments = segments

    def __repr__(self) -> str:
        """
        :return string in the format of segment --> segment --> segment
        """
        stops = [self.segments[0].departure,self.segments[0].destination]
        for segment in self.segments[1:]:
            stops.append(segment.destination)

        return ' --> '.join(stops)

    @property
    def departure_point(self)->str:
        return self.segments[0].departure
    
    @departure_point.setter
    def departure_point(self,val):
        #self.segments[0].departure=val
        dest = self.segments[0].destination
        self.segments[0] = Segment(departure=val,destination=dest)


flight = Flight([Segment('GDA','BRL')])
print(flight)

flight.departure_point = 'WAW'
print(flight.departure_point)

print(flight)