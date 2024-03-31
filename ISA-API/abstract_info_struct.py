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

class TrieNode:
    def __init__(self, data):
        self.next = {}
