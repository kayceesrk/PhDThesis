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
	files = ["BA-tp-vs-lat.dat"]
	for f in files:
		EC = []
		CC = []
		SC = []
		Q = []

		infile = open (f, "r")
		for line in infile.readlines ():
			if line == "\n" or line.startswith ("#"):
				continue
			d = line.split ()
			EC.append ((float(d[0]),float (d[1])))
			CC.append ((float(d[2]),float (d[3])))
			SC.append ((float(d[4]),float (d[5])))
			Q.append ((float(d[6]),float (d[7])))

		(ecx,ecy) = zip(*EC)
		(ccx,ccy) = zip(*CC)
		(scx,scy) = zip(*SC)
		(qx,qy) = zip(*Q)


		plt.xlabel ("Throughput (X 1000 ops/s)")
		plt.ylabel ("Latency (ms)")
		plt.grid (True)
		font = {'family' : 'normal', 'weight' : 'normal', 'size' : 20}
		matplotlib.rc('font', **font)

		plt.subplots_adjust (bottom=0.12)
		plt.plot (ecx, ecy, nodeKind [0], label="EC", linewidth=2.0, ms=15)
		plt.plot (ccx, ccy, nodeKind [1], label="CC", linewidth=2.0, ms=15)
		plt.plot (scx, scy, nodeKind [2], label="SC", linewidth=2.0, ms=15)
		plt.plot (qx, qy, nodeKind [3], label="Q", linewidth=2.0, ms=15)

		plt.xlim(xmin = 0)
		plt.legend (framealpha=0.5)
		print ("saving fig " + f.replace("dat","pdf"))
		plt.savefig (f.replace("dat","pdf"))
		plt.close ()

main ()
