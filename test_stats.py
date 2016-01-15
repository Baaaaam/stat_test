from stats import mean
from nose.tools import assert_equal

def test_mean():
  assert_equal(mean([2,4]), 3.0)
#test_mean()

def test_empty_list():
  assert_equal( mean([]),0.0)
#test_empty_list()

def test_flaot_mean():
  assert_equal( mean([1.5,1.5,0]), 1)
#test_flaot_mean()

print(mean([]))
#print(mean('hello'))