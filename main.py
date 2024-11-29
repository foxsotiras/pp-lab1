import json
from xml.etree import ElementTree as tree


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

    def from_json(self, data: dict):
        for aircraft in data["aircraft_list"]:
            name = aircraft["name"]
            max_speed = float(aircraft["max_speed"])
            length = float(aircraft["length"])
            width = float(aircraft["width"])
            height = float(aircraft["height"])
            pilot = bool(aircraft["pilot"])
            altitude = float(aircraft["altitude"])
            self.create(name, max_speed, length, width, height,
                pilot, altitude)

    def save_to_json(self) -> dict:
        to_json = {
            "aircraft_list": []
        }
        for aircraft in self.aircraft_list:
            to_json["aircraft_list"].append({
                "name": aircraft.name,
                "max_speed": aircraft.max_speed,
                "length": aircraft.length,
                "width": aircraft.width,
                "height": aircraft.height,
                "pilot": aircraft.pilot,
                "altitude": aircraft.altitude
            })

        return to_json

    def from_xml(self, root: tree):
        for aircraft in root.find("aircraft_list"):
            name = aircraft.find("name").text
            max_speed = float(aircraft.find("max_speed").text)
            length = float(aircraft.find("length").text)
            width = float(aircraft.find("width").text)
            height = float(aircraft.find("height").text)
            pilot = bool(aircraft.find("pilot").text)
            altitude = float(aircraft.find("altitude").text)
            self.create(name, max_speed, length, width, height, pilot,
                altitude)

    def save_to_xml(self) -> tree.Element:
        to_xml = tree.Element("aircraft_list")
        for aircraft in self.aircraft_list:
            aircraft_item = tree.Element("aircraft")
            tree.SubElement(aircraft_item, "name").text =\
                aircraft.name
            tree.SubElement(aircraft_item, "max_speed").text =\
                str(aircraft.max_speed)
            tree.SubElement(aircraft_item, "length").text =\
                str(aircraft.length)
            tree.SubElement(aircraft_item, "width").text =\
                str(aircraft.width)
            tree.SubElement(aircraft_item, "height").text =\
                str(aircraft.height)
            tree.SubElement(aircraft_item, "pilot").text =\
                str(aircraft.pilot)
            tree.SubElement(aircraft_item, "altitude").text =\
                str(aircraft.altitude)
            to_xml.append(aircraft_item)

        return to_xml


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

    def from_json(self, data: dict):
        for fighter_jet in data["fighter_jet_list"]:
            name = fighter_jet["name"]
            max_speed = float(fighter_jet["max_speed"])
            length = float(fighter_jet["length"])
            width = float(fighter_jet["width"])
            height = float(fighter_jet["height"])
            altitude = float(fighter_jet["altitude"])
            weapons_system = fighter_jet["weapons_system"]
            self.create(name, max_speed, length, width, height,
                altitude, weapons_system)

    def save_to_json(self) -> dict:
        to_json = {
            "fighter_jet_list": []
        }
        for fighter_jet in self.fighter_jet_list:
            to_json["fighter_jet_list"].append({
                "name": fighter_jet.name,
                "max_speed": fighter_jet.max_speed,
                "length": fighter_jet.length,
                "width": fighter_jet.width,
                "height": fighter_jet.height,
                "altitude": fighter_jet.altitude,
                "weapons_system": fighter_jet.weapons_system
            })

        return to_json

    def from_xml(self, root: tree):
        for fighter_jet in root.find("fighter_jet_list"):
            name = fighter_jet.find("name").text
            max_speed = float(fighter_jet.find("max_speed").text)
            length = float(fighter_jet.find("length").text)
            width = float(fighter_jet.find("width").text)
            height = float(fighter_jet.find("height").text)
            altitude = float(fighter_jet.find("altitude").text)
            weapons_system = fighter_jet.find("weapons_system").text
            self.create(name, max_speed, length, width, height,
                altitude, weapons_system)

    def save_to_xml(self) -> tree.Element:
        to_xml = tree.Element("fighter_jet_list")
        for fighter_jet in self.fighter_jet_list:
            fighter_jet_item = tree.Element("fighter_jet")
            tree.SubElement(fighter_jet_item, "name").text =\
                fighter_jet.name
            tree.SubElement(fighter_jet_item, "max_speed").text =\
                str(fighter_jet.max_speed)
            tree.SubElement(fighter_jet_item, "length").text =\
                str(fighter_jet.length)
            tree.SubElement(fighter_jet_item, "width").text =\
                str(fighter_jet.width)
            tree.SubElement(fighter_jet_item, "height").text =\
                str(fighter_jet.height)
            tree.SubElement(fighter_jet_item, "altitude").text =\
                str(fighter_jet.altitude)
            tree.SubElement(fighter_jet_item, "weapons_system").text =\
                fighter_jet.weapons_system
            to_xml.append(fighter_jet_item)

        return to_xml


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

    def from_json(self, data: dict):
        for commercial_aircraft in data["commercial_aircraft_list"]:
            name = commercial_aircraft["name"]
            max_speed = float(commercial_aircraft["max_speed"])
            length = float(commercial_aircraft["length"])
            width = float(commercial_aircraft["width"])
            height = float(commercial_aircraft["height"])
            altitude = float(commercial_aircraft["altitude"])
            passengers = int(commercial_aircraft["passengers"])
            self.create(name, max_speed, length, width, height,
                altitude, passengers)

    def save_to_json(self) -> dict:
        to_json = {
            "commercial_aircraft_list": []
        }
        for commercial_aircraft in self.commercial_aircraft_list:
            to_json["commercial_aircraft_list"].append({
                "name": commercial_aircraft.name,
                "max_speed": commercial_aircraft.max_speed,
                "length": commercial_aircraft.length,
                "width": commercial_aircraft.width,
                "height": commercial_aircraft.height,
                "altitude": commercial_aircraft.altitude,
                "passengers": commercial_aircraft.passengers
            })

        return to_json

    def from_xml(self, root: tree):
        for commercial_aircraft in\
                root.find("commercial_aircraft_list"):
            name = commercial_aircraft.find("name").text
            max_speed = float(commercial_aircraft.find("max_speed").\
                text)
            length = float(commercial_aircraft.find("length").text)
            width = float(commercial_aircraft.find("width").text)
            height = float(commercial_aircraft.find("height").text)
            altitude = float(commercial_aircraft.find("altitude").text)
            passengers = int(commercial_aircraft.\
                find("passengers").text)
            self.create(name, max_speed, length, width, height,
                altitude, passengers)

    def save_to_xml(self) -> tree.Element:
        to_xml = tree.Element("commercial_aircraft_list")
        for commercial_aircraft in self.commercial_aircraft_list:
            commercial_aircraft_item =\
                tree.Element("commercial_aircraft")
            tree.SubElement(commercial_aircraft_item, "name").text =\
                commercial_aircraft.name
            tree.SubElement(commercial_aircraft_item,
                "max_speed").text =\
                str(commercial_aircraft.max_speed)
            tree.SubElement(commercial_aircraft_item,
                "length").text =\
                str(commercial_aircraft.length)
            tree.SubElement(commercial_aircraft_item, "width").text =\
                str(commercial_aircraft.width)
            tree.SubElement(commercial_aircraft_item,
                "height").text =\
                str(commercial_aircraft.height)
            tree.SubElement(commercial_aircraft_item,
                "altitude").text =\
                str(commercial_aircraft.altitude)
            tree.SubElement(commercial_aircraft_item,
                "passengers").text =\
                str(commercial_aircraft.passengers)
            to_xml.append(commercial_aircraft_item)

        return to_xml


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

    def from_json(self, data: dict):
        for helicopter in data["helicopter_list"]:
            name = helicopter["name"]
            max_speed = float(helicopter["max_speed"])
            length = float(helicopter["length"])
            width = float(helicopter["width"])
            height = float(helicopter["height"])
            altitude = float(helicopter["altitude"])
            rotor_diameter = float(helicopter["rotor_diameter"])
            self.create(name, max_speed, length, width, height,
                altitude, rotor_diameter)

    def save_to_json(self) -> dict:
        to_json = {
            "helicopter_list": []
        }
        for helicopter in self.helicopter_list:
            to_json["helicopter_list"].append({
                "name": helicopter.name,
                "max_speed": helicopter.max_speed,
                "length": helicopter.length,
                "width": helicopter.width,
                "height": helicopter.height,
                "altitude": helicopter.altitude,
                "rotor_diameter": helicopter.rotor_diameter
            })

        return to_json

    def from_xml(self, root: tree):
        for helicopter in root.find("helicopter_list"):
            name = helicopter.find("name").text
            max_speed = float(helicopter.find("max_speed").text)
            length = float(helicopter.find("length").text)
            width = float(helicopter.find("width").text)
            height = float(helicopter.find("height").text)
            altitude = float(helicopter.find("altitude").text)
            rotor_diameter = float(helicopter.\
                find("rotor_diameter").text)
            self.create(name, max_speed, length, width, height,
                altitude, rotor_diameter)

    def save_to_xml(self) -> tree.Element:
        to_xml = tree.Element("helicopter_list")
        for helicopter in self.helicopter_list:
            helicopter_item = tree.Element("helicopter")
            tree.SubElement(helicopter_item, "name").text =\
                helicopter.name
            tree.SubElement(helicopter_item, "max_speed").text =\
                str(helicopter.max_speed)
            tree.SubElement(helicopter_item, "length").text =\
                str(helicopter.length)
            tree.SubElement(helicopter_item, "width").text =\
                str(helicopter.width)
            tree.SubElement(helicopter_item, "height").text =\
                str(helicopter.height)
            tree.SubElement(helicopter_item, "altitude").text =\
                str(helicopter.altitude)
            tree.SubElement(helicopter_item, "rotor_diameter").text =\
                str(helicopter.rotor_diameter)
            to_xml.append(helicopter_item)

        return to_xml


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

    def from_json(self, data: dict):
        for autogyro in data["autogyro_list"]:
            name = autogyro["name"]
            max_speed = float(autogyro["max_speed"])
            length = float(autogyro["length"])
            width = float(autogyro["width"])
            height = float(autogyro["height"])
            altitude = float(autogyro["altitude"])
            rotor_diameter = float(autogyro["rotor_diameter"])
            self.create(name, max_speed, length, width, height,
                altitude, rotor_diameter)

    def save_to_json(self) -> dict:
        to_json = {
            "autogyro_list": []
        }
        for autogyro in self.autogyro_list:
            to_json["autogyro_list"].append({
                "name": autogyro.name,
                "max_speed": autogyro.max_speed,
                "length": autogyro.length,
                "width": autogyro.width,
                "height": autogyro.height,
                "altitude": autogyro.altitude,
                "rotor_diameter": autogyro.rotor_diameter
            })

        return to_json

    def from_xml(self, root: tree):
        for autogyro in root.find("autogyro_list"):
            name = autogyro.find("name").text
            max_speed = float(autogyro.find("max_speed").text)
            length = float(autogyro.find("length").text)
            width = float(autogyro.find("width").text)
            height = float(autogyro.find("height").text)
            altitude = float(autogyro.find("altitude").text)
            rotor_diameter = float(autogyro.\
                find("rotor_diameter").text)
            self.create(name, max_speed, length, width, height,
                altitude, rotor_diameter)

    def save_to_xml(self) -> tree.Element:
        to_xml = tree.Element("autogyro_list")
        for autogyro in self.autogyro_list:
            autogyro_item = tree.Element("autogyro")
            tree.SubElement(autogyro_item, "name").text =\
                autogyro.name
            tree.SubElement(autogyro_item, "max_speed").text =\
                str(autogyro.max_speed)
            tree.SubElement(autogyro_item, "length").text =\
                str(autogyro.length)
            tree.SubElement(autogyro_item, "width").text =\
                str(autogyro.width)
            tree.SubElement(autogyro_item, "height").text =\
                str(autogyro.height)
            tree.SubElement(autogyro_item, "altitude").text =\
                str(autogyro.altitude)
            tree.SubElement(autogyro_item, "rotor_diameter").text =\
                str(autogyro.rotor_diameter)
            to_xml.append(autogyro_item)

        return to_xml


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

    def from_json(self, data: dict):
        for drone in data["drone_list"]:
            name = drone["name"]
            max_speed = float(drone["max_speed"])
            length = float(drone["length"])
            width = float(drone["width"])
            height = float(drone["height"])
            altitude = float(drone["altitude"])
            control_range = float(drone["control_range"])
            self.create(name, max_speed, length, width, height,
                altitude, control_range)

    def save_to_json(self) -> dict:
        to_json = {
            "drone_list": []
        }
        for drone in self.drone_list:
            to_json["drone_list"].append({
                "name": drone.name,
                "max_speed": drone.max_speed,
                "length": drone.length,
                "width": drone.width,
                "height": drone.height,
                "altitude": drone.altitude,
                "control_range": drone.control_range
            })

        return to_json

    def from_xml(self, root: tree):
        for drone in root.find("drone_list"):
            name = drone.find("name").text
            max_speed = float(drone.find("max_speed").text)
            length = float(drone.find("length").text)
            width = float(drone.find("width").text)
            height = float(drone.find("height").text)
            altitude = float(drone.find("altitude").text)
            control_range = float(drone.find("control_range").text)
            self.create(name, max_speed, length, width, height,
                altitude, control_range)

    def save_to_xml(self) -> tree.Element:
        to_xml = tree.Element("drone_list")
        for drone in self.drone_list:
            drone_item = tree.Element("drone")
            tree.SubElement(drone_item, "name").text =\
                drone.name
            tree.SubElement(drone_item, "max_speed").text =\
                str(drone.max_speed)
            tree.SubElement(drone_item, "length").text =\
                str(drone.length)
            tree.SubElement(drone_item, "width").text =\
                str(drone.width)
            tree.SubElement(drone_item, "height").text =\
                str(drone.height)
            tree.SubElement(drone_item, "altitude").text =\
                str(drone.altitude)
            tree.SubElement(drone_item, "control_range").text =\
                str(drone.control_range)
            to_xml.append(drone_item)

        return to_xml


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

    def from_json(self, data: dict):
        for zeppelin in data["zeppelin_list"]:
            name = zeppelin["name"]
            max_speed = float(zeppelin["max_speed"])
            length = float(zeppelin["length"])
            width = float(zeppelin["width"])
            height = float(zeppelin["height"])
            altitude = float(zeppelin["altitude"])
            gas_capacity = float(zeppelin["gas_capacity"])
            self.create(name, max_speed, length, width, height,
                altitude, gas_capacity)

    def save_to_json(self) -> dict:
        to_json = {
            "zeppelin_list": []
        }
        for zeppelin in self.zeppelin_list:
            to_json["zeppelin_list"].append({
                "name": zeppelin.name,
                "max_speed": zeppelin.max_speed,
                "length": zeppelin.length,
                "width": zeppelin.width,
                "height": zeppelin.height,
                "altitude": zeppelin.altitude,
                "gas_capacity": zeppelin.gas_capacity
            })

        return to_json

    def from_xml(self, root: tree):
        for zeppelin in root.find("zeppelin_list"):
            name = zeppelin.find("name").text
            max_speed = float(zeppelin.find("max_speed").text)
            length = float(zeppelin.find("length").text)
            width = float(zeppelin.find("width").text)
            height = float(zeppelin.find("height").text)
            altitude = float(zeppelin.find("altitude").text)
            gas_capacity = float(zeppelin.find("gas_capacity").text)
            self.create(name, max_speed, length, width, height,
                altitude, gas_capacity)

    def save_to_xml(self) -> tree.Element:
        to_xml = tree.Element("zeppelin_list")
        for zeppelin in self.zeppelin_list:
            zeppelin_item = tree.Element("zeppelin")
            tree.SubElement(zeppelin_item, "name").text =\
                zeppelin.name
            tree.SubElement(zeppelin_item, "max_speed").text =\
                str(zeppelin.max_speed)
            tree.SubElement(zeppelin_item, "length").text =\
                str(zeppelin.length)
            tree.SubElement(zeppelin_item, "width").text =\
                str(zeppelin.width)
            tree.SubElement(zeppelin_item, "height").text =\
                str(zeppelin.height)
            tree.SubElement(zeppelin_item, "altitude").text =\
                str(zeppelin.altitude)
            tree.SubElement(zeppelin_item, "gas_capacity").text =\
                str(zeppelin.gas_capacity)
            to_xml.append(zeppelin_item)

        return to_xml


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

    def from_json(self, data: dict):
        for balloon in data["balloon_list"]:
            name = balloon["name"]
            max_speed = float(balloon["max_speed"])
            length = float(balloon["length"])
            width = float(balloon["width"])
            height = float(balloon["height"])
            altitude = float(balloon["altitude"])
            gas_capacity = float(balloon["gas_capacity"])
            self.create(name, max_speed, length, width, height,
                altitude, gas_capacity)

    def save_to_json(self) -> dict:
        to_json = {
            "balloon_list": []
        }
        for balloon in self.balloon_list:
            to_json["balloon_list"].append({
                "name": balloon.name,
                "max_speed": balloon.max_speed,
                "length": balloon.length,
                "width": balloon.width,
                "height": balloon.height,
                "altitude": balloon.altitude,
                "gas_capacity": balloon.gas_capacity
            })

        return to_json

    def from_xml(self, root: tree):
        for balloon in root.find("balloon_list"):
            name = balloon.find("name").text
            max_speed = float(balloon.find("max_speed").text)
            length = float(balloon.find("length").text)
            width = float(balloon.find("width").text)
            height = float(balloon.find("height").text)
            altitude = float(balloon.find("altitude").text)
            gas_capacity = float(balloon.find("gas_capacity").text)
            self.create(name, max_speed, length, width, height,
                altitude, gas_capacity)

    def save_to_xml(self) -> tree.Element:
        to_xml = tree.Element("balloon_list")
        for balloon in self.balloon_list:
            balloon_item = tree.Element("balloon")
            tree.SubElement(balloon_item, "name").text =\
                balloon.name
            tree.SubElement(balloon_item, "max_speed").text =\
                str(balloon.max_speed)
            tree.SubElement(balloon_item, "length").text =\
                str(balloon.length)
            tree.SubElement(balloon_item, "width").text =\
                str(balloon.width)
            tree.SubElement(balloon_item, "height").text =\
                str(balloon.height)
            tree.SubElement(balloon_item, "altitude").text =\
                str(balloon.altitude)
            tree.SubElement(balloon_item, "gas_capacity").text =\
                str(balloon.gas_capacity)
            to_xml.append(balloon_item)

        return to_xml


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

    def from_json(self, data: dict):
        for spacecraft in data["spacecraft_list"]:
            name = spacecraft["name"]
            max_thrust = float(spacecraft["max_thrust"])
            height = float(spacecraft["height"])
            diameter = float(spacecraft["diameter"])
            self.create(name, max_thrust, height, diameter)

    def save_to_json(self) -> dict:
        to_json = {
            "spacecraft_list": []
        }
        for spacecraft in self.spacecraft_list:
            to_json["spacecraft_list"].append({
                "name": spacecraft.name,
                "max_thrust": spacecraft.max_thrust,
                "height": spacecraft.height,
                "diameter": spacecraft.diameter
            })

        return to_json

    def from_xml(self, root: tree): 
        for spacecraft in root.find("spacecraft_list"):
            name = spacecraft.find("name").text
            max_thrust = float(spacecraft.find("max_thrust").text)
            height = float(spacecraft.find("height").text)
            diameter = float(spacecraft.find("diameter").text)
            self.create(name, max_thrust, height, diameter)

    def save_to_xml(self) -> tree.Element:
        to_xml = tree.Element("spacecraft_list")
        for spacecraft in self.spacecraft_list:
            spacecraft_item = tree.Element("spacecraft")
            tree.SubElement(spacecraft_item, "name").text =\
                spacecraft.name
            tree.SubElement(spacecraft_item, "max_thrust").text =\
                str(spacecraft.max_thrust)
            tree.SubElement(spacecraft_item, "height").text =\
                str(spacecraft.height)
            tree.SubElement(spacecraft_item, "diameter").text =\
                str(spacecraft.diameter)
            to_xml.append(spacecraft_item)

        return to_xml


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

    def from_json(self, data: dict):
        for cargo_spacecraft in data["cargo_spacecraft_list"]:
            name = cargo_spacecraft["name"]
            max_thrust = float(cargo_spacecraft["max_thrust"])
            height = float(cargo_spacecraft["height"])
            diameter = float(cargo_spacecraft["diameter"])
            cargo_weight = float(cargo_spacecraft["cargo_weight"])
            self.create(name, max_thrust, height, diameter,
                cargo_weight)

    def save_to_json(self) -> dict:
        to_json = {
            "cargo_spacecraft_list": []
        }
        for cargo_spacecraft in self.cargo_spacecraft_list:
            to_json["cargo_spacecraft_list"].append({
                "name": cargo_spacecraft.name,
                "max_thrust": cargo_spacecraft.max_thrust,
                "height": cargo_spacecraft.height,
                "diameter": cargo_spacecraft.diameter,
                "cargo_weight": cargo_spacecraft.cargo_weight
            })

        return to_json

    def from_xml(self, root: tree): 
        for cargo_spacecraft in root.find("cargo_spacecraft_list"):
            name = cargo_spacecraft.find("name").text
            max_thrust = float(cargo_spacecraft.\
                find("max_thrust").text)
            height = float(cargo_spacecraft.find("height").text)
            diameter = float(cargo_spacecraft.find("diameter").text)
            cargo_weight = float(cargo_spacecraft.\
                find("cargo_weight").text)
            self.create(name, max_thrust, height, diameter,
                cargo_weight)

    def save_to_xml(self) -> tree.Element:
        to_xml = tree.Element("cargo_spacecraft_list")
        for cargo_spacecraft in self.cargo_spacecraft_list:
            cargo_spacecraft_item = tree.Element("cargo_spacecraft")
            tree.SubElement(cargo_spacecraft_item, "name").text =\
                cargo_spacecraft.name
            tree.SubElement(cargo_spacecraft_item,
                "max_thrust").text =\
                str(cargo_spacecraft.max_thrust)
            tree.SubElement(cargo_spacecraft_item, "height").text =\
                str(cargo_spacecraft.height)
            tree.SubElement(cargo_spacecraft_item, "diameter").text =\
                str(cargo_spacecraft.diameter)
            tree.SubElement(cargo_spacecraft_item,
                "cargo_weight").text =\
                str(cargo_spacecraft.cargo_weight)
            to_xml.append(cargo_spacecraft_item)

        return to_xml


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
        self.commercial_spacecraft_list = []

    def create(self, name: str, max_thrust: float,
            height: float, diameter: float, passengers: int):
        commercial_spacecraft = CommercialSpacecraft(name, max_thrust,
            height, diameter, passengers)
        self.commercial_spacecraft_list.append(commercial_spacecraft)
        return commercial_spacecraft

    def read_all(self):
        return self.commercial_spacecraft_list

    def read_by_name(self, name: str):
        for commercial_spacecraft in self.commercial_spacecraft_list:
            if commercial_spacecraft.name == name:
                return commercial_spacecraft
        return None

    def update(self, name: str = None, max_thrust: float = None,
            height: float = None, diameter: float = None,
            passengers: int = None):
        commercial_spacecraft = self.read_by_name(name)
        if commercial_spacecraft:
            if name is not None:
                commercial_spacecraft.name = name
            if max_thrust is not None:
                commercial_spacecraft.max_thrust = max_thrust
            if height is not None:
                commercial_spacecraft.height = height
            if diameter is not None:
                commercial_spacecraft.diameter = diameter
            if passengers is not None:
                commercial_spacecraft.passengers = passengers
            return commercial_spacecraft
        return None

    def delete(self, name: str):
        commercial_spacecraft = self.read_by_name(name)
        if commercial_spacecraft:
            self.commercial_spacecraft_list.\
                remove(commercial_spacecraft)
            return f"Commercial spacecraft with name {name}\
                has been deleted."
        return "Commercial spacecraft not found."

    def from_json(self, data: dict):
        for commercial_spacecraft in\
                data["commercial_spacecraft_list"]:
            name = commercial_spacecraft["name"]
            max_thrust = float(commercial_spacecraft["max_thrust"])
            height = float(commercial_spacecraft["height"])
            diameter = float(commercial_spacecraft["diameter"])
            passengers =\
                int(commercial_spacecraft["passengers"])
            self.create(name, max_thrust, height, diameter,
                passengers)

    def save_to_json(self) -> dict:
        to_json = {
            "commercial_spacecraft_list": []
        }
        for commercial_spacecraft in self.commercial_spacecraft_list:
            to_json["commercial_spacecraft_list"].append({
                "name": commercial_spacecraft.name,
                "max_thrust": commercial_spacecraft.max_thrust,
                "height": commercial_spacecraft.height,
                "diameter": commercial_spacecraft.diameter,
                "passengers": commercial_spacecraft.\
                    passengers
            })

        return to_json

    def from_xml(self, root: tree):
        for commercial_spacecraft in\
                root.find("commercial_spacecraft_list"):
            name = commercial_spacecraft.find("name").text
            max_thrust = float(commercial_spacecraft.\
                find("max_thrust").text)
            height = float(commercial_spacecraft.\
                find("height").text)
            diameter = float(commercial_spacecraft.\
                find("diameter").text)
            passengers = int(commercial_spacecraft.\
                find("passengers").text)
            self.create(name, max_thrust, height, diameter,
                passengers)

    def save_to_xml(self) -> tree.Element:
        to_xml = tree.Element("commercial_spacecraft_list")
        for commercial_spacecraft in self.commercial_spacecraft_list:
            commercial_spacecraft_item =\
                tree.Element("commercial_spacecraft")
            tree.SubElement(commercial_spacecraft_item,
                "name").text =\
                commercial_spacecraft.name
            tree.SubElement(commercial_spacecraft_item,
                "max_thrust").text =\
                str(commercial_spacecraft.max_thrust)
            tree.SubElement(commercial_spacecraft_item,
                "height").text =\
                str(commercial_spacecraft.height)
            tree.SubElement(commercial_spacecraft_item,
                "diameter").text =\
                str(commercial_spacecraft.diameter)
            tree.SubElement(commercial_spacecraft_item,
                "passengers").text =\
                str(commercial_spacecraft.passengers)
            to_xml.append(commercial_spacecraft_item)

        return to_xml


def load_json(file_name: str) -> dict:
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data

def write_json(file_name: str, *args: dict):
    output_dict = {}
    for item in args:
        output_dict.update(item)
    json_obj = json.dumps(output_dict, indent=4)
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(json_obj)

def load_xml(file_name: str) -> tree:
    input_file = tree.parse(file_name)
    root = input_file.getroot()

    return root

def write_xml(file_name: str, *args: tree.Element):
    root = tree.Element("list")
    for item in args:
        root.append(item)
    tree_obj = tree.ElementTree(root)
    with open(file_name, "wb") as file:
        tree_obj.write(file)

def main():
    json_data = load_json("./data/test.json")
    xml_data = load_xml("./data/test.xml")

    # Инициализация
    aircraft = AircraftManager()
    fighter_jet = FighterJetManager()
    commercial_aircraft = CommercialAircraftManager()
    helicopter = HelicopterManager()
    autogyro = AutogyroManager()
    drone = DroneManager()
    zeppelin = ZeppelinManager()
    balloon = BalloonManager()
    spacecraft = SpacecraftManager()
    cargo_spacecraft = CargoSpacecraftManager()
    commercial_spacecraft = CommercialSpacecraftManager()

    # Чтение данных с json
    aircraft.from_json(json_data)
    fighter_jet.from_json(json_data)
    commercial_aircraft.from_json(json_data)
    helicopter.from_json(json_data)
    autogyro.from_json(json_data)
    drone.from_json(json_data)
    zeppelin.from_json(json_data)
    balloon.from_json(json_data)
    spacecraft.from_json(json_data)
    cargo_spacecraft.from_json(json_data)
    commercial_spacecraft.from_json(json_data)

    # Запись в файлы
    write_json("./data/output.json", aircraft.save_to_json(),
        fighter_jet.save_to_json(),
        commercial_aircraft.save_to_json(),
        helicopter.save_to_json(),
        autogyro.save_to_json(),
        drone.save_to_json(),
        zeppelin.save_to_json(),
        balloon.save_to_json(),
        spacecraft.save_to_json(),
        cargo_spacecraft.save_to_json(),
        commercial_spacecraft.save_to_json())
    write_xml("./data/output.xml", aircraft.save_to_xml(),
        fighter_jet.save_to_xml(),
        commercial_aircraft.save_to_xml(),
        helicopter.save_to_xml(),
        autogyro.save_to_xml(),
        drone.save_to_xml(),
        zeppelin.save_to_xml(),
        balloon.save_to_xml(),
        spacecraft.save_to_xml(),
        cargo_spacecraft.save_to_xml(),
        commercial_spacecraft.save_to_xml())

try:
    main()
except NullStr as e:
    print(e)
except TypeError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
except KeyError as e:
    print(e)
