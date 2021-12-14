import os
from multiprocessing import Process, Value, Array, Queue


N_PROCESSES = 4


def f(n, i, a, q):
    n.value += float(i)
    a[i] = 3.14 + float(i)
    q.put(i)
    print(i, os.getpid())


if __name__ == "__main__":
    # 共有メモリ
    v = Value('d', 0.0)
    arr = Array('d', range(N_PROCESSES))
    q = Queue()
    ps = []

    for i in range(N_PROCESSES):
        p = Process(target=f, args=(v, i, arr, q))
        ps.append(p)
        p.start()

    [pi.join() for pi in ps]
    # print(v.value, arr.array)
    for _ in range(q.qsize()):
        print(q.get())
