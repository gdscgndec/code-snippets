#include<bits/stdc++.h>
using namespace std;

int board[9][9];

bool validateBoard(int n,int row,int col){
	//same columns
	for(int i=row-1;i>=0;i--){
		if(board[i][col]==1)return false;
	}
	//upper left diagonal
	for(int i=row-1,j=col-1;i>=0 && j>=0;i--,j--){
		if(board[i][j]==1)return false;
	}
	//upper right diagonal
	for(int i=row-1,j=col+1;i>=0 && j<n;i--,j++){
		if(board[i][j]==1)return false;
	}
	return true;
}

void nQueensHelper(int n,int row){
    if(row==n){
        //print the matrix
        //return
        for(int i=0;i<n;i++){
        	for(int j=0;j<n;j++){
        		cout<<board[i][j]<<" ";
        	}
        }
        // cout<<cnt<<endl;
        cout<<endl;
    }
    //Place at all possible positions
    for(int col=0;col<n;col++){
    	if(validateBoard(n,row,col)){
    		board[row][col] = 1;
    		nQueensHelper(n,row+1);
    		//Now Bactrack
    		board[row][col] = 0;
    	}
    }
    return;
}

void nQueens(int n){
    memset(board,0,9*9*sizeof(int));
    nQueensHelper(n,0);
}

int main(){
    nQueens(4);
    return 0;
}
