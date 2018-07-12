import mywork_job_queue
import job_queue
import random
import time


heap = mywork_job_queue.job_heap()
queue = job_queue.JobQueue()


# stress test
# for i in range(1000000):
#     n = random.randint(1, 20)
#     num = random.randint(1, 8)
#     array = [None] * n
#     for j in range(n):
#         array[j] = random.randint(1, 100)
#     heap.data(num, array)
#     queue.data(num, array)
#     a, b = heap.solve()
#     x, y = queue.solve()
#     if a != x or b != y:
#         print('a', a)
#         print('x', x)
#         print('b', b)
#         print('y', y)
#         print('=======================')
#         break
#     if i % 10000 == 0:
#         print(num, array)
#         print('so far so good')


# time constraint test
# heap
m = 100000
array = [None] * m
for j in range(m):
    array[j] = random.randint(1, 100000000)

start = time.time()
heap.data(100000, array)
a, b = heap.solve()
end = time.time()
print(end - start)

# queue
# m = 10000
# array = [None] * m
# for j in range(m):
#     array[j] = random.randint(1, 100000000)
#
# start = time.time()
# queue.data(10000, array)
# a, b = queue.solve()
# end = time.time()
# print(end - start)
