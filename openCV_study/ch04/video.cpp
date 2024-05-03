#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
  Mat frame, doubleFrame, reshapedFrame;
  VideoCapture cap(folder + "vtest.avi");
  if (!cap.isOpened()) {
    cerr << "Video open failed.\n";
    return -1;
  }
  cout << "Frame width: " << cap.get(CAP_PROP_FRAME_WIDTH) << endl;
  cout << "Frame height: " << cap.get(CAP_PROP_FRAME_HEIGHT) << endl;
  Size sz1(cap.get(CAP_PROP_FRAME_WIDTH), cap.get(CAP_PROP_FRAME_HEIGHT));
  std::vector<int> shape = {sz1.width / 2, sz1.height * 2};
  double fps = cap.get(CAP_PROP_FPS);
  int fourcc = VideoWriter::fourcc('D', 'I', 'V', 'X');
  int delay = cvRound(1000 / fps);

  VideoWriter outputVideo(folder + "output1.avi", fourcc, fps, sz1 * 2);
  while (true) {
    cap >> frame;
    resize(frame, doubleFrame, sz1 * 2);
    reshapedFrame = frame.reshape(3, shape);
    imshow("frame", frame);
    imshow("doubleFrame", doubleFrame);
    outputVideo << doubleFrame;
    imshow("reshapedFrame", reshapedFrame);
    if (waitKey(delay) == 27)
      break;
  }
  destroyAllWindows();
  return 0;
}