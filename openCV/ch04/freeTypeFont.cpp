#include <opencv2/opencv.hpp>
#include <opencv2/freetype.hpp>
#include <iostream>

void rapperFreeTypeCenter(cv::Mat& image, cv::String fontPath, int fontHeight, int thickness, int line_type, cv::Scalar color, cv::String text, cv::Point textOrg)
{
    // FreeType2 객체 생성 (스마트 포인터 사용)
    cv::Ptr<cv::freetype::FreeType2> ft2 = cv::freetype::createFreeType2();

    // 글꼴 파일 로드
    ft2->loadFontData(fontPath, 0);
    cv::Size textSize = ft2->getTextSize(text, fontHeight, -1, 0);

    // 텍스트 그리기
    cv::Point org((textOrg.x - textSize.width) / 2, (textOrg.y + textSize.height) / 2);
    ft2->putText(image, text, org, fontHeight, color, thickness, line_type, true);
}


int main() {
    // 이미지 생성
    cv::Mat image(300, 600, CV_8UC3, cv::Scalar(255, 255, 255));

    // 텍스트 설정
    std::string text = u8"안녕하세요, UTF-8 텍스트입니다.";

    rapperFreeTypeCenter(image, "/home/aa/NanumFont/NanumPen.ttf", 50, -1, cv::LINE_AA, cv::Scalar(0, 0, 0), text, cv::Point(600, 300));
    // 이미지 표시
    cv::imshow("Image with Text", image);
    cv::waitKey(0);

    return 0;
}