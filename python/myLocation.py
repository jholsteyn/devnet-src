class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

loc = Location("Johan", "Belgium")
print(loc.name)
print(loc.country)
print(type(loc))