//B?i tap 5: Su dung Queue trong C++ - Dong nuoc

#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
#include<queue>
#include<stack>
#define tankcapacity_x 9 //Suc chua binh x
#define tankcapacity_y 4 //Suc chua binh y
#define goal 6 //Muc tieu luong nuoc can dong duoc

//Hang chuoi de in ra ten cac hanh dong
const char* action[]={"First State","pour Water Full X", "pour Water Full Y","pour Water Empty X","pour Water Empry Y","pour Water X to Y","pour Water Y to X"};

using namespace std;

//Khai bao cau truc trang thai (State)
typedef struct{
	int x; // Luong nuoc trong binh x
	int y; // Luong nuoc trong binh y
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

//Ham so sanh trang thai co bang nhau khong
int compareStates(State state1, State state2){
	return (state1.x == state2.x && state1.y == state2.y);
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
 
// Ham lam day nuoc binh X
int pourWaterFullX(State cur_state, State *result) {
	if(cur_state.x < tankcapacity_x) {
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
		result->x = 0;
		result->y = cur_state.y;
		return 1;
	}
	return 0;
}

//Lam rong binh nuoc Y
int pourWaterEmptyY(State cur_state, State *result){
	if(cur_state.y > 0){
		result->y = 0;
		result->x = cur_state.x;
		return 1;
	}
	return 0;
}
//Chuyen nuoc tu binh X sang binh Y
int pourWaterXY(State cur_state, State *result){
	if(cur_state.x > 0 && cur_state.y < tankcapacity_y){
		result->x = max(cur_state.x - (tankcapacity_y - cur_state.y), 0);
		result->y = min(cur_state.x + cur_state.y, tankcapacity_y);
		return 1;
	}
	return 0;
}

//Chuyen nuoc tu binh Y sang binh X
int pourWaterYX(State cur_state, State *result){
	if(cur_state.y > 0 && cur_state.x < tankcapacity_x){
		result->y = max(cur_state.y - (tankcapacity_x - cur_state.y), 0);
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

//Khai bao cau truc nut (dinh) de dung cay tim kiem
typedef struct Node{
	State state;
	struct Node* Parent;
	int no_function;
}Node;

//Ham kiem tra trang thai co nam trong stack
int find_State(State state, queue<Node*> openQueue){
	while(!openQueue.empty()){
		if(compareStates(openQueue.front()->state, state))
			return 1;
		openQueue.pop();
	}
	return 0;
}

//Thuat toan duyet theo chieu sau
Node* BFS_Algorithm(State state){
	//Khai bao hai ngan xep Open va Close
	queue<Node*> Open_BFS;
	queue<Node*> Close_BFS;
	//Tao nut trang thai cha
	Node* root = (Node*)malloc(sizeof(Node));
	root->state = state;
	root->Parent = NULL;
	root->no_function = 0;
	Open_BFS.push(root);
	while(!Open_BFS.empty()){
		//Lay mot dinh trong ngan xep
		Node* node = Open_BFS.front(); //Lay gia tri ben trai cua Frontier de kiem tra
		Open_BFS.pop();
		Close_BFS.push(node);
		//Kiem tra xem dinh lay ra co phai trang thai muc tieu?
		if(goalcheck(node->state))
			return node;
		int i;
		for(i=1; i<=6; i++){
			State newstate;
			makeNullState(&newstate);
			if(call_operator(node->state, &newstate, i)){
				//Neu trang thai moi sinh ra da ton tai thi bo qua
				if(find_State(newstate, Open_BFS) || find_State(newstate, Close_BFS))
					continue;
				//Neu trang thai moi chua ton tai thi them vao ngan xep
				Node* newNode = (Node*)malloc(sizeof(Node));
				newNode->state = newstate;
				newNode->Parent = node;
				newNode->no_function = i;
				Open_BFS.push(newNode);
			}
		}
	}
	return NULL;
}

// In ket qua chuyen nuoc de dat den trang thai muc tieu
void print_WaysToGetGoal(Node* node) {
	stack<Node*> stackPrint;
	// Duyet nguoc ve nut parent
	while(node->Parent != NULL) {
		stackPrint.push(node);
		node = node->Parent;
	}
	stackPrint.push(node);
	// In ra thu tu hanh dong truyen nuoc
	int no_action = 0;
	while(!stackPrint.empty()){
		printf("\nAction %d: %s", no_action, action[stackPrint.top()->no_function]);
		print_State(stackPrint.top()->state);
		stackPrint.pop();
		no_action++;
	}
}

int main() {
	State cur_state = {0, 0};
	printf("Trang thai bat dau");
	print_State(cur_state);
	Node* p = BFS_Algorithm(cur_state);
	print_WaysToGetGoal(p);
	return 0;
}
