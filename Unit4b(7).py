class InvalidMarksError(Exception):
    pass

try:
    m = int(input("Enter marks: "))
    if m < 0 or m > 100:
        raise InvalidMarksError("Invalid marks")
    print("Pass" if m >= 40 else "Fail")

except InvalidMarksError as e:
    print(e)
except ValueError:
    print("Enter a number")
finally:
    print("Program finished")