# Uses python3
import sys
from operator import attrgetter
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_pts(segments):
    pts = []
    segments = sorted(segments, key=attrgetter('end'))
    mr = segments[0].end
    pts.append(mr)
    i = 1
    while i < len(segments):
        if mr < segments[i].start:
            mr = segments[i].end
            pts.append(mr)
        i += 1

    return pts


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    pts = optimal_pts(segments)
    print(len(pts))
    for p in pts:
        print(p, end=' ')