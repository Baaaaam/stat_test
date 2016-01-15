def mean(vals):
  "calculate the arithmetic mean of the list"
  total = sum(vals)
  length = len(vals)
  return total/length

print(mean([2,4]))