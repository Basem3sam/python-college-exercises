import ast

# The code to analyze
code = "y = (4*5)-3"

# Parse the code into an AST
tree = ast.parse(code)

# Print the AST structure
print("AST structure:")
print(ast.dump(tree, indent=4))