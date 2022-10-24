package com.mycompany.noor;
import java.util.Scanner;
public class matrix 
{
    int mat[][],m,n,i,j;
 void input()
 {
     Scanner sc=new Scanner(System.in);
     System.out.println("enter rows and columns");
     m=sc.nextInt();
     n=sc.nextInt();
     mat=new int[m][n];
     System.out.println("enter elements"+(m+n));
     for(i=0;i<m;i++)
     {
         for(j=0;j<n;j++)
             mat[i][j]=sc.nextInt();
     }
 }
 void display()
 {
     for(i=0;i<m;i++)
     {
         for(j=0;j<n;j++)
            System.out.print(mat[i][j]+" ");
         System.out.println();
     }
 }
 void sums()
 {
     int rsum;
     for(i=0;i<m;i++)
     {   rsum=0;
         for(j=0;j<n;j++)
         {
             rsum=rsum+mat[i][j];
         }
         System.out.println("sum of "+(i+1)+"="+rsum);
     }
     int csum;
     for(j=0;j<n;j++)
     { csum=0;
       for(i=0;i<m;i++)
       {
           csum=csum+mat[i][j];
       }
       System.out.println("sum of "+(j+1)+"="+csum);
     }
 }
  void sald()
  {//sum above left diagnol
      int sum=0;
      for(i=0;i<m;i++)
     {
         for(j=0;j<n;j++)
         {
             if(i<=j)
                 sum=sum+mat[i][j];
         }
     }
      System.out.println("sum above main diagnol ="+sum);
  }
  void pald()
  {//print elements above left diagnol
      for(i=0;i<m;i++)
     {
         for(j=0;j<n;j++)
         {
             if((i+j)<=(n-1))
                 System.out.print(mat[i][j]+" ");
             else
                 System.out.print(" ");
         }
         System.out.println();
     }
  }
  void borderSum()
  {
      int sum=0;
      for(i=0;i<m;i++)
     {
         for(j=0;j<n;j++)
         {
             if(i==0||j==0||i==(n-1)||j==(m-1))
                 sum=sum+mat[i][j];
         }
     }
  }
  public static void main(String args[])
  {
   matrix obj=new matrix();
    obj.input();
    obj.display();
    obj.sums();
    obj.sald();
    obj.pald();
    obj.borderSum();
  }
}
