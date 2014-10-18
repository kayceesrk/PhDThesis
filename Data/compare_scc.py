import subprocess
import shlex
import re
from optparse import OptionParser
import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import sys
import os
import fnmatch
import locale

nodeKind = ['o-', 's--', 'D-.', 'x:', '^-', 'V--', '>-.', '<:']

matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['pdf.fonttype'] = 42

def main ():
	files = ["time_scc.dat", "mutator_time_scc.dat", "gc_time_scc.dat"]
	for f in files:
		LC = []
		PRC = []
		SMC = []

		infile = open (f, "r")
		for line in infile.readlines ():
			if line == "\n" or line.startswith ("#"):
				continue

			d = line.split ()
			LC.append ((float(d[0]),float (d[1])))
			PRC.append ((float(d[2]),float (d[3])))
			SMC.append ((float(d[4]),float (d[5])))

		tmp = LC + PRC + SMC
		(x, y) = zip(*tmp)
		minX = min(x)
		if (f == "gc_overhead_scc.dat"):
			minY = 1.0
		else:
			minY = min(y)
		LC = [(x/minX, y/minY) for (x,y) in LC]
		(lcx,lcy) = zip(*LC)
		PRC = [(x/minX, y/minY) for (x,y) in PRC]
		(prcx,prcy) = zip(*PRC)
		SMC = [(x/minX, y/minY) for (x,y) in SMC]
		(smcx,smcy) = zip(*SMC)


		if (f == "time_scc.dat"):
			plt.xlabel ("Heap size relative to min heap size")
			plt.ylabel ("Normalized Time")
			ticker.MaxNLocator (nbins=4)
			plt.grid (True)
			font = {'family' : 'normal', 'weight' : 'normal', 'size' : 20}
			matplotlib.rc('font', **font)
			plt.axes().yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
		elif (f == "mutator_time_scc.dat"):
			plt.xlabel ("Heap size relative to min heap size")
			plt.ylabel ("Normalized Mutator Time")
			plt.grid (True)
			font = {'family' : 'normal', 'weight' : 'normal', 'size' : 20}
			matplotlib.rc('font', **font)
			plt.axes().yaxis.set_major_formatter(FormatStrFormatter('%1.2f'))
		elif (f == "gc_time_scc.dat"):
			plt.xlabel ("Heap size relative to min heap size")
			plt.ylabel ("Normalized GC Time (log)")
			plt.grid (True)
			font = {'family' : 'normal', 'weight' : 'normal', 'size' : 20}
			matplotlib.rc('font', **font)
			plt.axes().set_yscale ("log", basey=2)
			plt.axes().yaxis.set_major_formatter(FormatStrFormatter('%d'))
		else:
			plt.xlabel ("Heap size relative to min heap size")
			plt.ylabel ("GC overhead (%)")
			plt.grid (True)
			font = {'family' : 'normal', 'weight' : 'normal', 'size' : 20}
			matplotlib.rc('font', **font)
			plt.axes().set_yscale ("linear")

		plt.subplots_adjust (bottom=0.12)
		plt.plot (prcx, prcy, nodeKind [0], label="PRC", linewidth=2.0, ms=15)
		plt.plot (lcx, lcy, nodeKind [1], label="LC", linewidth=2.0, ms=15)
		plt.plot (smcx, smcy, nodeKind [2], label="SMC", linewidth=2.0, ms=15)

		plt.xlim(xmin = 0)
		plt.legend ()
		print ("saving fig " + f.replace("dat","pdf"))
		plt.savefig (f.replace("dat","pdf"))
		plt.close ()

main ()
