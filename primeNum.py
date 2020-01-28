import sympy
import pprind

list = [i for i in sympy.sieve.primerage(10000,2147483647)]
pprint.pprint(list, compact = True)

