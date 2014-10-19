import numpy
import pkg_resources
pkg_resources.require("matplotlib")

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter

nodeKind = ['o-', 's--', 'D-.', 'x:', '^-', 'V--', '>-.', '<:']

matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['pdf.fonttype'] = 42

def main ():
	f = "oltp_time.dat"
	CRex = []
	CML = []
	err1 = []
	err2 = []
	infile = open (f, "r")
	for line in infile.readlines ():
		if line == "\n" or line.startswith ("#"):
			continue

		d = line.split ()
		CML.append ((int(d[0]), float(d[1])))
		err1.append (float(d[2]))
		CRex.append ((int(d[0]), float(d[3])))
		err2.append (float(d[4]))

	(rx,ry) = zip(*CRex)
	(mx,my) = zip(*CML)

	plt.xlabel ("# Clients")
	plt.yscale ('log',basey=2)
	plt.ylabel ("Time (Secs)")
	plt.subplots_adjust(bottom=0.15)
	plt.subplots_adjust(left=0.15)
	plt.ylim (10,1400)
	plt.grid (True)
	font = {'weight' : 'normal', 'size' : 20}
	matplotlib.rc('font', **font)

	ax = plt.axes ()
	ax.errorbar (rx, ry, fmt=nodeKind [0], yerr = err2, label="Rx", linewidth=2.0, ms=10)
	ax.errorbar (mx, my, fmt=nodeKind [1], yerr = err1, label="Sync", linewidth=2.0, ms=10)

	plt.legend (loc = 1)
	plt.savefig (f.replace("dat","pdf"))
	plt.close ()

main ()
