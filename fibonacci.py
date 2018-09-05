# sequence = [1, 1]
#
# for _ in range(1, 5000):
#     next_in_sequence = sequence[0] + sequence[1]
#     sequence[0] = sequence[1] # Take the thing in sequence[1], put it in postion 0
#     sequence[1] = next_in_sequence # Take the thing in next_in_sequence, put it in postion 1

def memoize(fn):
  """ Decorator to memoize the result of a given function """
  cache = {}
  def memoizer(*args):
    if args not in cache:
      cache[args] = fn(*args)
    return cache[args]
  return memoizer

@memoize
def fib(n):
  """ Calculate the nth Fibonacci number """
  if n == 0 or n == 1
    return n
  return fib(n-1) + fib(n-2)

print fib(250)
