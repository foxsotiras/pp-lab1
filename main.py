class NullStr(Exception):
    def __init__(self, data = "string is empty"):
        self.data = data

    def __str__(self):
        return f"{self.data}"


class Aircraft:
    name: str
    max_speed: float
    length: float
    width: float
    height: float
    pilot: bool
    altitude: float

    def __init__(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            pilot: bool, altitude: float):
        if not isinstance(name, str)\
                or not isinstance(max_speed, float)\
                or not isinstance(length, float)\
                or not isinstance(width, float)\
                or not isinstance(height, float)\
                or not isinstance(pilot, bool)\
                or not isinstance(altitude, float):
            raise TypeError("incorrect arguments type")

        if not name:
            raise NullStr("argument \"name\" is empty")

        self.name = name
        self.max_speed = max_speed
        self.length = length
        self.width = width
        self.height = height
        self.pilot = pilot
        self.altitude = altitude


class FighterJet(Aircraft):
    weapons_system: str

    def __init__(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, weapons_system: str):
        if not isinstance(name, str)\
                or not isinstance(max_speed, float)\
                or not isinstance(length, float)\
                or not isinstance(width, float)\
                or not isinstance(height, float)\
                or not isinstance(altitude, float)\
                or not isinstance(weapons_system, str):
            raise TypeError("incorrect arguments type")

        if not name:
            raise NullStr("argument \"name\" is empty")

        super().__init__(name, max_speed, length, width, height, True,
            altitude)
        self.weapons_system = weapons_system


class CommercialAircraft(Aircraft):
    passengers: int

    def __init__(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, passengers: int):
        if not isinstance(name, str)\
                or not isinstance(max_speed, float)\
                or not isinstance(length, float)\
                or not isinstance(width, float)\
                or not isinstance(height, float)\
                or not isinstance(altitude, float)\
                or not isinstance(passengers, int):
            raise TypeError("incorrect arguments type")

        if not name:
            raise NullStr("argument \"name\" is empty")

        super().__init__(name, max_speed, length, width, height, True,
            altitude)
        self.passengers = passengers


class Helicopter(Aircraft):
    rotor_diameter: float

    def __init__(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, rotor_diameter: float):
        if not isinstance(name, str)\
                or not isinstance(max_speed, float)\
                or not isinstance(length, float)\
                or not isinstance(width, float)\
                or not isinstance(height, float)\
                or not isinstance(altitude, float)\
                or not isinstance(rotor_diameter, float):
            raise TypeError("incorrect arguments type")

        if not name:
            raise NullStr("argument \"name\" is empty")

        super().__init__(name, max_speed, length, width, height, True,
            altitude)
        self.rotor_diameter = rotor_diameter


class Autogyro(Aircraft):
    rotor_diameter: float

    def __init__(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, rotor_diameter: float):
        if not isinstance(name, str)\
                or not isinstance(max_speed, float)\
                or not isinstance(length, float)\
                or not isinstance(width, float)\
                or not isinstance(height, float)\
                or not isinstance(altitude, float)\
                or not isinstance(rotor_diameter, float):
            raise TypeError("incorrect arguments type")

        if not name:
            raise NullStr("argument \"name\" is empty")

        super().__init__(name, max_speed, length, width, height, True,
            altitude)
        self.rotor_diameter = rotor_diameter


class Drone(Aircraft):
    control_range: float

    def __init__(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, control_range: float):
        if not isinstance(name, str)\
                or not isinstance(max_speed, float)\
                or not isinstance(length, float)\
                or not isinstance(width, float)\
                or not isinstance(height, float)\
                or not isinstance(altitude, float)\
                or not isinstance(control_range, float):
            raise TypeError("incorrect arguments type")

        if not name:
            raise NullStr("argument \"name\" is empty")

        super().__init__(name, max_speed, length, width, height, True,
            altitude)
        self.control_range = control_range


class Zeppelin(Aircraft):
    gas_capacity: float

    def __init__(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, gas_capacity: float):
        if not isinstance(name, str)\
                or not isinstance(max_speed, float)\
                or not isinstance(length, float)\
                or not isinstance(width, float)\
                or not isinstance(height, float)\
                or not isinstance(altitude, float)\
                or not isinstance(gas_capacity, float):
            raise TypeError("incorrect arguments type")

        if not name:
            raise NullStr("argument \"name\" is empty")

        super().__init__(name, max_speed, length, width, height, True,
            altitude)
        self.gas_capacity = gas_capacity


class Balloon(Aircraft):
    gas_capacity: float

    def __init__(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, gas_capacity: float):
        if not isinstance(name, str)\
                or not isinstance(max_speed, float)\
                or not isinstance(length, float)\
                or not isinstance(width, float)\
                or not isinstance(height, float)\
                or not isinstance(altitude, float)\
                or not isinstance(gas_capacity, float):
            raise TypeError("incorrect arguments type")

        if not name:
            raise NullStr("argument \"name\" is empty")

        super().__init__(name, max_speed, length, width, height, True,
            altitude)
        self.gas_capacity = gas_capacity


class Spacecraft:
    name: str
    max_thrust: float
    height: float
    diameter: float

    def __init__(self, name: str, max_thrust: float, height: float,
            diameter: float):
        if not isinstance(name, str)\
                or not isinstance(max_thrust, float)\
                or not isinstance(height, float)\
                or not isinstance(diameter, float):
            raise TypeError("incorrect arguments type")

        if not name:
            raise NullStr("argument \"name\" is empty")

        self.name = name
        self.max_thrust = max_thrust
        self.height = height
        self.diameter = diameter


class CargoSpacecraft(Spacecraft):
    cargo_weight: float

    def __init__(self, name: str, max_thrust: float, height: float,
            diameter: float, cargo_weight: float):
        if not isinstance(name, str)\
                or not isinstance(max_thrust, float)\
                or not isinstance(height, float)\
                or not isinstance(diameter, float)\
                or not isinstance(cargo_weight, float):
            raise TypeError("incorrect arguments type")

        if not name:
            raise NullStr("argument \"name\" is empty")

        super().__init__(name, max_thrust, height, diameter)
        self.cargo_weight = cargo_weight


class CommercialSpacecraft(Spacecraft):
    passengers: int

    def __init__(self, name: str, max_thrust: float, height: float,
            diameter: float, passengers: int):
        if not isinstance(name, str)\
                or not isinstance(max_thrust, float)\
                or not isinstance(height, float)\
                or not isinstance(diameter, float)\
                or not isinstance(passengers, int):
            raise TypeError("incorrect arguments type")

        if not name:
            raise NullStr("argument \"name\" is empty")

        super().__init__(name, max_thrust, height, diameter)
        self.passengers = passengers
