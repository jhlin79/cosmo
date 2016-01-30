#include "table.h"
#include "array.h"

class galaxyCatalog {
  table *tptr;
  int n;
  array<float> ra, dec, red, w, x, y, z;
  char zChar[]="Z", wChar[]="WEIGHT_FKP", raChar[]="RA", decChar[]="DEC";

  galaxyCatalog(table *, char *);
  void red2Comoving(void);
  void ang2Car(void);
  int save(char *);
  
};
