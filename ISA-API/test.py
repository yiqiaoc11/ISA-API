"""
Copyright 2020, Yiqiao 

This file is part of python-awis.

ISA-API is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Python-awis is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

This file contains test cases and scenario summary of algorithms and data structures.
"""

from ais import *
# a classical Skyline problem solved by Segment Trees
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
