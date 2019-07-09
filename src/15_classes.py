# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon:
   def __init__(self,lat,lon,**kwargs):
        self.lon = lon
        self.lat = lat
# YOUR CODE HERE
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.



# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self,name,**kwargs):
        super().__init__(**kwargs)
        self.name = name

    def __str__(self):
        return f"Name {self.name}. Lon:{self.lon}. Lat:{self.lat}"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self,difficulty,size,**kwargs):
        super().__init__(**kwargs)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return f"Name {self.name}. Lon:{self.lon}. Lat:{self.lat}"

# YOUR CODE HERE

#   Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
my_waypoint = Waypoint(name="Catacombs", lon=41.70505, lat=-121.51521)

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(my_waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

my_geocache = Geocache(difficulty=1.5, size=2, name="Newberry Views", lon=44.052137, lat=-121.41556)
# YOUR CODE HERE

# Print it--also make this print more nicely
print(my_geocache)
