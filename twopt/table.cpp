#include "table.h"

long table::get_num_rows(){
  long nrows;
  fits_get_num_rows(fptr, &nrows, &status);
  return nrows;
}

int table::get_colnum(char *colnm){
  int id;
  fits_get_colnum(fptr, 1, colnm, &id, &status);
  return id;
}


int table::get_coltype(int id){
  int typecode;
  long width, repeat;
  fits_get_coltype(fptr, id, &typecode, &repeat, &width, &status);
  return typecode;
}

void table::read(char *colnm, float *arr, long ii, long len){
  int colnum = get_colnum(colnm), anynul;
  fits_read_col(fptr, 42, colnum, ii, 1, len, NULL, arr, &anynul, &status);
}

