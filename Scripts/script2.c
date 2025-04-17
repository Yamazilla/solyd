#include <stdio.h> 

int main(int argc, char *argv[]) {
	int contador;

	if (argc>1) {
		for (contador=0;contador<=254;contador++){
			printf("atacando o IP: %s.%i\n", argv[1], contador);
		}
	} else {
		printf("./args x.x.x");
	}

	return 0;
}
