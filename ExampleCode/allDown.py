#!/usr/bin/env python

'''allDown.py

Code to shut down all cards

Run by typing on the main processor -

mpirun.openmpi -np 8 -machinefile /home/pi/mpi_testing/machinefile python /ClusterShare/allDown.py

Where -np 8 = Run on 8 processors
machinefile contains a list of the IP addresses of the cards

============
Dependencies
============

Need to: 

* sudo apt-get install python-dev
* sudo apt-get install python-pip python2.7-dev
* sudo apt-get install python-rpi.gpio
* sudo pip install flask

====
Code
====
'''

import RPi.GPIO as GPIO
import os
import time
from mpi4py import MPI

comm = MPI.COMM_WORLD
myRank = comm.rank
mySize = comm.size

def setLED(ledState):
	'''Function to blink an LED attached to an output channel.
	Blink time is a function of the processor rank.
	'''
	GPIO.output(25, ledState)

GPIO.setwarnings(False)	# remove warnings about pre-assigned channels
GPIO.setmode(GPIO.BCM)	# setup GPIO using Board numbering
GPIO.setup(25, GPIO.OUT)# Set pin to output

data = 1
while True:
	if myRank == 0:
		comm.send(0, dest=data)
		print 'Shutdown board',data
		time.sleep(0.5)
		data += 1
		if data == mySize:
			os.system('sudo halt')
	else:
		data = comm.recv(source=0)
		os.system('sudo halt')

