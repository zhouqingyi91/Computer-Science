# python3


class JobQueue():
    # def read_data(self):
    #     self.num_workers, m = map(int, input().split())
    #     self.jobs = list(map(int, input().split()))
    #     assert m == len(self.jobs)

    def data(self, n, array):
        self.num_workers = n
        self.jobs = array

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
            next_worker = 0
            for j in range(self.num_workers):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] += self.jobs[i]
        return self.assigned_workers, self.start_times

    def solve(self):
        # self.read_data()
        worker, time = self.assign_jobs()
        return worker, time
        # self.write_response()


# if __name__ == '__main__':
#     job_queue = JobQueue()
#     job_queue.data(2, [1, 2, 3, 4, 5])
#     job_queue.solve()
