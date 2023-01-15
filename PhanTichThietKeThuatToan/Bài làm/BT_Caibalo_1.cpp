#include<stdio.h>
#include<malloc.h>
#include<string.h>
typedef struct{
	char Ten[20];
	float TL, GT, DG;
	int PA;
}DoVat;
DoVat *DocFile(float *W, int *n){
	FILE *f;
	f=fopen("CaiBalo1.INP","r");
	fscanf(f,"%f",W);
	DoVat *dsdv;
	dsdv=(DoVat*)malloc(sizeof(DoVat));
	int i=0;
	while(!feof(f)){
		fscanf(f,"%f%f%[^\n]",&dsdv[i].TL,&dsdv[i].GT,&dsdv[i].Ten);
		dsdv[i].DG = dsdv[i].GT/dsdv[i].TL;
		dsdv[i].PA = 0;
		i++;
		dsdv=(DoVat*)realloc(dsdv,sizeof(DoVat)*(i+1));
	}
	*n=i;
	fclose(f);
	return dsdv;
}
void Swap(DoVat *X, DoVat *Y){
	DoVat temp;
	temp= *X;
	*X = *Y;
	*Y = temp;
}	
void NoiBot(DoVat *dsdv, int n){
	int i, j;
	for(i=0; i<=n-2; i++){
		for(j=n-1 ; j>=i+1; j--){
			if(dsdv[j].DG > dsdv[j-1].DG){
				Swap(&dsdv[j], &dsdv[j-1]);
			}
		}
	}
}
void ThamAn(DoVat *dsdv, int n, float W){
	int i;
	for(i=0; i<n; i++){
		dsdv[i].PA = W/dsdv[i].TL;
		W = W - dsdv[i].PA*dsdv[i].TL;
	}
}
void InDS(DoVat *dsdv, int n, float W){
	int i;
	float TongTL=0, TongGT=0;
	printf("Bai toan Cai ba lo 1: \n");
	printf("|---|-------------------|-------------|---------|---------|-----------|\n");
	printf("|STT|  Ten Loai Do Vat  | Trong Luong | Gia Tri | Don Gia | Phuong An |\n");
	printf("|---|-------------------|-------------|---------|---------|-----------|\n");
	for(i=0; i<n; i++){
		printf("|%2d |%-19s|%-13.2f|%-9.2f|%-9.2f|%6d     |\n", i+1, dsdv[i].Ten, dsdv[i].TL, dsdv[i].GT, dsdv[i].DG, dsdv[i].PA);
		printf("|---|-------------------|-------------|---------|---------|-----------|\n");
		TongTL = TongTL + dsdv[i].PA*dsdv[i].TL;
		TongGT = TongGT + dsdv[i].PA*dsdv[i].GT;
	}
	printf("Trong luong cua ba lo la: %.2f\n",W);
	printf("Tong Trong Luong: %.2f\n",TongTL);
	printf("Tong Gia Tri: %.2f\n",TongGT);
}
int main(){
	DoVat *dsdv;
	float W;
	int n;
	dsdv= DocFile(&W,&n);
	NoiBot(dsdv,n);
	ThamAn(dsdv,n,W);
	InDS(dsdv,n,W);
	return 0;
}

