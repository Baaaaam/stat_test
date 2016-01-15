def mean(vals):
  "calculate the arithmetic mean of the list"

  assert type(vals) is list, 'wrong input format'
  total = sum(vals)
  length = len(vals)
  if length == 0:
    return 0.0
  return total/length
