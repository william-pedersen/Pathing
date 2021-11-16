from io import IOBase, TextIOWrapper
from typing import Union, Optional

import itertools, functools
import timeit

class Pathing(object):
    def __init__(self, data: Union[list, set, tuple, bytearray]) -> None:
        self.data = data

    def maxTotal(self, timing: Optional[bool] = False) -> Union[int, float, tuple]:
        if timing: 
            s = timeit.default_timer()
            res = self.maxTotal(
                timing = False
            )
            e = timeit.default_timer()
            elapsed = (e - s) * 1000
            return (res, elapsed)
            
        return sum(
            functools.reduce(
                lambda l, r: [
                    _l + _r
                    for _l, _r
                    in zip(
                        [
                            max(lv, rv if rv is not None else l)
                            for
                            lv, rv
                            in itertools.zip_longest(
                                l,
                                l[1:],
                                fillvalue = None
                            )
                            if (
                                (lv and rv) is not None or len(l) == 1
                            )
                        ],
                        r
                    )
                ],
                self.data[::-1]
            )
        )

    def minTotal(self, timing: Optional[bool] = False) -> Union[int, float, tuple]:
        if timing: 
            s = timeit.default_timer()
            res = self.minTotal(
                timing = False
            )
            e = timeit.default_timer()
            elapsed = (e - s) * 1000
            return (res, elapsed)
            
        return sum(
            functools.reduce(
                lambda l, r: [
                    _l + _r
                    for _l, _r
                    in zip(
                        [
                            min(lv, rv if rv is not None else l)
                            for
                            lv, rv
                            in itertools.zip_longest(
                                l,
                                l[1:],
                                fillvalue = None
                            )
                            if (
                                (lv and rv) is not None or len(l) == 1
                            )
                        ],
                        r
                    )
                ],
                self.data[::-1]
            )
        )

    @classmethod
    def fromFile(cls, file: Union[str, TextIOWrapper, IOBase]) -> 'Pathing':
        with open(file = file, mode = 'r', encoding = 'UTF-8') as file:
            return cls(
                data = 
                    [
                        [
                            int(num)
                            for num
                            in line.rstrip('\n').split(' ')
                        ]
                        for line
                        in file.readlines()
                    ]
            )




def main():
    pathing = Pathing.fromFile(
        file = 'triangle.txt'
    )
    total, time = pathing.maxTotal(
        timing = True
    )
    """
    Alternatively, 
    total = pathing.maxTotal(
        timing = False
    )
    """
    print(f'Finding value {total} took {time:.2f} ms')

if __name__ == '__main__':
    main()