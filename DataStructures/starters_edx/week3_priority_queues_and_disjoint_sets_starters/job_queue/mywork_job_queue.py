# implement priority heap to job queue


class job_heap():
    # def read_data(self):
    #     self.num_workers, m = map(int, input().split())
    #     self.jobs = list(map(int, input().split()))
    #     assert m == len(self.jobs)

    def data(self, n, array):
        self.num_workers = n
        self.jobs = array

    def write_response(self):
        for work in self.assigned_workers_and_starttime:
            print(work[1], work[0])

    def load_worker_to_heap(self):
        self.heap = []
        for worker in range(self.num_workers):
            self.heap.append([0, worker])

    def assign_jobs(self):
        self.assigned_workers = []
        self.start_times = []
        for i in range(len(self.jobs)):
            new_worker = self.heap[0]
            self.assigned_workers.append(new_worker[1])
            self.start_times.append(new_worker[0])
            self.change_priority(0, self.jobs[i] + new_worker[0])
        return self.assigned_workers, self.start_times

    def change_priority(self, i, pri):
        oldp = self.heap[i][0]
        self.heap[i][0] = pri
        if pri > oldp:
            self.siftdown(i)  # in this case it will always siftdown
        else:                 # because pri is always > oldp
            self.siftup(i)

    def siftup(self, i):
        p = self.parent(i)
        while i > 0 and self.heap[p][0] > self.heap[i][0]:
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p
            p = self.parent(i)

    def siftdown(self, i):
        index = i
        left = self.lchild(i)
        if left < self.num_workers and self.heap[left][0] < self.heap[index][0]:
            index = left

        right = self.rchild(i)
        if right < self.num_workers and self.heap[right][0] < self.heap[index][0]:
            index = right

        if left < self.num_workers and self.heap[left][0] == self.heap[index][0]:
            if self.heap[left][1] < self.heap[index][1]:
                index = left

        if right < self.num_workers and self.heap[right][0] == self.heap[index][0]:
            if self.heap[right][1] < self.heap[index][1]:
                index = right

        if i != index:
            self.heap[i], self.heap[index] = self.heap[index], self.heap[i]
            self.siftdown(index)

    def parent(self, i):
        return (i - 1) // 2

    def lchild(self, i):
        return i * 2 + 1

    def rchild(self, i):
        return i * 2 + 2

    def solve(self):
        # self.read_data()
        self.load_worker_to_heap()
        worker, time = self.assign_jobs()
        return worker, time
        # self.write_response()


# if __name__ == '__main__':
#     job_queue = job_heap()
#     job_queue.solve()
