all:
	pdflatex thesis

force:
	pdflatex thesis
	pdflatex thesis
	bibtex thesis
	bibtex thesis
	pdflatex thesis
	bibtex thesis
	pdflatex thesis

clean:
	rm -f *.log *.bbl *.out *.aux *.toc thesis.blg thesis.lof thesis.lot
