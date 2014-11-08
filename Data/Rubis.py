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

nodeKind = ['o-', 's--', 'D-.', '^:', 'X-', 'V--', '>-.', '<:']

matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['pdf.fonttype'] = 42

def main ():
	files = ["Rubis.dat"]
	for f in files:
		Q = []
		NoRep = []
		StrRep = []

		infile = open (f, "r")
		for line in infile.readlines ():
			if line == "\n" or line.startswith ("#"):
				continue
			d = line.split ()
			Q.append ((float(d[0]),float (d[1])))
			NoRep.append ((float(d[2]),float (d[3])))
			StrRep.append ((float(d[4]),float (d[5])))

		(qx,qy) = zip(*Q)
		(nrx,nry) = zip(*NoRep)
		(strx,stry) = zip(*StrRep)


		plt.xlabel ("Throughput (X 1000 ops/s)")
		plt.ylabel ("Latency (ms)")
		plt.grid (True)
		font = {'family' : 'normal', 'weight' : 'normal', 'size' : 20}
		matplotlib.rc('font', **font)

		plt.subplots_adjust (bottom=0.12)
		plt.plot (qx, qy, nodeKind [0], label="Quelea", linewidth=2.0, ms=15)
		plt.plot (nrx, nry, nodeKind [1], label="NoRep", linewidth=2.0, ms=15)
		plt.plot (strx, stry, nodeKind [2], label="StrongRep", linewidth=2.0, ms=15)

		plt.xlim(xmin = 0)
		plt.legend ()
		print ("saving fig " + f.replace("dat","pdf"))
		plt.savefig (f.replace("dat","pdf"))
		plt.close ()

main ()
