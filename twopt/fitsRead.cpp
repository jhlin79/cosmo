#include <fstream>
#include "galaxyCatalog.h"
#include <iostream>
using namespace std;

int main(int argc, char * argv[])
{
        //You can select catalog data here.
        char expr[] = "Z > 0.43 && Z < 0.7";
        ofstream fout;
        fout.open(argv[2]);
        galaxyCatalog cmass(argv[1], expr);
        fout.precision(8);
        cmass.save(fout);
        //If you only want to save 10 galaxy data, try:
        //cmass.save(fout, 10);
        fout.flush();
        fout.close();

        return 0;
}
