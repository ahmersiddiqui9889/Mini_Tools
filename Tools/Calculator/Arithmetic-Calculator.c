/*
This program can be used to perform the most basic arithmetic operations (addition, subtraction, multiplication, division) on two digits

by Silky1099
*/

#include<stdio.h>
#include<conio.h>
int main(){
    float a,b;
    char o;
    clrscr();
    printf("Enter the operator(+,-,*,/): ");
    scanf("%c",&o);
    printf("Enter the first and second numbers: ");
    scanf("%f %f",&a,&b);
    switch (o){
        case '+':
            printf("%f",a + b);
            break;
        case '-':
            printf("%f",a - b);
            break;
        case '*':
            printf("%f",a * b);
            break;
        case '/':
            printf("%f",a / b);
            break;
        default:
            printf("You entered a wrong operator!");
    }
    getch();
    return 0;
}
