#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<string.h>

void* thread_main(void* arg);

int main(int argc, char* argv[]){
    
    pthread_t t_id;
    int thread_param = 5;
    void* thr_ret;

    if(pthread_create(&t_id,NULL,thread_main,(void*)&thread_param)!=0){
        puts("pthread_create() error");
        return -1;
    }
    // thread가 종료될때까지 대기(blocking function)
    pthread_join(t_id, &thr_ret);          

    printf("Thread return message: %s \n",(char*)thr_ret);
    free(thr_ret);
    return 0;
}



void* thread_main(void* arg){

    int i;
    int cnt= *((int*)arg);
    char* msg=(char*)malloc(sizeof(char)*50);
    strcpy(msg, "Hello, I'm thread");
    for(i=0;i<cnt;++i){
        sleep(1);
        puts("running thread...");
    }
    return (void*)msg;
}
