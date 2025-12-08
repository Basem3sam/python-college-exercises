import dis

# 1. Define square function
def square(x):
    return x * x

# Disassemble square() to see its bytecode
print("Bytecode for square(x):")
dis.dis(square)

# 2. Define multiply function  
def multiply(a, b):
    return a * b

# Disassemble multiply() to compare
print("\nBytecode for multiply(a, b):")
dis.dis(multiply)