#include "fitsio.h"

class table {
  int status;
  fitsfile *fptr;


public:
  table(char *fn) {fits_open_table(&fptr, fn, READWRITE, &status); status=0;}
  long get_num_rows();
  int get_colnum(char *colnm);
  int get_coltype(int id);
  void select_rows(char *expr) {fits_select_rows(fptr, fptr, expr, &status);}
  void close(void) {fits_close_file(fptr, &status);}
  void read(char *colnm, float *arr, long ii, long len); 
  int stat(void) { return status;}
};
