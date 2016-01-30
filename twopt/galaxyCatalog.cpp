#include "galaxyCatalog.h"
#include <math.h>
#define PI 3.14159265


galaxyCatalog::galaxyCatalog(table *tptrIn, char *expr){
  tptr = tptrIn;
  tptr->select_rows(expr);
  n = tptr->get_num_rows();
  
  array<float> ra(n), dec(n), red(n), w(n), x(n), y(n), z(n);

  char redChar[]="Z", wChar[]="WEIGHT_FKP", raChar[]="RA", decChar[]="DEC";
  tptr->read(raChar,  ra.container, 1, n);
  tptr->read(decChar, dec.container, 1, n);
  tptr->read(redChar, red.container, 1, n);
  tptr->read(wChar, w.container, 1, n);
}


/*   In function ang2Car, red should be
     transformed into comoving distance first!!  */
void galaxyCatalog::ang2Car(){
  float sinDec, sinRa, cosRa;
  for (int i=0; i<n; i++){
    sinDec = sin(dec[i]*PI/180.0);
    sinRa  = sin( ra[i]*PI/180.0);
    cosRa  = cos( ra[i]*PI/180.0);
    z[i] = red[i] * sinDec;
    x[i] = red[i] * cosDec * cosRa;
    y[i] = red[i] * cosDec * sinRa;
  }
}
 
void galaxyCatalog::red2Comoving(){
  float z;
  for (int i=0; i<n; i++){
    z = red[i];
    red[i] = para[2] * z /
      sqrt( 1.0 + para[0]*pow(z, para[3]) + para[1]*pow(z, para[4]) );
  }
}

void galaxyCatalog::
