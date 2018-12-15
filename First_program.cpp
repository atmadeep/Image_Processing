//
// Created by atmadeep on 18/9/18.
//
#include <opencv2/core.hpp>
#include <iostream>
using namespace std;
using namespace cv;

int main(int argc, char** argv){
    cv::Mat image = cv::imread(argv[1],0);
    if(image.empty()){
        cerr<<"Empty Image";
        return -1;
    }
    namedWindow("Image",cv::WINDOW_AUTOSIZE);
    imshow("Image",image);
    waitKey(0);
    destroyWindow("Image");
}
