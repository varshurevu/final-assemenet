#include<stdio.h>
#include<conio.h>
int main()
{
    write();
    depread();
}

struct department
{
    char did[20];
    char dname[30];

};
struct admin
{
    struct department dp[3];
}ad;

void depread()
{
FILE *fptr ;
fptr=fopen("deptext.txt","r");
if(fptr==NULL)
{
    printf(stderr,"\n enter deptext.txt\n");
    exit(1);
}
int i=0;
printf("\n student details are\n");
printf(".sid..\t..sname .......");
printf("\n...............\n");

for(i=0;i<2;++i)
{
    fscanf(fptr,"%s %s\n",&ad.dp[i].did,&ad.dp[i].dname);
    printf("\t %s",ad.dp[i].did);
    printf("\t %s\n",ad.dp[i].dname);
}
while(fwrite(&ad,sizeof(struct admin),1,fptr))
{
    printf("did=%s dname=%s",&ad.dp[i].did,&ad.dp[i].dname);
}

fclose(fptr);

}
void write()
{
struct admin ad;
FILE *fptr ;
fptr=fopen("deptext.txt","w");
if(fptr==NULL)
{
    printf(stderr,"\n enter deptext.txt\n");
    exit(1);
}
//printf("\n student details are  \n");
//printf(".did  dname.......");
printf("\n=============================\n");
int i;
printf("enter the student details :\n ");
for(i=0;i<1;i++)
{
    printf("\n student  id:");
    scanf("%s",ad.dp[i].did);
    printf("\n student  name:");
    scanf("%s",ad.dp[i].dname);
}
fwrite(&ad, sizeof(struct admin), 1, fptr);

fclose(fptr);
}


