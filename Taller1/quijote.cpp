#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

int main ( )
{
  std::ifstream file("quijote.txt");
  std::string linea = "";

  if(file.is_open( ))
    {
      int lineas = 0;
      int letras = 0;
      int numPal = 0;
      int numA = 0;
      int numAtildes = 0;
      int numCap = 0;
      int palDosLetras = 0;
      int palTresLetras = 0;
      int palCuatroLetras = 0;
      
      while( file.good())
	{
	  getline (file,linea);
	  std::istringstream iss(linea);
	  while(iss)
	    {
	      std::string subs;
	      iss >> subs; // separa por palabra
	      std::vector<char> v(subs.begin(), subs.end()); // separa las palabras en letras

	      if (v.size() == 2) 
		palDosLetras++;
	      else if (v.size() == 3)
		palTresLetras++;
	      else if (v.size() == 4)
		palCuatroLetras++;

	      if(subs.compare("Capítulo") == 0) //Cuenta el numero de capitulos
		numCap++;
	      
	      for(int i= 0; i < v.size(); i++)
		{
		  if(v[i] == 'a' || v[i]=='A')
		      numA++;
		}
	      numPal++;
	    } 
	  letras += linea.size();
	  lineas++;
	}
      
      std::cout << "El numero de caracteres es " << letras << std::endl;
      std::cout << "El numero de palabras es " << numPal << std::endl;
      std::cout << "El numero de a y á es " << numA << std::endl;
      std::cout << "El numero de veces que aparece la palabra Capítulo es " << numCap << std::endl;
      std::cout << "El numero de palabras con 2 letras es " << palDosLetras << std::endl;
      std::cout << "El numero de palabras con 3 letras es " << palTresLetras << std::endl;
      std::cout << "El numero de palabras con 4 letras es " << palCuatroLetras << std::endl;
      
    }
  else std::cout << "Imposible abrir archivo" << std::endl;

  return 0;
}
