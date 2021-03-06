#!/usr/bin/env python

'''copyNetworkShareCodeToLocalFolder.py

Code to copy code from network share folder into a local folder

Run by typing on the main processor -

mpirun.openmpi -np 7 -machinefile /home/pi/mpi_testing/machinefile python copyNetworkShareCodeToLocalFolder.py

Where -np 7 = Run on 7 processors
machinefile contains a list of the IP addresses of the cards

============
Dependencies
============

====
Code
====
'''

import os
from mpi4py import MPI

comm = MPI.COMM_WORLD
myRank = comm.rank
mySize = comm.size

for data in xrange(mySize):
	if myRank == 0:
		comm.send(0, dest=data)
else:
	data = comm.recv(source=0)
	print 'node',myRank
	os.system('sudo cp /ClusterShare/Pt2-AoC-Day11_PiCluster.py ~/ClusterLocal/')
