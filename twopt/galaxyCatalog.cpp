#include "galaxyCatalog.h"

galaxyCatalog::galaxyCatalog(table *tptrIn, char expr[] = "Z>0.43 || Z<0.7"){
  tptr = tpreIn;
  tptr->select_rows(expr)
    n = tptr->get_num_rows();
  
  ra(n);
  dec(n);
  red(n);
  w(n);
  x(n);
  y(n);
  z(n);

  tptr->read(raChar,  ra.container, 1, n);
  tptr->read(decChar, dec.container, 1, n);
  tptr->read(zChar, z.container, 1, n);
  tptr->read(wChar, w.container, 1, n);
}
