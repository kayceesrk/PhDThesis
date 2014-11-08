import subprocess
import shlex
import re
from optparse import OptionParser
import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter, MultipleLocator
import sys
import os
import fnmatch
import locale

nodeKind = ['o-', 's--', 'D-.', '^:', 'X-', 'V--', '>-.', '<:']

matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['pdf.fonttype'] = 42

def main ():
	files = ["LWW-txn-lat.dat","LWW-txn-tp.dat"]
	for f in files:
		Cassandra = []
		EC = []
		CC = []
		SC = []

		infile = open (f, "r")
		for line in infile.readlines ():
			if line == "\n" or line.startswith ("#"):
				continue

			d = line.split ()
			Cassandra.append ((float(d[0]),float (d[1])))
			EC.append ((float(d[0]),float (d[2])))
			CC.append ((float(d[0]),float (d[3])))
			SC.append ((float(d[0]),float (d[4])))

		(cx,cy) = zip(*Cassandra)
		(ecx,ecy) = zip(*EC)
		(ccx,ccy) = zip(*CC)
		(scx,scy) = zip(*SC)


		plt.xlabel ("Clients")
		xmajorLocator = MultipleLocator(128)
		plt.axes().xaxis.set_major_locator (xmajorLocator)
		if (f=="BA-lat.dat"):
			plt.ylabel ("Latency (ms)")
			ymajorLocator = MultipleLocator(40)
			plt.axes().yaxis.set_major_locator (ymajorLocator)
		else:
			plt.ylabel ("Throughput (X1000 ops/s)")
		plt.grid (True)
		font = {'family' : 'normal', 'weight' : 'normal', 'size' : 20}
		matplotlib.rc('font', **font)

		plt.subplots_adjust (bottom=0.12)
		plt.plot (cx, cy, nodeKind [0], label="NoTxn", linewidth=2.0, ms=15)
		plt.plot (ecx, ecy, nodeKind [1], label="RC", linewidth=2.0, ms=15)
		plt.plot (ccx, ccy, nodeKind [2], label="MAV", linewidth=2.0, ms=15)
		plt.plot (scx, scy, nodeKind [3], label="RR", linewidth=2.0, ms=15)

		plt.xlim(xmin = 0)
		if (f=="BA-lat.dat"):
			plt.legend(loc=2,ncol=2)
		else:
			plt.legend(loc=2, framealpha=0.5)
		print ("saving fig " + f.replace("dat","pdf"))
		plt.savefig (f.replace("dat","pdf"))
		plt.close ()

main ()
