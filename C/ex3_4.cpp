#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    string word;
    vector<string> words;
//    vector<int> wlenths;
    vector<std::basic_string<char>::size_type> wlenths;
    while(cin >> word) {
        for (int i = 0; i < word.size(); i++) {
            if (word[i] == '.') {
                word.erase(word.find('.'));
            }
            if (word[i] == ',') {
                word.erase(word.find(','));
            }
            if (word[i] == '!') {
                word.erase(word.find('!'));
            }
            if (word[i] == '\'') {
                word.erase(word.find('\''));
            }
            if (word[i] == '\"') {
                word.erase(word.find('\"'));
            }
        }
        if (!word.empty()) {
            words.push_back(word);
            wlenths.push_back(word.size());
        }
    }
    vector<int> maxi;
    std::basic_string<char>::size_type max = 0;
    vector<int> mini;
    std::basic_string<char>::size_type min = wlenths[0];
    for(int i=0;i<words.size();i++)
    {
        if(max < wlenths[i]) {
            maxi.clear();
            maxi.push_back(i);
            max = wlenths[i];
        }else  if( max == wlenths[i]){
            maxi.push_back(i);
        }
        if(min > wlenths[i]) {
            mini.clear();
            mini.push_back(i);
            min = wlenths[i];
        }else  if( min == wlenths[i]){
            mini.push_back(i);
        }
    }
    cout << "Number of max words: " << maxi.size() << endl;
    cout << "max words : ";
    for(auto maxii : maxi) {
        cout << words[maxii] << " ";
    }
    cout << endl;

    cout << "Number of min words: " << mini.size() << endl;
    cout << "min words : ";
    for(auto minii : mini) {
        cout << words[minii] << " ";
    }
    cout << endl;


    return 0;
}