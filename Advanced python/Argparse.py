# import argparse
#
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--number1", help="first number")
#     parser.add_argument("--number2", help="second number")
#     parser.add_argument("--operation", help="operation")
#
#     args = parser.parse_args()
#
#     print(args.number1)
#     print(args.number2)
#     print(args.operation)
#
#     n1 = int(args.number1)
#     n2 = int(args.number2)
#     result = None
#     if args.operation == "add":
#         result = n1+n2
#     elif args.operation == "subtract":
#         result = n1-n2
#     elif args.operation == "multiply":
#         result = n1 * n2
#     else:
#         raise ValueError("Invalid Operation")
#
#     print("Result:", result)

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--physics", help ="physics marks")
    parser.add_argument("--chemistry", help="chemistry marks")
    parser.add_argument("--maths", help="maths marks")

    args = parser.parse_args()

    print(args.physics)
    print(args.chemistry)
    print(args.maths)

    print("Result:", (
        int(args.physics) + int(args.chemistry) + int(args.maths)

    ) /3 )