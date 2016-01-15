def mean(vals):
  "calculate the arithmetic mean of the list"

  assert type(vals) is list, 'wrong input format'
  total = sum(vals)
  length = len(vals)
  if length == 0:
    return 0.0
  return total/length

def test_mean():
  assert mean([2,4]) == 3.0
test_mean()

def test_empty_list():
  assert mean([]) == 0.0
test_empty_list()


print(mean([]))
#print(mean('hello'))