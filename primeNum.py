import sympy
import pprind

list = [i for i in sympy.sieve.primerage(1,10000)]
pprint.pprint(list, compact = True)

