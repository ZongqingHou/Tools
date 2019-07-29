//vector.cpp
#include "vector.hpp"
#include <iostream>
#include <cmath>
using namespace std;

Vector::Vector(int a,int b){  x=a;  y=b;  }
void Vector::display(){  cout << "(" << x << ',' << y << ')' << endl; }
double Vector::abs(){    return sqrt(x*x+y*y);  }