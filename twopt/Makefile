Include=-I/usr/common/usg/cfitsio/3.31/gnu/include
Link=-L/usr/common/usg/cfitsio/3.31/gnu/lib -lcfitsio

fitsRead: fitsRead.cpp table.o
	g++ $(Include) table.o $< -o $@ $(Link)

table.o: table.cpp
	g++ $(Include) -c $< $(Link)

galaxyCatalog.o: galaxyCatalog.cpp
	g++ $(Include) -c $< $(Link)