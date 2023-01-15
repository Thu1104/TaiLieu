#include<stdio.h>
#include<string.h>
#include<malloc.h>
typedef struct{
	char TenDoVat[20];
	float TL, GT, DG;
	int SL, PA;
}DoVat;
DoVat* Docfile(float *W, int *n){
	FILE *f = fopen("CAIBALO.INP", "r");
	fscanf(f, "%f", W);
	DoVat *dsdv;
	dsdv = (DoVat*)malloc(sizeof(DoVat));
	int i=0;
	while(!feof(f)){
		fscanf(f, "%f%f%d%[^\n]", &dsdv[i].TL, &dsdv[i].GT, &dsdv[i].SL, &dsdv[i].TenDoVat);
		dsdv[i].DG = dsdv[i].GT/dsdv[i].TL;
		dsdv[i].PA = 0;
		i++;
		dsdv = (DoVat*)realloc(dsdv, sizeof(DoVat)*(i+1));
	}
	*n = i;
	fclose(f);
	return dsdv;
}
void Swap(DoVat &X, DoVat &Y){
	DoVat temp;
	temp = X;
	X = Y;
	Y = temp;
}
void BubbleSort(DoVat *dsdv, int n){
	int i, j;
	for(i=0; i<n-1; i++){
		for(j=n-1; j>=i+1; j--){
			if(dsdv[j].DG>dsdv[j-1].DG){
				Swap(dsdv[j],dsdv[j-1]);
			}
		}
	}
}
void ThamAn(DoVat *dsdv, float W, int n){
	int i;
	for(i=0; i<n; i++){
		dsdv[i].PA = W / dsdv[i].TL;
		if(dsdv[i].PA> dsdv[i].SL){
			dsdv[i].PA = dsdv[i].SL;
		}
		W = W- dsdv[i].PA *dsdv[i].TL;
	}
}
void InDS(DoVat *dsdv, float W, int n){
	int i;
	float TTL=0, TGT=0;
	printf("Giai bai toan Cabalo2 bang thuat toan Tham An: \n");
	printf("|---|------------------|-------------|---------|----------|---------|-----------|\n");
	printf("|STT|    Ten Do Vat    | Trong luong | Gia tri | So luong | Don gia | Phuong an |\n");
	printf("|---|------------------|-------------|---------|----------|---------|-----------|\n");
	for(i=0; i<n; i++){
		printf("|%2d |%-18s|%13.2f|%9.2f|%10d|%9.2f|%6d     |\n",i+1,dsdv[i].TenDoVat,dsdv[i].TL,dsdv[i].GT,dsdv[i].SL,dsdv[i].DG,dsdv[i].PA);
		printf("|---|------------------|-------------|---------|----------|---------|-----------|\n");
		TTL = TTL + dsdv[i].PA*dsdv[i].TL;
		TGT = TGT + dsdv[i].PA*dsdv[i].GT;
	}
	printf("Trong luong cua balo: %.2f\n", W);
	printf("Tong trong luong cua do vat: %.2f\n", TTL);
	printf("Tong gia tri cua do vat: %.2f\n", TGT);
}
int main (){
	DoVat *dsdv;
	float W;
	int n;
	dsdv = Docfile(&W,&n);
	BubbleSort(dsdv,n);
	ThamAn(dsdv,W,n);
	InDS(dsdv,W,n);
	free(dsdv);
	return 0;
}
