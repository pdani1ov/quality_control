import sys


def get_triangle_type(a: float, b: float, c: float) -> str:
    if a <= 0 or b <= 0 or c <= 0:
        return "not_triangle"
    if a + b <= c or a + c <= b or b + c <= a:
        return "not_triangle"
    if a == b and a == c:
        return "equilateral"
    if a == b or a == c or b == c:
        return "isosceles"
    return "default"


if len(sys.argv) != 4:
    print("unknown")
else:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
        if a > sys.float_info.max or b > sys.float_info.max or c > sys.float_info.max:
            print("unknown")
        else:
            print(get_triangle_type(a, b, c))
    except ValueError:
        print("unknown")
