from mpi4py import MPI

comm = MPI.COMM_WORLD

print 'Hi my rank is:', comm.rank
