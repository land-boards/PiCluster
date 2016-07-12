#!/usr/bin/env python

'''cylonLED.py

Code to blink LED on the RPI-PWR card.

Run by typing on the main processor -

mpirun.openmpi -np 8 -machinefile /home/pi/mpi_testing/machinefile python cylonLED.py

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

# Blink the LEDs one at a time forever
# CTRL-C to exit which is not a particularly elegant exit strategy, but this is a demo program
# CTRL-C stops all of the nodes in the cluster

def cycleLED():
	setLED(1)
	time.sleep(0.25)
	setLED(0)
	time.sleep(0.25)
	
data = 0
direction = True
while True:
	if myRank == 0:
		data = comm.bcast(data, root=0)
	if data == myRank:
		cycleLED()
		print 'cycled LED on board:',data

	if direction:
		data += 1
		if data == mySize:
			data = 6
			direction = False
	else:
		data -= 1
		if data == -1:
			data = 2
			direction = True
	time.sleep(1.0)
