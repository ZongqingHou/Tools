/* nms.i */
%module nms
%{
#include "nms.hpp"
%}

nc::NdArray<unsigned int> nMs(float nms_confidence, nc::NdArray<float> detections);

