from langchain.tools import tool
import ast
import operator

class CalculatorTools():
    @tool("Make a calculation")
    def calculate(expression):
        # Define allowed operators
        allowed_operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.BitXor: operator.xor,
        }

        # Safely evaluate the expression
        try:
            # Parse the expression
            node = ast.parse(expression, mode='eval')

            # Ensure the expression only consists of safe elements
            if not all(isinstance(n, (ast.Expression, ast.Num, ast.BinOp)) and 
                       isinstance(n.op, tuple(allowed_operators.keys())) 
                       for n in ast.walk(node)):
                raise ValueError("Unsafe expression detected")

            # Compile and evaluate the safe expression
            compiled = compile(node, "<string>", "eval")
            return eval(compiled, {"__builtins__": None}, allowed_operators)
        except Exception as e:
            return f"Error in calculation: {str(e)}"
