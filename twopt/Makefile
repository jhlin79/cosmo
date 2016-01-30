fitsRead: fitsRead.cpp table.o
	g++ -I/usr/common/usg/cfitsio/3.31/gnu/include table.o $< -o $@ -L/usr/common/usg/cfitsio/3.31/gnu/lib -lcfitsio

table.o: table.cpp
	g++ -I/usr/common/usg/cfitsio/3.31/gnu/include -c $< -L/usr/common/usg/cfitsio/3.31/gnu/lib -lcfitsio