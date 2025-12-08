import dis

def calculate_sum(a, b):
  return a + b

# Disassemble the function to see bytecode
print("Bytecode for calculate_sum(a, b):")
dis.dis(calculate_sum)