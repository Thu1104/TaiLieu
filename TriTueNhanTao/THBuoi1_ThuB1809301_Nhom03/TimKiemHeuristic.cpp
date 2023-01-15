// Giai thuat A*

#include<stdio.h>
#include<set>
#include<stack>
#include<vector>
#include<cmath>

using namespace std;
const int board_rows = 3;
const int board_cols = 3;
const int empty_tile = 0;
const int max_op = 4;

struct State{
	int num[board_rows][board_cols];
	int empty_row;
	int empty_col;
};
struct Node{
	State state;
	Node* parent;
	int g; //Gia tri duong di cua nut goc den nut hien tai
	int h; //Ket qua uoc luong cua ham heuristic cua nut hien tai den trang thai dich
	int f;
};
//Dinh nghia phep toan so sanh trong multiset
struct node_cmp{
	bool operator()(Node* a, Node* b){
		return a->f < b->f;
	}
};
bool sameState(State s1, State s2){
	if(s1.empty_col != s2.empty_col || s1.empty_row != s2.empty_row){
		return false;
	}
	for(int row = 0; row < board_rows; row++){
		for(int col = 0; col < board_cols; col++){
			if(s1.num[row][col] != s2.num[row][col]){
				return false;
			}
		}
	}
	return true;
}
bool up(State s, State &out){
	int er = s.empty_row, ec = s.empty_col;
	if(er>0){
		out = s;
		out.empty_col = ec;
		out.empty_row = er-1;
		out.num[er][ec] = s.num[er-1][ec];
		out.num[er-1][ec] = empty_tile;
		return true;
	}
	return false;
}
bool down(State s, State &out){
	int er = s.empty_row, ec = s.empty_col;
	if(er < board_rows-1){
		out = s;
		out.empty_col = ec;
		out.empty_row = er+1;
		out.num[er][ec] = s.num[er+1][ec];
		out.num[er+1][ec] = empty_tile;
		return true;
	}
	return false;
}
bool left(State s, State &out){
	int er = s.empty_row, ec = s.empty_col;
	if(ec>0){
		out = s;
		out.empty_col = ec-1;
		out.empty_row = er;
		out.num[er][ec] = s.num[er][ec-1];
		out.num[er][ec-1] = empty_tile;
		return true;
	}
	return false;
}
bool right(State s, State &out){
	int er = s.empty_row, ec = s.empty_col;
	if(ec < board_cols-1){
		out = s;
		out.empty_col = ec+1;
		out.empty_row = er;
		out.num[er][ec] = s.num[er][ec+1];
		out.num[er][ec+1] = empty_tile;
		return true;
	}
	return false;
}
bool call_operator(State s, State &out, int op_no){
	switch(op_no){
		case 1: return up(s, out);
		case 2: return down(s, out);
		case 3: return left(s, out);
		case 4: return right(s, out);
		default: return false;
	}
}
void print_state(State s){
	for(int i=0; i<board_rows; i++){
		for(int j=0; j<board_cols; i++){
			cout<<s.num[i][j] << " " ;
		}
		cout << "\n";
	}
}
bool is_goal(State s, State goal){
	return sameState(s, goal);
}
//Ham H1 dem so vi tri sai khac
int h1(State s, State s2){
	int count = 0;
	for(int row=0; row<board_rows; row++){
		for(int col=0; col<board_cols; col++){
			if(s.num[row][col] != s2.num[row][col]){
				count++;
			}
		}
	}
	return count++;
}
//Kiem tra phan tu da co trong frontier chua
Node* find_node(State s, multiset<Node*, node_cmp> list){
	for(Node* n: list){
		if(sameState(s, n->state)){
			return n;
		}
	}
	return NULL;
}
//Kiem tra phan tu da co trong explore chua
bool find_state(State s, vector <State> *explored){
	for(State c1: *explored){
		if(sameState(s, c1))
			return true;
	}
}
//Nhap trang thai cho bai toan
State* getState(){
	State *s = new State();
	for(int row=0; row<board_rows; row++){
		for(int col=0; col<board_cols; col++){
			cin >> s->num[row][col];
			if(s->num[row][col] == 0){
				s->empty_row = row;
				s->empty_col = col;
			}
		}
	}
	return s;
}
//Giai thuat A*
Node* A_star(State init_state, State goal_state, vector <State> *explored){
	Node* root = new Node();
	root->state = init_state;
	root->parent = NULL;
	root->g = 0;
	root->h = h1(init_state, goal_state);
	root->f = root->g + root->h;
	multiset <Node*, node_cmp> frontiers;
	frontiers.insert(root);
	while(!frontiers.empty()){
		Node* node = *frontiers.begin();
		frontiers.erase(frontiers.begin());
		explored->push_back(node->state);
		if(sameState(node->state, goal_state)){
			return node;
		}
		for(int op=1; op<=4; op++){
			State new_state;
			if(call_operator(node->state, new_state, op)){
				if(find_state(new_state, explored)){
					continue;
				}
				Node* n = find_node(new_state, frontiers);
				if(n==NULL){
					n = new Node();
					n->parent = node;
					n->state = new_state;
					n->h = h1(new_state, goal_state);
					print_state(new_state);
					n->g = node->g + 1;
					n->f = n->g + n->h;
					cout<<"=== Gia tri g: "<<n->g <<"=== Gia tri f: "<<n->f <<endl;
					frontiers.insert(n);
				}
				else{
					n->g = node->g+1;
					n->f = n->g + n->h;
				}
			}
		}
	}
	return NULL;
}
void print_path(Node* r){
	int i=0;
	stack<State> q;
	cout<<"Duong di loi giai\n";
	while(r->parent !=NULL){
		q.push(r->state);
		r=r->parent;
	}
	q.push(r->state);
	while(!q.empty()){
		cout <<"Trang thai thu "<< i++ <<endl;
		print_state(q.pop());
		cout << endl;
		q.pop();
	}
}
