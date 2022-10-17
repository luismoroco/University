#include <fstream>
#include <set>
#include <utility>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
#include <random>
#include <ctime>

using std::string;
using std::ifstream;
using std::getline;
using std::multiset;
using std::multimap;
using std::set;
using std::pair;
using std::map;
using std::vector;
using std::sort;
using std::cout;

string getDataFromFile(string iName) {
  ifstream iFile(iName);
  string buffer, tmp;

  if (!iFile) 
    return "";

  while(getline(iFile, tmp)) 
    buffer.append(tmp);
  
  iFile.close();

  return buffer;
}

void sustituionsInCharacters(string &text) {
  int i; 
  char c;
  for (i = 0; i < text.length(); ++i) {
    c = text[i];
    if (c >= 65 && c <= 90) 
      c += 32;

    switch (c) {
      case 'j' || 'h': text[i] = 'i'; break;
      case 'u': text[i] = 'v'; break;
      case 'w': text[i] = 'v'; break;
      case 'k': text[i] = 'l'; break;
      case 'y': text[i] = 'z'; break;
      case 'x': text[i] = 'r'; break;
      case -61: 
        if (text[i+1]  == -79) {
          text[i] = 'n'; 
          text.erase(i+1, 1); 
        }
        break; 
      default: break;
    }
  }
}

void deleteacents(string &text) {
  int i; 
  char c, t; 
  for (i = 0; i < text.length(); ++i) {
    if (text[i] == -61) {
      c = text[i], t = text[i+1];
      switch (t) {
        case -95: text[i] = 'a'; break;
        case -87: text[i] = 'e'; break;
        case -83: text[i] = 'i'; break;
        case -77: text[i] = 'o'; break;
        case -70: text[i] = 'u'; break;
      }
      text.erase(i+1, 1);
    }
  }
}

void arrToUpper(string &text) {
  int i; 
  char c; 
  for (i = 0; i < text.length(); ++i) {
    c = text[i];
    if (c >= 97 && c <= 122) 
      text[i] -= 32;
  }
}

void deleteWhiteSpaceAndPoints(string &text) {
  int i; 
  char c; 
  for (i = 0; i < text.length(); ++i) {
    c = text[i];
    if (c >= 33 && c <= 47 || c >= 58 && c <= 64) 
      text.erase(i, 1);
  }

  for (i = 0; i < text.length(); ++i) {
    if (text[i] == ' ') 
      text.erase(i, 1);
  }

  for (i = 0; i < text.length(); ++i) {
    if (text[i] == -62) 
      text.erase(i, 2);
  }
}

// SECOND 

void generateFrecuencyTable(string &text, int *frecuency) {
  int i;
  multiset<char> container; 
  
  for (i = 0; i < text.length(); ++i) 
    container.insert(text[i]);

  for (i = 65; i <= 90; ++i) 
    frecuency[i-65] = container.count((char)i);
}

void findTriagramsForKasiski(string text) {
  string str;
  multimap<string, int> mp;
  set<string> norep;

  for (int i = 0; i < text.length(); ++i) {
    str = text.substr(i, 3);
    mp.insert({str, i});
    norep.insert(str);
  }

  vector<pair<string, int>> vec;
  printf("LABEL - OCURRENCIAS\n");
  for (string i: norep) {
    if (mp.count(i) > 1) {
      for (auto x: mp) 
        if (x.first == i) 
          vec.push_back({x.first, x.second});

      sort(vec.begin(), vec.end(), 
        [](auto &a, auto &b) {return a.second < b.second;});
      
      printf(" %s", str.c_str());
      str = vec[0].first;
      for (auto item: vec) 
        printf(" %d ", item.second);
      printf("\n");

      vec.clear();
    } 
  }
}

void textToUnicode(string &text) {
  string target = "0123456789abcdef", inde = "45";
  int i, j = 1, index = 0;

  string tmp; 
  map<char, string> mpi;
  for (i = 65; i <= 90; ++i) {
    if (j == 16) {
      j = 0; ++index;
    }
    tmp = inde.substr(index, 1) + target.substr(j, 1);
    mpi.insert({(char)i, tmp});
    ++j;
  }

  string textUnCode8;
  for (i = 0; i < text.length(); ++i) {
    textUnCode8.append(mpi.find(text[i])->second);
  }

  text = textUnCode8;
}

int getRandomNumberForMap() {
  return rand()%(40-10 + 1)+10;
}

void changueAlphabet(string &text) {
  int i; 
  char abc[26];
  for (i = 65; i <= 90; ++i) 
    abc[i-65] = i;
  
  map<char, char> alphabet; 
  for (auto item: abc)
    alphabet.insert({item, item + getRandomNumberForMap()});
  
  for (i = 0; i < text.length(); ++i) 
    text[i] = alphabet.find(text[i])->second;
}

void putCharacterUsingPattern(string &text) {
  int i;
  for (i = 20; i < text.length(); i+=20) 
    text.insert(i, "MANI");
  
  if (text.length() % 4 != 0) {
    i = text.length() + (4, text.length() % 4);
    int left = i - text.length();
    while (left--) 
      text.push_back('M');
  }
}
