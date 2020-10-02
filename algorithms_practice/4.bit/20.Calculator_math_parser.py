"""
Contributed by izanbf1803.
Example:
-------------------------------------------------------------------------------------------------
    Code:
        |   exp = "2452 * (3 * 6.5 + 1) * 6 / 235"
        |   print("Expression:", exp)
        |   print("Parsed expression:", mp.parse(exp))
        |   print("Evaluation result:", mp.evaluate(exp))
    Output:
        |   Expression: 2452 * (3 * 6 + 1) * 6 / 235
        |   Parsed expression: ['2452', '*', '(', '3', '*', '6', '+', '1', ')', '*', '6', '/', '235']
        |   Evaluation result: 1189.4808510638297
-------------------------------------------------------------------------------------------------
Now added '^' operator for exponents. (by @goswami-rahul)
"""
from algorithms.calculator.math_parser import evaluate

def main():
    """
        simple user-interface
    """
    print("\t\tCalculator\n\n")
    while True:
        user_input = input("expression or exit: ")
        if user_input == "exit":
            break
        try:
            print("The result is {0}".format(evaluate(user_input)))
        except Exception:
            print("invalid syntax!")
            user_input = input("expression or exit: ")
    print("program end")


if __name__ == "__main__":
    main()