import sys
import subprocess


def check_test(args: list[str]) -> str:
    command = ['python', 'lw1/triangle.py']
    expected_result = args[-1]
    args.pop()
    for arg in args:
        command.append(arg)
    current_result = subprocess.run(command, capture_output=True, text=True).stdout.strip()
    if expected_result == current_result:
        return "SUCCESS\n"
    else:
        return "ERROR\n"


if len(sys.argv) != 2:
    print("Invalid number of arguments")

try:
    file = open(sys.argv[1], 'r')
    output = open("lw1/output.txt", "w")
    testsStr = file.readlines()
    for test_id, test_data in enumerate(testsStr):
        args = test_data.split()
        result = f"{test_id + 1} - " + check_test(args)
        output.write(result)
except OSError:
    print("Can't open file")
