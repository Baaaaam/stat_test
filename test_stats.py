from stats import mean  
def test_mean():
  assert mean([2,4]) == 3.0
test_mean()

def test_empty_list():
  assert mean([]) == 0.0
test_empty_list()


print(mean([]))
#print(mean('hello'))