def mean(vals):
  "calculate the arithmetic mean of the list"

  assert type(vals) is list, 'wrong input format'

  length = len(vals)
  parsedlist = list();
  for i in range(0, length):
    parsedlist.append(float(vals[i]))

    total = sum(parsedlist)

  if length == 0:
    return 0.0
  return total/length
