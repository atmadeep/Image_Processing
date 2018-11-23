//
// Created by atmadeep on 20/8/18.
//
#include"opencv2/opencv.hpp"
#include"opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>

using namespace cv;
int main(int argv, char** argc){
    Mat image =cv::imread("image_1.jpg",CV_LOAD_IMAGE_COLOR);
    if ( image.empty() )
   {std::cerr << "Could not open file" << std::endl; return ( -1 );}
    namedWindow("Image",WINDOW_AUTOSIZE);
    imshow("Image",image);
    waitKey(30);
}


