#include <stdio.h>

int main()
{
    int a, b, e,f,i;
    float c, d,g;
    

    printf(" ------------------------------------------\n");
    printf("|         KNOW YOUR ELECTRICITY BILL       |\n ");
    printf("------------------------------------------\n\n");
    printf("Welcome to the most reliable electricity bill calculator \nwhich takes meter unit as input and displays the Bill amount\n\n");
    printf("This bill calculator shows the bill amount for both URBAN and RURAL areas\nconsumed in a month of 30 days\n\n");
    printf("CHOOSE 1 FOR URBAN CITIES\n");
    printf("CHOOSE 2 FOR RURAL AND OTHER CITIES\n");
    printf("CHOOSE 3 TO EXIT\n\n");
    scanf("%d", &a);
    
        if (a == 1)
        {
            printf("CHOOSE YOUR CITY:-\n");
            printf("1.CHENNAI\n2.NEWDELHI\n3.KOLKATA\n4.MUMBAI\n5.BANGLORE\n\n\n");
            scanf("%d", &b);

            if (b == 1 || b == 2 || b == 3 || b == 4 || b == 5)
            {

                printf("ENTER THE PREVIOUS UNIT METER READING:");
                scanf("%f", &c);
                printf("ENTER THE CURRENT UNIT METER READING:");
                scanf("%f", &d);
                printf("\n");
                g = d - c;
                printf("TOTAL UNIT CONSUMED IN A MONTH: %.2fkwh\n\n", g);
                printf("ENTER 1 IF THE VALUES ARE CORRECT");
                printf("ENTER 2 TO EXIT");
                scanf("%d", &e);
                if (e == 1) {
                    printf("\n");
                    printf("CURRENT RATE OF ELECTRICITY PER UNIT 7.05 INR\n");
                    printf("GST INCLUDED 5 PERCENT\n\n");
                    g = (g * 7.05) + (5 / 100);
                    printf("-------------------------------------------\n");
                    printf("|TOTAL BILL AMOUNT INCLUDING TAX:%.2fINR| \n", g);
                    printf("-------------------------------------------\n");
                    printf("\n");
                    printf("WE ARE PLEASED TO SERVE YOU");
                }
                else {
                    printf("THANK YOU VISIT AGAIN....");
                }
            }
        }
        else if (a == 2)
        {
            printf("ALL THE RURAL CITIES HAVE A FIXED UNIT RATE OF 6.07INR\n\n");
            printf("ENTER THE PREVIOUS UNIT METER READING:");
            scanf("%f", &c);
            printf("ENTER THE CURRENT UNIT METER READING:");
            scanf("%f", &d);
            printf("\n");
            g = d - c;
            printf("TOTAL UNIT CONSUMED IN A MONTH: %.2fkwh\n\n", g);
            printf("ENTER 1 IF THE VALUES ARE CORRECT");
            printf("ENTER 2 TO EXIT");
            scanf("%d", &e);
            if (e == 1) {
                printf("\n");
                printf("CURRENT RATE OF ELECTRICITY PER UNIT  6.07INR\n");
                printf("GST INCLUDED 5 PERCENT\n\n");
                g = (g * 6.07) + (5 / 100);
                printf("-------------------------------------------\n");
                printf("|TOTAL BILL AMOUNT INCLUDING TAX:%.2fINR| \n", g);
                printf("-------------------------------------------\n");
                printf("\n");
                printf("WE ARE PLEASED TO SERVE YOU");
            }
            else {
                printf("THANK YOU VISIT AGAIN....");
            }
        }
        
        else {
            printf("THANK YOU VISIT AGAIN....");
        }
    
    return 0;
}