#include<stdio.h>
#include<conio.h>
void check(char,char);
char a[9]={'1','2','3','4','5','6','7','8','9'};
void gameName(){
    printf("\n\t\t\t\t\t Tic Tac Toe Game\n");
}
void show(){
    printf("\n\n\t\t\t---|---|---\n");
    printf("\t\t\t %c | %c | %c\n",a[0],a[1],a[2]);
    printf("\t\t\t---|---|---\n");
    printf("\t\t\t %c | %c | %c\n",a[3],a[4],a[5]);
    printf("\t\t\t---|---|---\n");
    printf("\t\t\t %c | %c | %c\n",a[6],a[7],a[8]);
    printf("\t\t\t---|---|---\n");
}
void inputSymbol(){
    printf("\nplayer 1 symbol: x");
    printf("\nplayer 2 symbol: 0");

}
void start(){
    char player;
    printf("\nWhich player will start the game?Player 1 or Player 2:");
    scanf("%d",&player);

}

int count=0;//count is declared globally
void play (){  //take two input 1.position of symbol to insert 2.players symbol
char pos,sym;
printf("Enter symbol of player:\n");//repeat taking this i/p until a player wins a game or match becomes draw
fflush(stdin);
scanf("%c",&sym);

printf("Enter position of symbol:\n");
fflush(stdin);
scanf("%c",&pos);
count++;
check(pos,sym);//this func has store particulr sym in array a[9] at particulr pos

}

void check(char pos,char sym){
    int i;
    for(i=0;i<=8;i++){
        if (a[i]==pos){
            a[i]=sym;//This time it will print symbol at the given position

        }

    }
}

int end(){
    if((a[0]=='x' && a[1]=='x' && a[2]=='x')||(a[0]=='x' && a[4]=='x' && a[8]=='x')||(a[0]=='x' && a[3]=='x' && a[6]=='x'))
            return 1;
    else if((a[0]=='0' && a[1]=='0' && a[2]=='0')||(a[0]=='0' && a[4]=='0' && a[8]=='0')||(a[0]=='0' && a[3]=='0' && a[6]=='0'))
            return 2;
   else if(a[1]=='x' && a[4]=='x' && a[7]=='x')
            return 1;
    else if(a[1]=='0' && a[4]=='0' && a[7]=='0')
            return 2;
    else if(a[2]=='x' && a[5]=='x' && a[8]=='x')  
            return 1;
    else if(a[2]=='0' && a[5]=='0' && a[8]=='0')  
            return 2;
    else if(a[3]=='x' && a[4]=='x' && a[5]=='x')  
            return 1;
    else if(a[3]=='0' && a[4]=='0' && a[5]=='0')  
            return 2;
    else if(a[2]=='x' && a[4]=='x' && a[6]=='x')  
            return 1;
    else if(a[2]=='0' && a[4]=='0' && a[6]=='0')  
            return 2;      
    else if(a[6]=='x' && a[7]=='x' && a[8]=='x')  
            return 1;
    else if(a[6]=='0' && a[7]=='0' && a[8]=='0')  
            return 2;
    else
            return 3;    
    
}
int main(){
    int k;
    char ch;
    labell:
    gameName();
    show();
    inputSymbol();
    start();
    play();
    //system("cls");
     label:
    //show();
    play();

    k=end();
    show();
    if(count<9)
    {
     if(k==1){
       printf("\n player 1 won");
       count=0;
     }
     else if(k==2){
       printf("\n player 2 won");
       count=0;//count ko vapas zero karna pdega even if any player wins or it is draw
     }
     else
       goto label;
    }
    else{
        printf("\nGame draw");
        count=0;
    }
    
    printf("\nDo you want to continue?:Enter Y for YES and N for NO");
    fflush(stdin);
    scanf("%c",&ch);
    if(ch=='Y' || ch=='y'){
    a[0]='1';
    a[1]='2';
    a[2]='3';
    a[3]='4';
    a[4]='5';
    a[5]='6';
    a[6]='7';
    a[7]='8';
    a[8]='9';

    goto labell;

    }
getch();
}