from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
name = MPI.Get_processor_name()

shared = range(10)

if rank == 0:
	data = shared
	comm.send(data, dest=1)
	print 'Node:',name,', sent:',data

elif rank == 1:
	data = comm.recv(source=0)
	print 'Node:',name,'Received data',data
	print 'Max:',max(data)
	