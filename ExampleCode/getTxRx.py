from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
name = MPI.Get_processor_name()

shared = (rank+1)*5

if rank == 0:
	data = shared
	comm.send(data, dest=1)
	print 'from node:',name,'we sent',data

elif rank == 1:
	data = comm.recv(source=0)
	print 'on node:',name,'we received data',data
	