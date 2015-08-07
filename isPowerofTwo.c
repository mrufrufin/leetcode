#include <stdio.h>
typedef enum { false, true } bool;
bool isPowerOfTwo(int n) {
	    while((n > 1 )&& ((n & 1) == 0)){
			        n >>=1;
					    };

		    return (n==1);

}

int main(int argc, char * argv[]){
int n = atoi(argv[1]);
bool is2toX = isPowerOfTwo(n);
printf("%d\n", is2toX);
return 0;
};
