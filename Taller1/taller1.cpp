#include <iostream>
#include <vector>
#include <fstream>

int carac(std::vector<int> &y);
int palabras2(std::vector<int> &y, int N);
std::vector<int> palabras3(std::vector<int> &y, std::vector<int> &v);
int cant_letras(std::vector<int> &y);
int num_veces(std::vector<int> &y);

int main (void)
{
  FILE * pFile1; 
  FILE * pFile2; 
  std::vector<char> w;
  std::vector<char> y;
  std::vector<int> v;
  std::vector<int> z;
   
  pFile1 = fopen("datos1.txt", "r");

  fprintf (pFile1, "%c");

  for(int i=0; feof(pFile1)==0; i++){
    y.push_back(i);
    fscanf(pFile1, "%c", &y[i]);
    z.push_back(y[i]);
    //std::cout << z[i] << "\t" << i << std::endl;
  }
  fclose(pFile1); 
  std::cout<< z.size() << std::endl;

  pFile2 = fopen("versos_sencillos.txt", "r");

  fprintf (pFile2, "%c");

  for(int i=0; feof(pFile2)==0; i++){
    w.push_back(i);
    fscanf(pFile2, "%c", &w[i]); 
    v.push_back(w[i]);
    //std::cout << v[i] << std::endl;
  }
  fclose(pFile2); 

  std::cout << v.size() << std::endl;
  std::cout << "El número de caracteres es: " << carac(v) << std::endl;
  std::cout << "El número de 'a' y 'á' (ambas en minúscula) es: " << cant_letras(v) << std::endl;
  std::cout << "El número de veces que la palabra 'Capítulo' aparece es: " << num_veces(v) << std::endl;
  std::vector<int> vect1=palabras3(v,z);
  std::cout << "El número de palabras es: " << vect1.size() << std::endl;
  std::cout << "El número de palabras de 2 letras es: " << palabras2(vect1,2) << std::endl;
  std::cout << "El número de palabras de 1 letras es: " << palabras2(vect1,1) << std::endl;
  std::cout << "El número de palabras de 3 letras es: " << palabras2(vect1,3) << std::endl;
  std::cout << "El número de palabras de 4 letras es: " << palabras2(vect1,4) << std::endl;
  return 0;
}


int carac(std::vector<int> &y)
{
  int contador = 0;
  for(int i=0; i<y.size()-2; i++){
    if(y[i]>0 && y[i]!=10){
      contador += 2;
    }
    else if(y[i]<0){
      contador++;
    }
  }
  return contador*(0.5);
}

std::vector<int> palabras3(std::vector<int> &y, std::vector<int> &v)
{
  int contador = 0;
  int contador1 = 0;
  int contador2 = 0;
  std::vector<int> vect;
  for(int i=0; i<y.size()-1; i++){
    if(y[i]!=10 && y[i]!=32){
      for(int l=0; l<v.size()-1; l++){
	if(y[i]>0 && v[l]>0){
	  if(y[i]==v[l]){
	    contador1++;
	  }
	}
	else if(y[i]<0 && y[i+1]<0 && v[l]<0 && v[l+1]<0){
	  if(y[i]==v[l] && y[i+1]==v[l+1]){
	  contador1++;
	  }
	}
      }
    }
    else if(y[i]==10 || y[i]==32){
      if(y[i+1]!=10 && y[i+1]!=32){
	contador++;
	vect.push_back(contador1);
	contador1=0;
      }
    }
  }
  return vect;
}


int palabras2(std::vector<int> &y, int N)
{
  int contador = 0;
  for(int i=0; i<y.size(); i++){
    if(y[i]==N){
	contador++;
    }
  }
  return contador;
}


int cant_letras(std::vector<int> &y)
{
  int contador = 0;
  std::vector<int> v={97,-61,-95};
  for(int i=0; i<y.size()-2; i++){
    if(y[i]==v[0] || (y[i]==v[1] && y[i+1]==v[2]) ){
      contador++;
    }
  }
  return contador;
}


int num_veces(std::vector<int> &y)
{
  int contador = 0;
  std::vector<int> v={67,97,112,-61,-83,116,117,108,111};
  for(int i=0; i<(y.size()-v.size()+1); i++){
    if(y[i]==v[0]){
      if(y[i+1]==v[1]){
	if(y[i+2]==v[2]){
	  if(y[i+3]==v[3]){
	    if(y[i+4]==v[4]){
	      if(y[i+5]==v[5]){
		if(y[i+6]==v[6]){
		  if(y[i+7]==v[7]){
		    if(y[i+8]==v[8]){
		      contador++;
		    }
		  }
		}
	      }
	    }
	  }
	}
      }
    }
  }
  return contador;
}
