#include<stdio.h>
#include<string.h>
#include<malloc.h>
typedef struct {
	char Ten[20];
	float TL, GT, DG;
	int PA;
}DoVat;
DoVat *DocFile(float *W, int *n){
	FILE *fb;
	fb = fopen("CaiBalo1.INP","r");
	fscanf(fb,"%f",W);
	DoVat *ds;
	ds = (DoVat*)malloc(sizeof(DoVat));
	int i=0;
	while(!feof(fb)){
		printf("%f%f%[^\n]", ds[i].TL, ds[i].GT, ds[i].Ten);
		ds[i].DG = ds[i].GT / ds[i].TL;
		ds[i].PA = 0;
		i++;
		ds = (DoVat*)realloc(ds,sizeof(DoVat)*(i+1));
		}
	*n = i;
	fclose(fb);
	return ds;
} 
void Swap(DoVat *X, DoVat *Y){
	DoVat Temp;
	Temp = *X;
	*X = *Y;
	*Y = Temp;
}
void InDS(DoVat *ds, float W, int n){
	int i;
	printf("|---|-------------|---------|------------------|---------|-----------|\n");
	printf("|STT| Trong Luong | Gia Tri |    Ten Do Vat    | Don Gia | Phuong An |\n");
	printf("|---|-------------|---------|------------------|---------|-----------|\n");
	for(i=0; i<n; i++){
		printf("|%3d|%13.2f|%9.2f|%18s|%9.2f|%6f     |", i+1, ds[i].TL, ds[i].GT, ds[i].Ten, ds[i].DG, ds[i].PA);
		printf("|---|-------------|---------|------------------|---------|-----------|\n");
	}
}

