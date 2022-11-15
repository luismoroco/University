#include "library.hpp"

int main(int, char**) {
  /* PRIMERA PARTE 
  string buffer = getDataFromFile("Cesar.txt");
  deleteacents(buffer);
  deleteWhiteSpaceAndPoints(buffer);
  arrToUpper(buffer);

  cout << "ORIGINAL => \n" << buffer << '\n';

  cesarEncoder(buffer);

  cout << "CIFRADO => \n" << buffer << '\n';

  //-----

  descifrarText(buffer);

  cout << "DESCIFRADO => \n" << buffer << '\n';

  */
  
  // ----------------------

  
  string buffer = getDataFromFile("Cesar.txt");
  sustituionsInCharacters(buffer);
  deleteacents(buffer);
  deleteWhiteSpaceAndPoints(buffer);
  arrToUpper(buffer); 

  cout << buffer << '\n';

  cifrVignere(buffer, "MEZCLADOR");

  cout << buffer << '\n';
  
  desciVginere(buffer, "MEZCLADOR");

  cout << buffer << '\n';

  return 0;
}