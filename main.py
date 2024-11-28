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


class AircraftManager:
    def __init__(self):
        self.aircraft_list = []

    def create(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            pilot: bool, altitude: float):
        aircraft = Aircraft(name, max_speed, length, width, height,
            pilot, altitude)
        self.aircraft_list.append(aircraft)
        return aircraft

    def read_all(self):
        return self.aircraft_list

    def read_by_name(self, name: str):
        for aircraft in self.aircraft_list:
            if aircraft.name == name:
                return aircraft
        return None

    def update(self, name: str = None, max_speed: float = None,
            length: float = None, width: float = None,
            height: float = None, pilot: bool = None,
            altitude: float = None):
        aircraft = self.read_by_name(name)
        if aircraft:
            if name is not None:
                aircraft.name = name
            if max_speed is not None:
                aircraft.max_speed = max_speed
            if length is not None:
                aircraft.length = length
            if width is not None:
                aircraft.width = width
            if height is not None:
                aircraft.height = height
            if pilot is not None:
                aircraft.pilot = pilot
            if altitude is not None:
                aircraft.altitude = altitude
            return aircraft
        return None

    def delete(self, name: str):
        aircraft = self.read_by_name(name)
        if aircraft:
            self.aircraft_list.remove(aircraft)
            return f"Aircraft with name {name} has been deleted."
        return "Aircraft not found."


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


class FighterJetManager:
    def __init__(self):
        self.fighter_jet_list = []

    def create(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, weapons_system: str):
        fighter_jet = FighterJet(name, max_speed, length, width,
            height, altitude, weapons_system)
        self.fighter_jet_list.append(fighter_jet)
        return fighter_jet

    def read_all(self):
        return self.fighter_jet_list

    def read_by_name(self, name: str):
        for fighter_jet in self.fighter_jet_list:
            if fighter_jet.name == name:
                return fighter_jet
        return None

    def update(self, name: str = None, max_speed: float = None,
            length: float = None, width: float = None,
            height: float = None, altitude: float = None,
            weapons_system: str = None):
        fighter_jet = self.read_by_name(name)
        if fighter_jet:
            if name is not None:
                fighter_jet.name = name
            if max_speed is not None:
                fighter_jet.max_speed = max_speed
            if length is not None:
                fighter_jet.length = length
            if width is not None:
                fighter_jet.width = width
            if height is not None:
                fighter_jet.height = height
            if altitude is not None:
                fighter_jet.altitude = altitude
            if weapons_system is not None:
                fighter_jet.weapons_system = weapons_system
            return fighter_jet
        return None
    
    def delete(self, name: str):
        fighter_jet = self.read_by_name(name)
        if fighter_jet:
            self.fighter_jet_list.remove(fighter_jet)
            return f"Fighter jet with name {name} has been deleted."
        return "Fighter jet not found."


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


class CommercialAircraftManager:
    def __init__(self):
        self.commercial_aircraft_list = []

    def create(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, passengers: int):
        commercial_aircraft = CommercialAircraft(name, max_speed,
            length, width, height, altitude, passengers)
        self.commercial_aircraft_list.append(commercial_aircraft)
        return commercial_aircraft

    def read_all(self):
        return self.commercial_aircraft_list

    def read_by_name(self, name: str):
        for commercial_aircraft in self.commercial_aircraft_list:
            if commercial_aircraft.name == name:
                return commercial_aircraft
        return None

    def update(self, name: str = None, max_speed: float = None,
            length: float = None, width: float = None,
            height: float = None, altitude: float = None,
            passengers: int = None):
        commercial_aircraft = self.read_by_name(name)
        if commercial_aircraft:
            if name is not None:
                commercial_aircraft.name = name
            if max_speed is not None:
                commercial_aircraft.max_speed = max_speed
            if length is not None:
                commercial_aircraft.length = length
            if width is not None:
                commercial_aircraft.width = width
            if height is not None:
                commercial_aircraft.height = height
            if altitude is not None:
                commercial_aircraft.altitude = altitude
            if passengers is not None:
                commercial_aircraft.passengers = passengers
            return commercial_aircraft
        return None
    
    def delete(self, name: str):
        commercial_aircraft = self.read_by_name(name)
        if commercial_aircraft:
            self.commercial_aircraft_list.remove(commercial_aircraft)
            return f"Commercial aircraft\
                with name {name} has been deleted."
        return "Commercial aircraft not found."


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


class HelicopterManager:
    def __init__(self):
        self.helicopter_list = []

    def create(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, rotor_diameter: float):
        helicopter = Helicopter(name, max_speed, length, width,
            height, altitude, rotor_diameter)
        self.helicopter_list.append(helicopter)
        return helicopter

    def read_all(self):
        return self.helicopter_list

    def read_by_name(self, name: str):
        for helicopter in self.helicopter_list:
            if helicopter.name == name:
                return helicopter
        return None

    def update(self, name: str = None, max_speed: float = None,
            length: float = None, width: float = None,
            height: float = None, altitude: float = None,
            rotor_diameter: float = None):
        helicopter = self.read_by_name(name)
        if helicopter:
            if name is not None:
                helicopter.name = name
            if max_speed is not None:
                helicopter.max_speed = max_speed
            if length is not None:
                helicopter.length = length
            if width is not None:
                helicopter.width = width
            if height is not None:
                helicopter.height = height
            if altitude is not None:
                helicopter.altitude = altitude
            if rotor_diameter is not None:
                helicopter.rotor_diameter = rotor_diameter
            return helicopter
        return None
    
    def delete(self, name: str):
        helicopter = self.read_by_name(name)
        if helicopter:
            self.helicopter_list.remove(helicopter)
            return f"Helicopter with name {name} has been deleted."
        return "Helicopter not found."


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


class AutogyroManager:
    def __init__(self):
        self.autogyro_list = []

    def create(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, rotor_diameter: float):
        autogyro = Autogyro(name, max_speed, length, width,
            height, altitude, rotor_diameter)
        self.autogyro_list.append(autogyro)
        return autogyro

    def read_all(self):
        return self.autogyro_list

    def read_by_name(self, name: str):
        for autogyro in self.autogyro_list:
            if autogyro.name == name:
                return autogyro
        return None

    def update(self, name: str = None, max_speed: float = None,
            length: float = None, width: float = None,
            height: float = None, altitude: float = None,
            rotor_diameter: float = None):
        autogyro = self.read_by_name(name)
        if autogyro:
            if name is not None:
                autogyro.name = name
            if max_speed is not None:
                autogyro.max_speed = max_speed
            if length is not None:
                autogyro.length = length
            if width is not None:
                autogyro.width = width
            if height is not None:
                autogyro.height = height
            if altitude is not None:
                autogyro.altitude = altitude
            if rotor_diameter is not None:
                autogyro.rotor_diameter = rotor_diameter
            return autogyro
        return None
    
    def delete(self, name: str):
        autogyro = self.read_by_name(name)
        if autogyro:
            self.autogyro_list.remove(autogyro)
            return f"Autogyro with name {name} has been deleted."
        return "Autogyro not found."


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

        super().__init__(name, max_speed, length, width, height, False,
            altitude)
        self.control_range = control_range


class DroneManager:
    def __init__(self):
        self.drone_list = []

    def create(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, control_range: float):
        drone = Drone(name, max_speed, length, width,
            height, altitude, control_range)
        self.drone_list.append(drone)
        return drone

    def read_all(self):
        return self.drone_list

    def read_by_name(self, name: str):
        for drone in self.drone_list:
            if drone.name == name:
                return drone
        return None

    def update(self, name: str = None, max_speed: float = None,
            length: float = None, width: float = None,
            height: float = None, altitude: float = None,
            control_range: float = None):
        drone = self.read_by_name(name)
        if drone:
            if name is not None:
                drone.name = name
            if max_speed is not None:
                drone.max_speed = max_speed
            if length is not None:
                drone.length = length
            if width is not None:
                drone.width = width
            if height is not None:
                drone.height = height
            if altitude is not None:
                drone.altitude = altitude
            if control_range is not None:
                drone.control_range = control_range
            return drone
        return None
    
    def delete(self, name: str):
        drone = self.read_by_name(name)
        if drone:
            self.drone_list.remove(drone)
            return f"Drone with name {name} has been deleted."
        return "Drone not found."


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


class ZeppelinManager:
    def __init__(self):
        self.zeppelin_list = []

    def create(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, gas_capacity: float):
        zeppelin = Zeppelin(name, max_speed, length, width,
            height, altitude, gas_capacity)
        self.zeppelin_list.append(zeppelin)
        return zeppelin

    def read_all(self):
        return self.zeppelin_list

    def read_by_name(self, name: str):
        for zeppelin in self.zeppelin_list:
            if zeppelin.name == name:
                return zeppelin
        return None

    def update(self, name: str = None, max_speed: float = None,
            length: float = None, width: float = None,
            height: float = None, altitude: float = None,
            gas_capacity: float = None):
        zeppelin = self.read_by_name(name)
        if zeppelin:
            if name is not None:
                zeppelin.name = name
            if max_speed is not None:
                zeppelin.max_speed = max_speed
            if length is not None:
                zeppelin.length = length
            if width is not None:
                zeppelin.width = width
            if height is not None:
                zeppelin.height = height
            if altitude is not None:
                zeppelin.altitude = altitude
            if gas_capacity is not None:
                zeppelin.gas_capacity = gas_capacity
            return zeppelin
        return None
    
    def delete(self, name: str):
        zeppelin = self.read_by_name(name)
        if zeppelin:
            self.zeppelin_list.remove(zeppelin)
            return f"Zeppelin with name {name} has been deleted."
        return "Zeppelin not found."


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


class BalloonManager:
    def __init__(self):
        self.balloon_list = []

    def create(self, name: str, max_speed: float,
            length: float, width: float, height: float,
            altitude: float, gas_capacity: float):
        balloon = Balloon(name, max_speed, length, width,
            height, altitude, gas_capacity)
        self.balloon_list.append(balloon)
        return balloon

    def read_all(self):
        return self.balloon_list

    def read_by_name(self, name: str):
        for balloon in self.balloon_list:
            if balloon.name == name:
                return balloon
        return None

    def update(self, name: str = None, max_speed: float = None,
            length: float = None, width: float = None,
            height: float = None, altitude: float = None,
            gas_capacity: float = None):
        balloon = self.read_by_name(name)
        if balloon:
            if name is not None:
                balloon.name = name
            if max_speed is not None:
                balloon.max_speed = max_speed
            if length is not None:
                balloon.length = length
            if width is not None:
                balloon.width = width
            if height is not None:
                balloon.height = height
            if altitude is not None:
                balloon.altitude = altitude
            if gas_capacity is not None:
                balloon.gas_capacity = gas_capacity
            return balloon
        return None
    
    def delete(self, name: str):
        balloon = self.read_by_name(name)
        if balloon:
            self.balloon_list.remove(balloon)
            return f"Balloon with name {name} has been deleted."
        return "Balloon not found."


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


class SpacecraftManager:
    def __init__(self):
        self.spacecraft_list = []

    def create(self, name: str, max_thrust: float,
            height: float, diameter: float):
        spacecraft = Spacecraft(name, max_thrust, height, diameter)
        self.spacecraft_list.append(spacecraft)
        return spacecraft

    def read_all(self):
        return self.spacecraft_list

    def read_by_name(self, name: str):
        for spacecraft in self.spacecraft_list:
            if spacecraft.name == name:
                return spacecraft
        return None

    def update(self, name: str = None, max_thrust: float = None,
            height: float = None, diameter: float = None):
        spacecraft = self.read_by_name(name)
        if spacecraft:
            if name is not None:
                spacecraft.name = name
            if max_thrust is not None:
                spacecraft.max_thrust = max_thrust
            if height is not None:
                spacecraft.height = height
            if diameter is not None:
                spacecraft.diameter = diameter
            return spacecraft
        return None
    
    def delete(self, name: str):
        spacecraft = self.read_by_name(name)
        if spacecraft:
            self.spacecraft_list.remove(spacecraft)
            return f"Spacecraft with name {name} has been deleted."
        return "Spacecraft not found."


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


class CargoSpacecraftManager:
    def __init__(self):
        self.cargo_spacecraft_list = []

    def create(self, name: str, max_thrust: float,
            height: float, diameter: float, cargo_weight: float):
        cargo_spacecraft = CargoSpacecraft(name, max_thrust, height,
            diameter, cargo_weight)
        self.cargo_spacecraft_list.append(cargo_spacecraft)
        return cargo_spacecraft

    def read_all(self):
        return self.cargo_spacecraft_list

    def read_by_name(self, name: str):
        for cargo_spacecraft in self.cargo_spacecraft_list:
            if cargo_spacecraft.name == name:
                return cargo_spacecraft
        return None

    def update(self, name: str = None, max_thrust: float = None,
            height: float = None, diameter: float = None,
            cargo_weight: float = None):
        cargo_spacecraft = self.read_by_name(name)
        if cargo_spacecraft:
            if name is not None:
                cargo_spacecraft.name = name
            if max_thrust is not None:
                cargo_spacecraft.max_thrust = max_thrust
            if height is not None:
                cargo_spacecraft.height = height
            if diameter is not None:
                cargo_spacecraft.diameter = diameter
            if cargo_weight is not None:
                cargo_spacecraft.cargo_weight = cargo_weight
            return cargo_spacecraft
        return None
    
    def delete(self, name: str):
        cargo_spacecraft = self.read_by_name(name)
        if cargo_spacecraft:
            self.cargo_spacecraft_list.remove(cargo_spacecraft)
            return f"Cargo spacecraft with name {name}\
                has been deleted."
        return "Cargo spacecraft not found."


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


class CommercialSpacecraftManager:
    def __init__(self):
        self.cargo_spacecraft_list = []

    def create(self, name: str, max_thrust: float,
            height: float, diameter: float, passengers: int):
        cargo_spacecraft = CommercialSpacecraft(name, max_thrust,
            height, diameter, passengers)
        self.cargo_spacecraft_list.append(cargo_spacecraft)
        return cargo_spacecraft

    def read_all(self):
        return self.cargo_spacecraft_list

    def read_by_name(self, name: str):
        for cargo_spacecraft in self.cargo_spacecraft_list:
            if cargo_spacecraft.name == name:
                return cargo_spacecraft
        return None

    def update(self, name: str = None, max_thrust: float = None,
            height: float = None, diameter: float = None,
            passengers: int = None):
        cargo_spacecraft = self.read_by_name(name)
        if cargo_spacecraft:
            if name is not None:
                cargo_spacecraft.name = name
            if max_thrust is not None:
                cargo_spacecraft.max_thrust = max_thrust
            if height is not None:
                cargo_spacecraft.height = height
            if diameter is not None:
                cargo_spacecraft.diameter = diameter
            if passengers is not None:
                cargo_spacecraft.passengers = passengers
            return cargo_spacecraft
        return None
    
    def delete(self, name: str):
        cargo_spacecraft = self.read_by_name(name)
        if cargo_spacecraft:
            self.cargo_spacecraft_list.remove(cargo_spacecraft)
            return f"Commercial spacecraft with name {name}\
                has been deleted."
        return "Commercial spacecraft not found."
