from optparse import OptionParser
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['pdf.fonttype'] = 42

def main ():
	B = []
	AMD = []
	Error = []

	ind = np.arange (8)
	width = 0.25

	f = "RB_overhead.dat"
	infile = open (f, "r")
	for line in infile.readlines ():
		if line == "\n" or line.startswith ("#"):
			continue

		d = line.split ()
		B.append (d[0])
		AMD.append (float(d[1]))
		Error.append (float(d[2]))

	ax = plt.axes ()
	ax.yaxis.grid ()

	amd_rects = ax.bar (ind + 0.3, AMD,  width, yerr=Error, color="#3399CC", ecolor='black', error_kw=dict(capthick=2))

	ax.set_ylabel ("Overhead (%)")
	ax.set_xticklabels (B, rotation="45")
	ax.set_xticks(ind + 0.3)

	plt.subplots_adjust (bottom=0.2)
	plt.show ()
	#plt.savefig (f.replace("dat","eps"))
	plt.close ()

main ()
