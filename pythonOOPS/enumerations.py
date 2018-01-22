import enum

class DaysOfWeek(enum.Enum):
	monday=1
	tuesday=2
	wednesday=3
	thursday=4
	friday=5
	saturday=6
	sunday=7



print("String Representation of enum member is {}".format(DaysOfWeek.tuesday))
print("repr Representation of enum member is {}".format(repr(DaysOfWeek.friday)))

print "thursday" in [day.name for day in DaysOfWeek]

