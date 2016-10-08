LIB:=${WCC_LIBRARY_PATH}/cpp/lib
ICL:=${WCC_LIBRARY_PATH}/cpp/include

a.out: 0000.cpp
	g++ -std=gnu++11 -Wall -L$(LIB) -Wl,-rpath=$(LIB) -I$(ICL)  0000.cpp

.PHONY: clean run asb 0 create 

create:
	mv ${WCC_SCRIPTS_PATH}/template/template.lang 0000.cpp

asb:
	source-assembler cpp 0000.cpp	

run:
	make && ./a.out

clean:
	rm a.out

0:
	g++ -std=gnu++11 0000.cpp



