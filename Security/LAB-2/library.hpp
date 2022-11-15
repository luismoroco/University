#include <bits/stdc++.h>
using namespace std;

const char *alpha = "ABCDEFGHIJKLMN*OPQRSTUVWXYZ";
const int len = strlen(alpha);

void sustituionsInCharacters(string &text) {
  int i; 
  char c;
  for (i = 0; i < text.length(); ++i) {
    c = text[i];
    if (c >= 65 && c <= 90) 
      c += 32;
    switch (c) {
      case -61: 
        if (text[i+1]  == -111) {
          text[i] = '*'; 
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

void arrToUpper(string &text) {
  int i; 
  char c; 
  for (i = 0; i < text.length(); ++i) {
    c = text[i];
    if (c >= 97 && c <= 122) 
      text[i] -= 32;
  }
}

char findNextLetter(char c) {
  int i;
  for (i = 0; i < len; ++i) 
    if (alpha[i] == c) 
      break;
  
  return (i+3 <= 27) 
    ? alpha[i+3] : alpha[(i+3)-27]; 
}

char findPrevLetter(char c) {
  int i;
  for (i = 0; i < len; ++i) 
    if (alpha[i] == c) 
      break;
  
  return (i-3 >= 0) 
    ? alpha[i-3] : alpha[27-(i-3)];  
}

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

void cesarEncoder(string &text) {
  int i;
  for (i = 0; i < text.length(); ++i) 
    text[i] = (text[i] != ' ') 
      ? findNextLetter(text[i]) : text[i];
  
  for (i = 0; i < text.length(); ++i)
    if (text[i] == '*') {
      text.erase(i, 1);
      text.insert(i, "Ñ");
    }
}

void descifrarText(string &text) {
  while (text.find("Ñ") != string::npos) {
    auto i = text.find("Ñ");
    text.erase(i, 2);
    text.insert(i, "*");
  }

  for (int i = 0; i < text.length(); ++i)
    text[i] = findPrevLetter(text[i]);
}


// 2 

int getIndex(char c) {
  int i;
  for (i = 0; i < len; ++i) 
    if (alpha[i] == c) 
      break;
  return i;
}

void cifrVignere(string &text, string key) {
  int itKey = 0, i, tmK = key.size();
  for (i = 0; i < text.length(); ++i) {
    if (itKey == tmK) {
      itKey = 0;
      text[i] = alpha[getIndex(text[i])+getIndex(key[itKey])];
    } else {
      text[i] = alpha[(getIndex(text[i])+getIndex(key[itKey])) % 27];
    }
    ++itKey;
  }

  for (i = 0; i < text.length(); ++i)
    if (text[i] == '*') {
      text.erase(i, 1);
      text.insert(i, "Ñ");
    }
}

void desciVginere(string &text, string key) {
  while (text.find("Ñ") != string::npos) {
    auto i = text.find("Ñ");
    text.erase(i, 2);
    text.insert(i, "*");
  }
    
  int itKey = 0, i, tmK = key.size();
  for (i = 0; i < text.length(); ++i) {
    if (itKey == tmK) {
      itKey = 0;
      text[i] = alpha[getIndex(text[i])-getIndex(key[itKey])];
    } else {
      text[i] = alpha[(getIndex(text[i])-getIndex(key[itKey])) % 27];
    }
    ++itKey;
  }

}
