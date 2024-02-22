#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    string word;
    vector<string> words;
    vector<string> swords;
    vector<int> wcounts;
    int cnt=0;
    while(cin >> word){
        for(int i=0;i<word.size();i++) {
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
        words.push_back(word);
    }
    sort(words.begin(), words.end());
    for(int i=0;i<words.size();i++){
        if( words[i] == words[i+1]){
            ++cnt;
        }else {
            swords.push_back(words[i]);
            wcounts.push_back(cnt+1);
            cnt = 0;
        }
    }
    cout << "size of swords : " << swords.size() << endl;
    cout << "size of wcounts : " << wcounts.size() << endl;
    for(int i=0;i<swords.size();i++){
        cout << swords[i] << " : " << wcounts[i] << endl;
    }

    return 0;
}