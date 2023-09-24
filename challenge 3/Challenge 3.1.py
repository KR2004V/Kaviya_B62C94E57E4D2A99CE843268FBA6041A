
#function called linear search product that takes the list of products and a target product name as input.
def linearsearchproduct (productList, targetProduct):
  indices = []
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices

products=["shoes","boot","loater","shoes","sandel","shoes"]
target = "shoes"
target2  = 'apple'
result = linearsearchproduct(products, target)
print(result)