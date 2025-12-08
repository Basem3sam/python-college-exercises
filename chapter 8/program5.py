import torch

# Create two tensors
tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])

# Dot product
dot_product = torch.dot(tensor1, tensor2)

# Element-wise multiplication
element_wise = tensor1 * tensor2

print(f"Dot Product: {dot_product}")
print(f"Element-wise Multiplication: {element_wise}")