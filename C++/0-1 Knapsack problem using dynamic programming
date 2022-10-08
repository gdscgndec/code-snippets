//C++ implementation for 0-1 Knapsack problem using DP
#include <bits/stdc++.h>
using namespace std;

//below function returns maximum of 2 integers
int maximum(int x , int y){
  if(x>y){
    return x;
  }
  else{
    return y;
  }
}
//returns the max value that can be put into the given Knapsack
int Knapsack(int W, int wt[], int val[], int n)
{
    vector<vector<int>> K(n + 1, vector<int>(W + 1));
    for(int i = 0; i <= n; i++)
    {
        for(int w = 0; w <= W; w++)
        {
            if (i == 0 || w == 0)
                K[i][w] = 0;
            else if (wt[i - 1] <= w)
                K[i][w] = max(val[i - 1] +
                                K[i - 1][w - wt[i - 1]],
                                K[i - 1][w]);
            else
                K[i][w] = K[i - 1][w];
        }
    }
    return K[n][W];
}
int main()
{
    int wt[] = { 5,10,15,20,25 };
    int val[] = { 30,40,120,100,50 };
    int W = 35;
    int n = sizeof(val) / sizeof(val[0]);
    cout << Knapsack(W, wt, val, n);
    return 0;
}
