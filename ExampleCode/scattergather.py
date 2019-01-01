# Based on https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html
# Also https://mpi4py.readthedocs.io/en/stable/tutorial.html

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
   data = [(x+1)**x for x in range(size)]
   print 'we will be scattering:',data
else:
   data = None
   
data = comm.scatter(data, root=0)

data = [[rank,10],[rank,11],[rank,12],[rank,13]]
newData = comm.gather(data,root=0)
if rank == 0:
   print 'master:'
   for processor in newData:
	print processor
