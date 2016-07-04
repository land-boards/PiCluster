from mpi4py import MPI

comm = MPI.COMM_WORLD

print 'Hi my rank is:', comm.rank

if comm.rank == 1:
	print 'doing the task of rank 1'

if comm.rank == 0:
	print 'doing the task of rank 0'

if comm.rank == 2:
	print 'doing the task of rank 2'
	