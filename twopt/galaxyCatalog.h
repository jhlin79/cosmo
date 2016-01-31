#include "table.h"
#include <fstream>

class galaxyCatalog {
  table * tptr;
  int n;
  float ra[10], dec[10], red[10], w[10], x[10], y[10], z[10];
  float DH, para[5]; //These are fitting paramters for the comovig distance.
  char redChar[20], wChar[20], raChar[20], decChar[20];

 public:
  galaxyCatalog(char *, char *);
  void read(const int&);
  void red2Comoving();
  void ang2Car();
  void save(std::ofstream &);
  ~galaxyCatalog();
};
