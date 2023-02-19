"""Main Module"""

from points import Point


def main():
    """Main Function"""
    point_1 = Point(val_a=1, val_b=2)
    print(f"x_val= {point_1.x_val}")
    point_1.x_val = 10
    print(f"x_val= {point_1.x_val}")
    del point_1.x_val
    print(f"x_val= {point_1.x_val}")
    point_1.x_val = point_1.start_x_val_value
    print(f"x_val= {point_1.x_val}")


if __name__ == "__main__":
    main()
