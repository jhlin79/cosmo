DEBUG=
INCLUDE=-I/usr/common/usg/cfitsio/3.31/gnu/include
LINK=-L/usr/common/usg/cfitsio/3.31/gnu/lib -lcfitsio

fitsRead: fitsRead.cpp table.o galaxyCatalog.o
	g++ $(INCLUDE) table.o  galaxyCatalog.o $< -o $@ $(LINK) $(DEBUG)

table.o: table.cpp table.h
	g++ $(INCLUDE) -c $< $(LINK) $(DEBUG)

galaxyCatalog.o: galaxyCatalog.cpp galaxyCatalog.h table.h
	g++ $(INCLUDE) -c $< $(LINK) $(DEBUG)