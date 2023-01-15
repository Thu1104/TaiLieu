//Bai tap 1: Bai toan dong nuoc

#include<stdio.h>
#include<stdlib.h>
#define tankcapacity_x 9 //Suc chua binh x
#define tankcapacity_y 4 //Suc chua binh y
#define empty 0 
#define goal 6 //Muc tieu luong nuoc can dong duoc
#define Maxlength 100 //Su dung cai dac ngan xep (Stack)

//Hang chuoi de in ra ten cac hanh dong
const char* action[]={"First State","pour Water Full X", "pour Water Full Y","pour Water Empty X","pour Water Empry Y","pour Water X to Y","pour Water Y to X"};

//Khai bao cau truc trang thai
typedef struct{
	int x;
	int y;
}State;

//Khoi tao trang thai binh X=0 va Y=0
void makeNullState(State *state){
	state->x = 0;
	state->y = 0; 
}

//In trang thai
void print_State(State state){
	printf("\n  X:%d --- Y:%d", state.x, state.y);
}

//Ham kiem tra trang thai muc tieu
int goalcheck(State state){
	return(state.x == goal || state.y == goal);
}

//Ham max
int max(int x, int y){
	if(x > y) return x;
	return y;
}

//Ham min
int min(int x, int y){
	if(x < y) return x;
	return y;
}
 
//Lam day nuoc binh X
int pourWaterFullX(State cur_state, State *result){
	if(cur_state.x < tankcapacity_x){
		result->x = tankcapacity_x;
		result->y = cur_state.y;
		return 1;
	}
	return 0;
 }

//Lam day nuoc binh y
int pourWaterFullY(State cur_state, State *result){
	if(cur_state.y < tankcapacity_y){
		result->y = tankcapacity_y;
		result->x = cur_state.x;
		return 1;
	}
	return 0;
}

//Lam rong binh nuoc X
int pourWaterEmptyX(State cur_state, State *result){
	if(cur_state.x > 0){
		result->x = empty;
		result->y = cur_state.y;
		return 1;
	}
	return 0;
}

//Lam rong binh nuoc Y
int pourWaterEmptyY(State cur_state, State *result){
	if(cur_state.y > 0){
		result->y = empty;
		result->x = cur_state.x;
		return 1;
	}
	return 0;
}
//Chuyen nuoc tu binh X sang binh Y
int pourWaterXY(State cur_state, State *result){
	if(cur_state.x > 0 && cur_state.y < tankcapacity_y){
		result->x = max(cur_state.x - (tankcapacity_y - cur_state.y), empty);
		result->y = min(cur_state.x + cur_state.y, tankcapacity_y);
		return 1;
	}
	return 0;
}

//Chuyen nuoc tu binh Y sang binh X
int pourWaterYX(State cur_state, State *result){
	if(cur_state.y > 0 && cur_state.x < tankcapacity_x){
		result->y = max(cur_state.y - (tankcapacity_x - cur_state.y), empty);
		result->x = min(cur_state.y + cur_state.x, tankcapacity_x);
		return 1;
	}
	return 0;
}

//Goi cac phep toan tren trang thai
int call_operator(State cur_state, State *result, int option){
	switch(option){
		case 1: return pourWaterFullX(cur_state, result);
		case 2: return pourWaterFullY(cur_state, result);
		case 3: return pourWaterEmptyX(cur_state, result);
		case 4: return pourWaterEmptyY(cur_state, result);
		case 5: return pourWaterXY(cur_state, result);
		case 6: return pourWaterYX(cur_state, result);
		default: printf("Error calls operators");
			return 0;
	}
}

int main(){
	State cur_state = {5, 4}, result;
	int i;
	printf("Trang thai bat dau:");
	print_State(cur_state);
	for(i=1; i<=6; i++){
		int j = call_operator(cur_state, &result, i);
		if(j == 1){ //Thuc hien hanh dong thanh cong
			printf("\nHanh dong %s thanh cong", action[i]);
			print_State(result);
		}
		else{
			printf("\nHanh dong %s KHONG thanh cong", action[i]);
		}
	}
	return 0;
}
