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

This file contains definitions of multiple Abstract Information Stuctures.
"""

# Range Maximum Query
class SegmentTree(object):
    def __init__(self, length):
        self.st = [0]*(4*length-1)

    def updateSegmentTree(self, idx, diff, lower, upper, lo, hi):
        if lower > hi or upper < lo:
            return
        if lo >= hi:
            self.st[idx] = max(diff, self.st[idx])
            return
        mid = lo + (hi-lo)//2
        self.updateSegmentTree(2*idx, diff, lower, upper, lo, mid)
        self.updateSegmentTree(2*idx+1, diff, lower, upper, mid+1, hi)
        self.st[idx] = max(self.st[2*idx], self.st[2*idx+1])
        return
    
    def RMQSegmentTree(self, idx, lower, upper, lo, hi):
        if lower <= lo <= hi <= upper:
            return self.st[idx]
        if upper < lo or lower > hi:
            return 0
        mid = lo + (hi-lo)//2
        return max(self.RMQSegmentTree(idx*2, lower, upper, lo, mid), self.RMQSegmentTree(idx*2+1, lower, upper, mid+1, hi))

# Range and Dynamic Sum Query 
class Fenwick:
    def __init__(self, n):
        self.ft = [0 for _ in range(n+1)]

    def update(self, val, idx):
        idx += 1
        while idx < len(self.ft):
            self.ft[idx] += val
            idx += idx & -idx

    def sum(self, idx):
        res = 0
        while idx > 0:
            res += self.ft[idx]
            idx -= idx & -idx
        return res

# Prefix Search
class TrieNode:
    def __init__(self):
        self.next = {}
