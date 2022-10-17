#include <iostream>
#include "library.hpp"

int main(int, char**) {
  srand(static_cast <unsigned int> (time(0)));

  string text = getDataFromFile("input.txt");
  
  sustituionsInCharacters(text);

  
  //cout << text << '\n';

  deleteacents(text);

  //cout << text << '\n';

  arrToUpper(text);

  //cout << text << '\n';

  deleteWhiteSpaceAndPoints(text);

  //cout << text << '\n';

  int *frecuency = new int[25];

  generateFrecuencyTable(text, frecuency);


  findTriagramsForKasiski(text);


  //textToUnicode(text); 

  
  //cout << text << '\n';

  //changueAlphabet(text);

  //cout << text;

  cout << text.size() << '\n';


  putCharacterUsingPattern(text);

  cout << text.length() << '\n';

  

  cout << text << '\n';




  return 0;
}
