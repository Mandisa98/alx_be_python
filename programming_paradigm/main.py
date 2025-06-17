import sys
from robust_division_calculator import safe_divide

def main():
    # Check if the user typed two numbers
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Grab the two numbers from what the user typed
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Ask the brain (safe_divide) to calculate
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()

