from collections import namedtuple
import functools
import requests


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def expensive_call(str1: str, str2: str):
    return {'prop': [str1, str2]}


def memoize_func(func):
    cache: dict = {}

    def inner_func(*args):
        argsStr = ''.join(list(args))
        if argsStr in cache:
            print('from cache')
            return cache[argsStr]
        else:
            value = func(*args)
            cache[argsStr] = value
            print('not from cache')
            return value

    return inner_func


m = memoize_func(expensive_call)
#m('kevin', 'b')
#m('kevin', 'b')

N = namedtuple('N', ['a', 'b', 'c'])
n = N(a={'foo': 'bar'}, b='hi', c=[])


def testing_args(*args):
    counter = 0
    return functools.reduce(lambda accum, e: accum.update({e[0]: e[1]}) or accum, enumerate(list(args)), {})


print(testing_args('1', 2))

r = requests.get("https://catfact.ninja/breeds?limit=1")
print(r.status_code, r.json()['data'])
