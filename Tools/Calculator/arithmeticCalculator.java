/*
A simple arithmetic calculator using java language

Silky1099
*/

import java.util.*;

public class arithmeticCalculator {
    public static void calc(int a, char op, int b) {
        switch (op) {
            case '+':
                System.out.println(a + b);
                return;
            case '-':
                System.out.println(a - b);
                return;
            case '*':
                System.out.println(a * b);
                return;
            case '/':
                System.out.println(a / b);
                return;
            default:
                System.out.println("Enter a valid operator!!!");
                main(null);
        }

    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter two numbers: ");
            int x = sc.nextInt(), y = sc.nextInt();
            System.out.println("Enter the operation to be performed: (+ - * /)");
            char op = sc.next().charAt(0);
            calc(x, op, y);
        }
    }
}
