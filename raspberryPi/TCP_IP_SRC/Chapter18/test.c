#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<string.h>

struct adder
{
    int op1;
    int op2;
    int result;
}adder;

void* thread_add(void* arg);

int main(int argc, char* argv[]){

    struct adder tmp;
    tmp.op1 = 10;
    tmp.op2 = 20;
    pthread_t t_id;
    void* thr_ret;

    if(pthread_create(&t_id,NULL,thread_add,(void*)&tmp)!=0){
        puts("pthread_create() error");
        return -1;
    }
    // thread가 종료될때까지 대기(blocking function)
    pthread_join(t_id, &thr_ret);          

    printf("result: %d \n",tmp.result);
    return 0;
}

void* thread_add(void* arg){
    struct adder *op = (struct adder*)arg;

    arg-

    return NULL;
}