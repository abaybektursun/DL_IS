#include <stdio.h>
#include <opencv2/opencv.hpp>

using namespace cv;

Mat resize_pad(Mat image);

int main(int argc, char** argv )
{
    if ( argc != 2 )
    {
        printf("usage: DisplayImage.out <Image_Path>\n");
        return -1;
    }

    Mat image;
    image = imread( argv[1], 1 );

    if ( !image.data )
    {
        printf("No image data \n");
        return -1;
    }


    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", resize_pad(image));
    //imshow("Display Image", image);

    waitKey(0);

    return 0;
}

Mat resize_pad(Mat image)
{
    int boxSide = 256;
    Size norm_size(boxSide,boxSide);
    int new_rows, new_cols;
    int top, bottom, left, right;

    if (image.rows > image.cols)
    {
        new_rows = boxSide;
        float CoR = (float)image.cols/(float)image.rows;
        new_cols = std::floor(CoR * new_rows);
        top = 0; bottom = 0;
        left = (256 - new_cols)/2;
        right = (256 - new_cols) - left;
    }
    else if(image.rows < image.cols)
    {
        new_cols = boxSide;
        float RoC = (float)image.rows/(float)image.cols;
        new_rows = std::floor(RoC * (float)new_cols);
        left = 0; right = 0;
        top = (256 - new_rows)/2;
        bottom = (256 - new_rows) - top;
    }

    Size new_size(new_cols,new_rows);
    
    Mat resized;
    resize(image,resized,new_size);
    std::cout << "Original: " << image.rows << " by " << image.cols << std::endl;
    std::cout << "Resized: "  << new_rows << " by " << new_cols << std::endl;

    Mat padded(boxSide, boxSide, CV_8UC3);
    copyMakeBorder(resized, padded, top, bottom, left, right, BORDER_CONSTANT);

    std::cout << left << ", " << right << ", " << top << ", " << bottom << std::endl;
    std::cout << "Padded: "  << padded.rows << " by " << padded.cols << std::endl;


    return padded;
}

