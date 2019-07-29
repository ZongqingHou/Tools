/* vector.i */
%module vector
%{
#include "vector.hpp"
%}

class Vector{
public:
    Vector(int,int);
    double abs();
    void display();
private:
    int x;
    int y;
};