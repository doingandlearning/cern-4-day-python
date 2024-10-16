
all_results = [
    {"angle_of_impact": 90, "energy": 0.01, "particle": "proton"},
    {"angle_of_impact": 90, "energy": 0.01, "particle": "proton"},
    {"angle_of_impact": 90, "energy": 0.01, "particle": "proton"},
    {"angle_of_impact": 90, "energy": 0.01, "particle": "proton"},
    {"angle_of_impact": 90, "energy": 0.01, "particl": "proton"},
]

class Result:
    def __init__(self, angle, energy, particle):
        self.angle_of_impact = angle
        self.energy = energy
        self.particle = particle

all_results = [
    Result(angle=90, energy=0.01, particle="proton"),
    Result(90, 0.01, "electron")
]