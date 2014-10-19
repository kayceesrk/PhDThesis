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
	f = "collab.dat"
	CRex = []
	CML = []
	err1 = []
	err2 = []
	infile = open (f, "r")
	for line in infile.readlines ():
		if line == "\n" or line.startswith ("#"):
			continue

		d = line.split ()
		CRex.append ((int(d[0]), float(d[1])))
		err1.append (float(d[2]))
		CML.append ((int(d[0]), float(d[3])))
		err2.append (float(d[4]))

	(rx,ry) = zip(*CRex)
	ry = [x/1000 for x in ry]
	(mx,my) = zip(*CML)
	my = [x/1000 for x in my]

	plt.xlabel ("# Authors")
	plt.ylabel ("Time (X 1000 Secs)")
	plt.subplots_adjust(bottom=0.15)
	plt.grid (True)
	font = {'weight' : 'normal', 'size' : 20}
	matplotlib.rc('font', **font)
	plt.xticks ([2,3,4,5,6])
	ax = plt.axes ()
	ax.errorbar (rx, ry, fmt=nodeKind [0], label="Rx", yerr = err1, linewidth=2.0, ms=10)
	ax.errorbar (mx, my, fmt=nodeKind [1], label="Sync", yerr = err2, linewidth=2.0, ms=10)

	plt.legend (loc = 2)
	plt.savefig (f.replace("dat","pdf"))
	plt.close ()

main ()
