# Based on https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html
# Also https://mpi4py.readthedocs.io/en/stable/tutorial.html

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = [[rank,10],[rank,11],[rank,12],[rank,13]]
newData = comm.gather(data,root=0)
if rank == 0:
   print 'master:'
   for processor in newData:
	print processor
