class InvalidSpeedError(Exception):
    pass

try:
    speed = int(input("Enter speed: "))

    if speed < 0 or speed > 120:
        raise InvalidSpeedError("Speed must be between 0 and 120 km/h")

    print("Valid speed")

except InvalidSpeedError as e:
    print(e)