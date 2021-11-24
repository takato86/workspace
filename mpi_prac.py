from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    # ブロッキング通信
    # comm.send(data, dest=1, tag=11)
    # ノンブロッキング通信
    print(rank, data)
    req = comm.isend(data, dast=1, tag=11)
    print("hoge")
    req.wait()

elif rank == 1:
    # ブロッキング通信
    # data = comm.recv(source=0, tag=11)
    # ノンブロッキング通信
    req = comm.irecv(source=0, tag=11)
    data = req.wait()
    print(rank, data)
