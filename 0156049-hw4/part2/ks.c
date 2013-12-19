#include<stdio.h>
#include<stdlib.h>
int main(int argc, char** argv){
	FILE *fp= fopen(argv[1],"r");
	FILE *output = fopen("tmpout","w");
	int da[4096];
	int db[4096];
	int i,j,count;
	char num[64]={'\0'},c;
	fgetc(fp);
	fgetc(fp);
	j=0;
	while( 1){
		c=fgetc(fp);
		for(i=0; c!=',' && c!=' '; c=fgetc(fp),i++){
//			getc(stdin);
			num[i] = c;
		}
		num[i] = '\0';
		da[j]=atoi(num);
		j++;
		if(c == ','){
			break;
		}
	}
	
	fgetc(fp);
	fgetc(fp);
	fgetc(fp);

	for(count=0;count<j;count++){
	c=fgetc(fp);
		for(i=0; c!=' ' && c!=EOF && c!='\n'; c=fgetc(fp),i++){
//			getc(stdin);
			num[i] = c;
		}
		num[i] = '\0';
		db[count]=atoi(num);
	}
	for(i=0;i<j;i++){
		if(da[i] < db[i]){
			fprintf(output,"%cA ",'A'+i);
		}
		else{
			fprintf(output,"%cB ",'A'+i);
		}
	}
	fclose(output);
	fclose(fp);




}






