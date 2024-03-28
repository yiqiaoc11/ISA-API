from abstract_info_struct import *

def getSkyline(buildings):
    events = []
    for b, e, _ in buildings:
	events.append(b)
	events.append(e)
    events.sort()
    events.append(events[-1]+1)

    Tree = SegmentTree(events[-1])
    lo, hi = 0, events[-1]

    res = []
    for p, q, h in buildings:
	Tree.updateSegmentTree(1, h, p, q-1, lo, hi)
	
    for i in range(1, len(events)):
	if events[i] != events[i-1]:
	    height = Tree.RMQSegmentTree(1, events[i-1], events[i]-1, lo, hi)
	    res.append([events[i-1], height])
    return res
