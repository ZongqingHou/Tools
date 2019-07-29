# ifndef NMS_HPP
# define NMS_HPP

# include "NumCpp.hpp"

nc::NdArray<unsigned int> nMs(float nms_confidence, nc::NdArray<float> detections);

# endif
