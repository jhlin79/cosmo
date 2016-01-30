#include <string.h>
#include <stdio.h>
#include "fitsio.h"
#include "table.h"
#include <fstream>
using namespace std;

int main(int argc, char *argv[])
{
  ofstream fout;
  table galTable(argv[1]);
  float z[10];
  char zChar[]="Z";
  int id;

  fout.open("test.txt");
  id = galTable.get_colnum(zChar);
  galTable.read(zChar, z, 1, 10);

  fout << z[1] << " " << z[2] << " " << z[3];
  fout.close();
  galTable.close();

  if (galTable.stat())
    fits_report_error(stderr, galTable.stat());
  return(galTable.stat());
}
