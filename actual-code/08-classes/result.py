
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
    Result(energy=0.01,angle=90,  particle="proton"),
    Result(0.01, 90, "electron")
]   