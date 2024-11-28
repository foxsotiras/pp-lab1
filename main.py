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
        super().__init__(name, max_speed, length, width, height, True,
            altitude)
        self.weapons_system = weapons_system


class CommercialAircraft(Aircraft):
    passengers: int

    def __init__(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, passengers: int):
        super().__init__(name, max_speed, length, width, height, True,
            altitude)
        self.passengers = passengers


class Helicopter(Aircraft):
    rotor_diameter: float

    def __init__(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, rotor_diameter: float):
        super().__init__(name, max_speed, length, width, height, True,
            altitude)
        self.rotor_diameter = rotor_diameter


class Autogyro(Aircraft):
    rotor_diameter: float

    def __init__(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, rotor_diameter: float):
        super().__init__(name, max_speed, length, width, height, True,
            altitude)
        self.rotor_diameter = rotor_diameter


class Drone(Aircraft):
    control_range: float

    def __init__(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, control_range: float):
        super().__init__(name, max_speed, length, width, height, True,
            altitude)
        self.control_range = control_range


class Zeppelin(Aircraft):
    gas_capacity: float

    def __init__(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, gas_capacity: float):
        super().__init__(name, max_speed, length, width, height, True,
            altitude)
        self.gas_capacity = gas_capacity


class Balloon(Aircraft):
    gas_capacity: float

    def __init__(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, gas_capacity: float):
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
        self.name = name
        self.max_thrust = max_thrust
        self.height = height
        self.diameter = diameter


class CargoSpacecraft(Spacecraft):
    cargo_weight: float

    def __init__(self, name: str, max_thrust: float, height: float,
            diameter: float, cargo_weight: float):
        super().__init__(name, max_thrust, height, diameter)
        self.cargo_weight = cargo_weight


class CommercialSpacecraft(Spacecraft):
    passengers: int

    def __init__(self, name: str, max_thrust: float, height: float,
            diameter: float, passengers: int):
        super().__init__(name, max_thrust, height, diameter)
        self.passengers = passengers
