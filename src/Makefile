# Python files do not need to be compiled. They are interpreted by the Python interpreter. Therefore, the makefile does not contain any compilation rules.

.PHONY: doc clean pack all test

PROJECT= IVS2_Ackostaci
AUTHORS= xdubro01_xsamoi00_xvolk02_xarltt00

all:
	pyinstaller --name=calculator.exe --onefile -w main.py
	rm -rf build
	rm -f calculator.exe.spec

run: main.py gui.py calculator_logic.py
	./dist/calculator.exe
	
profile: 
	python profiling.py

test:
	pytest 

help:
	./help.sh
 
 doc: Doxyfile
	doxygen $<
        
pack: clean Doxyfile
	rm -rf $(AUTHORS)
	mkdir ./$(AUTHORS)
	mkdir ./$(AUTHORS)/repo
	cd ../.. && cp -r ./$(PROJECT) $(PROJECT)_c
	mv ../../$(PROJECT)_c ./$(AUTHORS)/repo/$(PROJECT)
	rm -r ./$(AUTHORS)/repo/$(PROJECT)/src/$(AUTHORS)
	doxygen Doxyfile
	cp -r ./doc/ ./$(AUTHORS)
	mkdir ./$(AUTHORS)/install
	cp ../src/dist/calculator.exe ./$(AUTHORS)/install/
	zip -r $(AUTHORS).zip $(AUTHORS)

clean:
	rm -rf doc
	rm *.pyc
        rm -rf $(AUTHORS)
