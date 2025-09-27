# helper.py

"""
DATA STRUCTURE DECISION GUIDE:

Do you have one value or many values?
    Many → Does order matter?
        Yes → Will it change?
            Yes → list
            No  → tuple
        No → Do you need key-value mapping?
            Yes → dict
            No  → set
"""

def recommend_structure(order: bool, changeable: bool, mapping: bool):
    """Return the recommended Python data structure."""
    if order:
        return "list" if changeable else "tuple"
    else:
        return "dict" if mapping else "set"

if __name__ == "__main__":
    print("Welcome to Data Structure Helper!")
    order = input("Do you need order? (y/n): ").lower() == 'y'
    changeable = True
    mapping = False
    if order:
        changeable = input("Will it change? (y/n): ").lower() == 'y'
    else:
        mapping = input("Do you need key→value mapping? (y/n): ").lower() == 'y'

    print("Recommended data structure:", recommend_structure(order, changeable, mapping))
