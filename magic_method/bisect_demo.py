import bisect
import sys


HAYSTACK=[1,4,5,6,8,12,15,20,21,23,26,29,30]
NEEDLES=[0,1,2,5,8,10,22,23,29,30,31]

row_format="{0:2d} @ {1:2d}    {2}{0:<2d}"

def demo(bisect_fun):
    for needle in reversed(NEEDLES):
        position=bisect.bisect(HAYSTACK,needle)
        offset="  |" *position
        print(row_format.format(needle,position,offset))

if __name__=="__main__":
    bisect_fun=bisect.bisect
    print("HAYSTACK->", " ".join("%2d"% n for n in NEEDLES))
    demo(bisect_fun)
