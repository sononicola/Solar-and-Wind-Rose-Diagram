import pandas as pd

def to_decimal_format(angle:str) -> float:
    """
    Convert angles in the format sessadecimale like 10°15'30'' into the decimal format 10.2583

    """
    if not isinstance(angle, str):
        return ValueError(
            "Angle must be a string in the form: 10°15'30'' or 10°15' or 10° or -10°15'30'' or -10°15' or -10°")

    # Takes the integral part of degree as a positive float
    coef = 1
    if angle.startswith("-"):
        coef = -1
        splitted_int_dec = angle.split("-")[1].split("°")
        intpart = float(splitted_int_dec[0])
    else:
        splitted_int_dec = angle.split("°")
        intpart = float(splitted_int_dec[0])

    splitted_decimals = splitted_int_dec[1].split("'")
    # If there are minutes in the angle
    if len(splitted_decimals) > 1:
        decimal_60 = float(splitted_decimals[0]) / 60
    else:
        decimal_60 = 0.

    # If there are seconds in the angle"
    if len(splitted_decimals) > 2:
        decimal_3600 = float(splitted_decimals[1]) / 3600
    else:
        decimal_3600 = 0.

    return coef * (intpart + decimal_60 + decimal_3600)

    

def set_north_zero(angle: float) -> float:
    """
    Takes an angle where -180 is the North, 0 is the South, and positive is the East plane.
    Returns North as 0 and 180 as South, passing throuth East
    """
    return 360. - (angle + 180.)

def transform_azimut(angle: str | float):
    "specific to this database"
    if isinstance(angle, str):
        return set_north_zero(to_decimal_format(angle))

    # If is a NaN value
    if isinstance(angle, type(pd.NA)):
        return angle

def transform_height(angle: str | float):
    "specific to this database"
    if isinstance(angle, str):
        return to_decimal_format(angle)

    # If is a NaN value
    if isinstance(angle, type(pd.NA)):
        return angle