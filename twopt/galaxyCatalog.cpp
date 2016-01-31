#include "galaxyCatalog.h"
#include <math.h>
#include <string.h>
#define PI 3.14159265

galaxyCatalog::galaxyCatalog(char *fn, char *expr){
  //These parameters are for Om=0.274.
  para[0] = 0.55109459;
  para[1] = 0.04424543;
  para[2] = 0.99033654;
  para[3] = 1.26811119;
  para[4] = 2.27075546;
  DH = 3000./0.7;

  strcpy(redChar, "Z");
  strcpy(wChar, "WEIGHT_FKP");
  strcpy(raChar, "RA");
  strcpy(decChar, "DEC");

  tptr = new table (fn);
  tptr->select_rows(expr);
  n = tptr->get_num_rows();
}

void galaxyCatalog::read(const int& i){
  //dn < 100
  tptr->read(raChar,  ra, i, 1);
  tptr->read(decChar, dec, i, 1);
  tptr->read(redChar, red, i, 1);
  tptr->read(wChar, w, i, 1);

}


/*   In function ang2Car, red should be
     transformed into comoving distance first!!  */


void galaxyCatalog::ang2Car(){
  float sinDec, cosDec, sinRa, cosRa;
    sinDec = sin(dec[0]*PI/180.0);
    cosDec = cos(dec[0]*PI/180.0);
    sinRa  = sin( ra[0]*PI/180.0);
    cosRa  = cos( ra[0]*PI/180.0);
    z[0] = red[0] * sinDec;
    x[0] = red[0] * cosDec * cosRa;
    y[0] = red[0] * cosDec * sinRa;
 }
 
void galaxyCatalog::red2Comoving(){
  float zi;
  zi = red[0];
  red[0] = DH * para[2]*zi /sqrt( 1.0 + para[0]*pow(zi, para[3]) + para[1]*pow(zi, para[4]) );
  
}

void galaxyCatalog::save(std::ofstream &fout){
  for (int row=1; row<n+1; row++){
    read(row);
    red2Comoving();
    ang2Car();
    fout << x[0] << " " << y[0] << " " << z[0] << " " << w[0] << std::endl;
  }
}

galaxyCatalog::~galaxyCatalog(){
  delete[] tptr;
}
