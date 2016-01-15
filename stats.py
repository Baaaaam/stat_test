def mean(vals):
  "calculate the arithmetic mean of the list"

  assert type(vals) is list, 'wrong input format'
  total = sum(vals)
  length = len(vals)
  return total/length

print(mean([2,4]))
print(mean('hello'))