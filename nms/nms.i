/* nms.i */
%module nms
%{
#include "NumCpp.hpp"
#include <iostream>
%}

nc::NdArray<unsigned int> nms(float nms_confidence, nc::NdArray<float> detections);
