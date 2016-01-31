#include <fstream>
#include "galaxyCatalog.h"
#include <iostream>
using namespace std;

int main(int argc, char * argv[])
{
  char expr[] = "Z > 0.43 && Z < 0.7 && WEIGHT_FKP>0";
  ofstream fout;
  fout.open(argv[2]);
  galaxyCatalog cmass(argv[1], expr);
  fout.precision(8);
  cmass.save(fout);
  fout.flush();
  fout.close();
 
  return 0;
}
