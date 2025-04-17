#include <stdio.h>
#include <string.h>

int main () {

	char alvo[100];
	char resposta[4];
	int porta;

	printf("Digite o alvo: ");
	scanf("%s", &alvo);

	printf("Digite a porta: ");
	scanf("%i", &porta);

	printf("Você realmente quer iniciar o ataque no alvo %s? (Sim/Nao)\n", alvo);
	scanf("%s", resposta);
	
	if (strcmp(resposta,  "sim") == 0){
		printf("Iniciando ataque no alvo %s, na porta %i", alvo, porta);

} else{
	printf("Cancelando o ataque no alvo %s", alvo);
}




	return 0;
}
