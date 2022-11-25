"""Main Module"""

from points import Point


def main():
    p1 = Point(a=1, b=2)
    print(f"x= {p1.x}")
    p1.x = 10
    print(f"x= {p1.x}")
    del p1.x
    print(f"x= {p1.x}")
    p1.x = p1.start_x_value
    print(f"x= {p1.x}")


if __name__ == '__main__':
    main()
