# ifndef NMS_HPP
# define NMS_HPP

# include "NumCpp.hpp"
#include <iostream>

nc::NdArray<unsigned int> nms(float nms_confidence, nc::NdArray<float> detections);

# endif
