from optparse import OptionParser
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['pdf.fonttype'] = 42

def main ():
	B = []
	MU = []
	CL = []
	err1 = []
	err2 = []

	ind = np.arange (8)
	width = 0.35

	f = "slowdown_cleanliness.dat"
	infile = open (f, "r")
	for line in infile.readlines ():
		if line == "\n" or line.startswith ("#"):
			continue

		d = line.split ()
		B.append (d[0])
		MU.append (float(d[1]))
		err1.append (float(d[2]))
		CL.append (float(d[3]))
		err2.append (float(d[2]))

	ax = plt.axes ()
	ax.yaxis.grid ()

	mu_rects = ax.bar (ind+0.1, MU, width, yerr=err1, ecolor='black', color="#3399CC", error_kw=dict(capthick=2))
	cl_rects = ax.bar (ind+width+0.1, CL, width, yerr=err2, ecolor='black', color="#CC6633", hatch="X", error_kw=dict(capthick=2))

	ax.set_ylabel ("Slowdown (%)")
	ax.set_xticks(ind+width)
	ax.set_xticklabels (B, rotation="45")
	ax.legend( (mu_rects[0], cl_rects[0] ), ('PRC MU-', 'PRC CL-') )

	plt.subplots_adjust (bottom=0.2)
	plt.show ()
	#plt.savefig (f.replace("dat","eps"))
	plt.close ()

main ()
