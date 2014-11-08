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
	files = ["GC.dat"]
	for f in files:
		Cassandra = []
		EC = []
		CC = []

		infile = open (f, "r")
		for line in infile.readlines ():
			if line == "\n" or line.startswith ("#"):
				continue

			d = line.split ()
			if (len(d) == 6):
				Cassandra.append ((float(d[0])/10000,float (d[1])/100))
				EC.append ((float(d[2])/10000,float (d[3])/100))
				CC.append ((float(d[4])/10000,float (d[5])/100))
			elif (len(d) == 4):
				EC.append ((float(d[0])/10000,float (d[1])/100))
				CC.append ((float(d[2])/10000,float (d[3])/100))
			elif (len(d) == 2):
				CC.append ((float(d[0])/10000,float (d[1])/100))


		(cx,cy) = zip(*Cassandra)
		(ecx,ecy) = zip(*EC)
		(ccx,ccy) = zip(*CC)


		plt.xlabel ("Operations (X 10,000)")
		plt.ylabel ("Latency (X 100 ms)")
		plt.grid (True)
		font = {'family' : 'normal', 'weight' : 'normal', 'size' : 20}
		matplotlib.rc('font', **font)

		plt.subplots_adjust (bottom=0.12)
		plt.plot (cx, cy, nodeKind [0], label="No Sum", linewidth=2.0, ms=10)
		plt.plot (ecx, ecy, nodeKind [1], label="Mem Only", linewidth=2.0, ms=10)
		plt.plot (ccx, ccy, nodeKind [2], label="Mem & Disk", linewidth=2.0, ms=10)
		plt.xlim(xmin = 0)
		plt.legend (bbox_to_anchor=(1, 0.75))
		print ("saving fig " + f.replace("dat","pdf"))
		plt.savefig (f.replace("dat","pdf"))
		plt.close ()

main ()
