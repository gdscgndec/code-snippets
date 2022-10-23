import java.util.*;
public class Factorial {
    public static void main(String[] args) {
        int a;
        Scanner s=new Scanner(System.in);
        System.out.print("Enter number whose factorial you want to find : ");
        a=s.nextInt();
        int fact=1;
        for(int i=1;i<=a;i++){
            fact=fact*i;
        }
        System.out.println("Factorial is : "+fact);
        s.close();
    }
}