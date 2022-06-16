#include <stdio.h>
#include <stdlib.h>  
int main()
{
  int *vetor, i; 
  
  vetor = (int *) realloc(vetor, 22 * sizeof(int));
  
  for (i = 0; i < 22; i++)
  {
    printf("\nDigite o valor para a posicao %d do vetor: ", i+1);
    scanf("%d",&vetor[i]);
  }
  
  // ------ Percorrendo o vetor e imprimindo os valores ----------
  printf("\n*********** Valores do vetor dinamico ************\n\n");
  
  for (i = 0;i < 22; i++)
  {
    printf("%d\n",vetor[i]);
  }
  
  free(vetor);
  
  return 0;
}


/*

#include <stdio.h>
#include <stdlib.h>  
int main()
{
  float *v; 
  int i;
  
  v = (float *) realloc(v, 22 * sizeof(float));
  
  free(v);

  return 0;
}
  */
