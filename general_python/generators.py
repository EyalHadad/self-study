import itertools

def iter_primes():
     # an iterator of all numbers between 2 and +infinity
     numbers = itertools.count(2)

     # generate primes forever
     while True:
         # get the first number from the iterator (always a prime)
         prime = next(numbers)
         yield prime
         print("Here")
         # this code iteratively builds up a chain of
         # filters...slightly tricky, but ponder it a bit
         numbers = filter(prime.__rmod__, numbers)


def naama_gen():
    # an iterator of all numbers between 2 and +infinity
    numbers = 2

    while True:
        yield numbers
        numbers *= numbers


n = naama_gen()

print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))

for p in iter_primes():
    if p > 3:
        break
    print (p)