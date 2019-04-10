# -*- encoding: utf-8 -*-

from random import shuffle

aaa = list(range(20))

print(aaa)
shuffle(aaa)


values = ','.join(str(v) for v in aaa)


print(values)

