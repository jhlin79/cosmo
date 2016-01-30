#include "table.h"
#include "array.h"
#include <fstream>

class galaxyCatalog {
  table *tptr;
  int n;
  array<float> ra, dec, red, w, x, y, z;
  float para[5]; //These are fitting paramters for the comovig distance.
  para[0] = 0.55109459;
  para[1] = 0.04424543;
  para[2] = 0.99033654;
  para[3] = 1.26811119;
  para[4] = 2.27075546;


 public:
  galaxyCatalog(table *, char *);
  void red2Comoving(void);
  void ang2Car(void);
  int save(fstream *);
  
};
