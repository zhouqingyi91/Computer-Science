# python3
class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []
        self.size = 0

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)
        self.size = n

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def build_heap(self):
        for i in range(self.size - 1 // 2, -1, -1):
            self.siftdown(i)
        print('heap', self._data)

    def heap_sort(self):
        for i in range(self.size - 1):
            self._data[0], self._data[self.size - 1] = self._data[self.size - 1], self._data[0]
            self.size -= 1
            self.siftdown(0)
        print('sorted', self._data)

    def siftdown(self, i):
        maxindex = i
        l = self.leftchild(i)
        if l < self.size and self._data[l] < self._data[maxindex]:
            maxindex = l
        r = self.rightchild(i)
        if r < self.size and self._data[r] < self._data[maxindex]:
            maxindex = r

        if i != maxindex:
            self._data[i], self._data[maxindex] = self._data[maxindex], self._data[i]
            self._swaps.append((i, maxindex))
            self.siftdown(maxindex)

    def leftchild(self, i):
        return 2 * i + 1

    def rightchild(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def Solve(self):
        self.ReadData()
        self.build_heap()
        self.WriteResponse()
        self.heap_sort()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
