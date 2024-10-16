class ExperimentResult:
    location = "Switzerland"
    def __init__(self, date, value, experiment, unit):
        if unit not in ["m", "cm", "mm"]:
            raise ValueError("Must be m, cm or mm for unit")
        self.experiment = experiment
        self.date = date
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"Experiment at {self.experiment} on {self.date} with value {self.value}"

    def __repr__(self):
        return f"ExperimentResult({self.date}, {self.value}, {self.experiment})"

    def value_in_unit(self, new_unit):
        if new_unit == "m":
            return f"{self.value / 1000}m"

        if new_unit == "cm":
            return f"{self.value / 10}cm"

        return self.value
result1 = ExperimentResult("2024-10-15", 10, "LHC", "mm")
result2 = ExperimentResult("2024-10-14", 8, "LPC", "mm")

print(result1.date)
print(result1.value)
print(result1.experiment)

print(result1)
print(result2.__repr__())

print(result1.value)
print(result1.value_in_unit("m"))
print(result1.value_in_unit("cm"))

print([result1, result2])



print(result1.location)


# class Result:
#     def __init__(self, experiment):
#         self.experiment = experiment
#
# class ExperimentResult(Result):
#     def __init__(self, date, value, experiment):
#         super()
#         self.experiment = experiment
#         self.date = date
#         self.value = value
#
# result1 = ExperimentResult("2024-10-15", 10, "LHC")
# result2 = ExperimentResult("2024-10-14", 8, "LPC")
#
# print(result1.date)
# print(result1.value)
# print(result1.experiment)