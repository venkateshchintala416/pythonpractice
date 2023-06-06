# list is unsafe
l1 = [10, 20, 30, 40, 50, 10]
print(l1)
 # output [10, 20, 30, 40, 50, 10]



l2 = [int, float, complex, bool, str, list, tuple, set, frozenset, dict, bytes, bytearray, range]
print(l2)

 # output [<class 'int'>, <class 'float'>, <class 'complex'>, <class 'bool'>, <class 'str'>, <class 'list'>, <class 'tuple'>, <class 'set'>, <class 'frozenset'>, <class 'dict'>, <class 'bytes'>, <class 'bytearray'>, <class 'range'>]



l3 = [int(), float(), complex(), bool(), str(), list(), tuple(), set(), frozenset(), dict(), bytes(), bytearray(), range(0)]
print(l3)
 # output [0, 0.0, 0j, False, '', [], (), set(), frozenset(), {}, b'', bytearray(b''), range(0, 0)]


l4 = [10, 20, 30, 40, 10, 20, 30, 40, 50, 11, 34, 65]
print(len(l4))
 # output 12