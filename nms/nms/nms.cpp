# include "nms.hpp"
#include <iostream>



nc::NdArray<unsigned int> nMs(float nms_confidence, nc::NdArray<float> detections)
{
    auto x1 = detections(detections.rSlice(), 0);
    auto x2 = detections(detections.rSlice(), 2);
    auto y1 = detections(detections.rSlice(), 1);
    auto y2 = detections(detections.rSlice(), 3);

    auto scores = detections(detections.rSlice(), 4);

    auto area_collection = (x2 - x1 + 1) * (y2 - y1 + 1);
    auto order_ = area_collection.argsort();

    nc::NdArray<float> keep;
    while (order_.size() > 0)
    {
        break;
    }

    std::cout << area_collection << std::endl;

    return order_;
}
