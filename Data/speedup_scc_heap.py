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
	LC = []
	PRC = []
	SMC = []

	f = "speedup_scc_heap.dat"
	infile = open (f, "r")
	for line in infile.readlines ():
		if line == "\n" or line.startswith ("#"):
			continue
		d = line.split ()
		LC.append ((float(d[0]), float(d[1])))
		PRC.append ((float(d[0]), float(d[2])))
		SMC.append ((float(d[0]), float(d[3])))
	(lc_x,lc_y) = zip(*LC)
	(prc_x,prc_y) = zip(*PRC)
	(smc_x,smc_y) = zip(*SMC)

	plt.xlabel ("# Cores")
	plt.ylabel ("Speedup")
	plt.grid (True)
	font = {'family' : 'normal', 'weight' : 'normal', 'size' : 20}
	matplotlib.rc('font', **font)

	plt.plot (lc_x, lc_y, nodeKind [0], label="LC", linewidth=2.0, ms=15)
	plt.plot (prc_x, prc_y, nodeKind [1], label="PRC", linewidth=2.0, ms=15)
	plt.plot (smc_x, smc_y, nodeKind [2], label="SMC", linewidth=2.0, ms=15)

	plt.subplots_adjust (bottom=0.12)
	plt.xlim(xmin = 0)
	plt.legend (loc = 2)
	print ("saving fig " + f.replace("dat","pdf"))
	plt.savefig (f.replace("dat","pdf"))
	plt.close ()

main ()
