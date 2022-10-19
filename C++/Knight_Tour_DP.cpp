//https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define N 8
//setw(2) = set width of 2
int is_safe(int x,int y,int sol[N][N])
{
     if(x>=0 && x<N && y>=0 && y<N && sol[x][y]==-1)
     {
         return 1;
     }
     return 0;
}
void print_sol(int sol[N][N])
{
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            cout<<" "<<setw(2)<<sol[i][j]<<" ";
        }
        cout<<endl;
    }
}
int solve_KT_until(int x,int y,int movei ,int sol[N][N],int xmove[8],int ymove[8])
{
    int k,next_x,next_y;
    if(movei==N*N)
    {
        return 1;
    }
    for(k=0;k<8;k++)
    {
        next_x=x+xmove[k];
        next_y=y+ymove[k];
        if(is_safe(next_x,next_y,sol))
        {
            sol[next_x][next_y]=movei;
            if(solve_KT_until(next_x,next_y,movei+1,sol,xmove,ymove)==1)
            {
                return 1;
            }
            else
            {
                sol[next_x][next_y]=-1;
            }
        }
    }
    return 0;
}
int knight_tour()
{
    int sol[N][N];
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            sol[i][j]=-1;
        }
    }
    
    int xmove[8]={2,1,-1,-2,-2,-1,1,2};
    int ymove[8]={1,2,2,1,-1,-2,-2,-1};
    sol[0][0]=0;
    if(solve_KT_until(0,0,1,sol,xmove,ymove)==0)
    {
        cout<<"Sol does not exist"<<endl;
        return 0;
        
    }
    else
    {
        print_sol(sol);
    }
    return 1;
}

int main() 
{
    knight_tour();
  }
