# Python files do not need to be compiled. They are interpreted by the Python interpreter. Therefore, the makefile does not contain any compilation rules.

.PHONY: all doc clean

PROJECT=IVS2_Ackostaci
AUTHORS= xdubro01_xsamoi00_xvolk02_xarltt00

run:
    python calculator_logic.py

doc: Doxyfile
	doxygen $<

profiling: 
	python profiling.py

clean:
	rm -rf doc
    rm *.pyc