// Ap dung giai thuat minimax trong tro choi Tic-Tac-Toe 

// Bai nay chi minh hoa giai thuat minmax chu khong phai la cai dat toan bo tro choi Tic-Tac-Toe 

// Sinh vien bo sung code tai cac dau ...

 
#include<bits/stdc++.h> 
using namespace std; 

struct Move 
{ 
	int row, col; 
}; 

char computer = 'x', opponent = 'o'; 

// Ham nay kiem tra xem con nuoc di hay khong (co o nao con trong khong?)
bool isMovesLeft(char board[3][3]) 
{ 
	for (int i = 0; i<3; i++) 
		for (int j = 0; j<3; j++) 
			if (board[i][j]=='_') 
				return true; 
	return false; 
} 


// Ham uoc luong gia tri cua nut la trong cay tro choi
// Neu X thang thi ham nay co gia tri 1
// Neu O thang (X thua) thi ham nay co gia tri -1
// Neu 2 ben hoa thi co gia tri la 0

int evaluate(char b[3][3]) 
{ 
	// Kiem tra 3 dau XXX hoac OOO tren cung mot hang.
	for (int row = 0; row<3; row++) 
	{ 
		if (b[row][0]==b[row][1] && 
			b[row][1]==b[row][2]) 
		{ 
			if (b[row][0]=='x') 
				return +1; 
			else if (b[row][0]=='o') 
				return -1; 
		} 
	} 

	// Kiem tra 3 dau XXX hoac OOO tren cung mot cot.
	for (int col = 0; col<3; col++) 
	{ 
		if (b[0][col]==b[1][col] && 
			b[1][col]==b[2][col]) 
		{ 
			if (b[0][col]=='x') 
				return +1; 

			else if (b[0][col]=='o') 
				return -1; 
		} 
	} 

	// Kiem tra duong cheo. 
	if (b[0][0]==b[1][1] && b[1][1]==b[2][2]) 
	{ 
		if (b[0][0]=='x') 
			return +1; 
		else if (b[0][0]=='o') 
			return -1; 
	} 

	if (b[0][2]==b[1][1] && b[1][1]==b[2][0]) 
	{ 
		if (b[0][2]=='x') 
			return +1; 
		else if (b[0][2]=='o') 
			return -1; 
	} 

	// Truong hop 2 ben hue 
	return 0; 
} 

// Ham tinh minimax cua cac nut 
int minimax(char board[3][3], int depth, bool isMax) 
{ 
	int score = evaluate(board); 

	// Truong hop nut la, Computer thang
	if (score == 1) 
		return score; 

	// Truong hop nut la, Computer thua
	if (score == -1) 
		return score; 

	// Neu khong con cho trong de choi tiep v? khong ben nao thang
	// thi 2 ben hue nhau
	if (isMovesLeft(board)==false) 
		return 0; 
 
	// Luot di cua Max
	if (isMax) 
	{ 
		int best = -1000; 

		// Duyet tat ca cac o tren ban co 
		for (int i = 0; i<3; i++) 
		{ 
			for (int j = 0; j<3; j++) 
			{ 
				// Kiem tra cac o con trong 
				if (board[i][j]=='_') 
				{ 
					// Computer dat X vao o trong nay. Tinh gia tri cua trang thai moi sinh ra 
					board[i][j] = computer; 
					best = max( best, 
						minimax(board, depth+1, !isMax) ); 

					// Tra ve hien trang cua ban co 
					board[i][j] = '_'; 
				} 
			} 
		} 
		return best; 
	} 

	// Tuong tu ben tren doi voi luot di cua Min
	else
	{ 
		int best = 1000; 
		for (int i = 0; i<3; i++) 
		{ 
			for (int j = 0; j<3; j++) 
			{ 
				// Check if cell is empty
				// Kiem tra xem co phai la o trong?
				if (board[i][j]=='_') 
				{ 
					board[i][j] = opponent;
					best = min(best, 
						minimax(board, depth+1, !isMax)); 
					board[i][j] = '_'; 
				} 
			} 
		} 
		return best; 
	} 
} 


// Xay dung ham tim nuoc di tot nhat
Move findBestMove(char board[3][3]) 
{ 
	int bestVal = -1000; 
	Move bestMove; 
	bestMove.row = -1; 
	bestMove.col = -1; 
	
	// Duyet qua tat ca cac o tren ban co. 
	// Uoc luong gia tri minimax tai cac vi tri trong
	
	for (int i = 0; i<3; i++) 
	{ 
		for (int j = 0; j<3; j++) 
		{ 
			// Tim nhung o trong (chua co gia tri X hay O)
			if (board[i][j]=='_') 
			{ 
				// Danh chu X vao o trong 
				board[i][j] = computer; 

				// Uoc luong gia tri sau khi dien X 
				int moveVal = minimax(board, 0, false); 

				// Reset lai o trong 
				board[i][j] = '_'; 

				
				// Neu gia tri cua nuoc di hien tai tot hon gia tri tot nhat (bestVal)
				// thi cap nhat lai gia tri tot nhat
				if (moveVal > bestVal) 
				{ 
					bestMove.row = i; 
					bestMove.col = j; 
					bestVal = moveVal; 
				} 
			} 
		} 
	} 

	cout<<"Gia tri cua nuoc co tot nhat la : "<<bestVal; 
	return bestMove;
} 

// Ham chinh
int main() 
{ 
	char board[3][3] = 
	{ 
		{ 'x', 'o', 'x' }, 
		{ 'o', 'o', 'x' }, 
		{ '_', '_', '_' } 
	}; 

	Move bestMove = findBestMove(board); 
	
	cout<<endl<<"Nuoc di tot nhat la : ";
	cout<<"["<<bestMove.row<<"]"<<"["<<bestMove.col<<"]";
	return 0; 
} 

