#include <iostream>
#include <cstring>
#include <stdlib.h>

int main(int argc, char** argv)
{ 
	char buff[1000];
    std::cout << "Enter a string " << std::endl;
    std::cout << ">>";
    std::cin >> buff;

int i, j;
int k = strlen(buff);

   for (i = 0; i < k; i++) 
   {
      if (buff[i] == 'a' || buff[i] == 'e' || buff[i] == 'i' || buff[i] == 'o' || buff[i] == 'u') 
      {
         for (j = i; j < k; j++) 
         {
            buff[j] = buff[j + 1];
         }
      }
   }

    std::cout << buff << std::endl;

    return 0;
}