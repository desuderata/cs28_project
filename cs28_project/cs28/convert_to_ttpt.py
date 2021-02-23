"""
Converts alphanumeric to 22pt

author: Yee Hou, Teoh (2471020t)
"""


def to_ttpt(alpha):
    """
    Takes an alphanumeric grade and converts it to 22pt
    Args:
        alpha (str): The alphanumeric grade to convert

    Returns:
        The 22pt grade as an integer
    """

    grades_dict = {"A1": 22, "A2": 21,
                   "A3": 20, "A4": 19,
                   "A5": 18, "B1": 17,
                   "B2": 16, "B3": 15,
                   "C1": 14, "C2": 13,
                   "C3": 12, "D1": 11,
                   "D2": 10, "D3": 9,
                   "E1": 8, "E2": 7,
                   "E3": 6, "F1": 5,
                   "F2": 4, "F3": 3,
                   "G1": 2, "G2": 1,
                   "H": 0, "CW": 0,
                   "CR": 0, "MV": 0
                   }
    return grades_dict[alpha]
