#include<unistd.h>
#include<stdio.h>
#include<pthread.h>     // posix
void* thread_main1(void* arg);
// void* thread_main2(void* arg);

int main(int argc, char* argv[]){

    pthread_t t_id;
    pthread_t t_id2;
    int thread_param=5;
    int thread_param2=5;

    if(pthread_create(&t_id, NULL, thread_main1,(void*)&thread_param)!=0){
        puts("pthread_create() error");
        return -1;
    }
    // if(pthread_create(&t_id2, NULL, thread_main2,(void*)&thread_param2)!=0){
    //     puts("pthread_create() error");
    //     return -1;
    // }
    sleep(3);
    puts("end of main");
    return 0;
}

void* thread_main1(void* arg){

    int i;
    int cnt= *((int*)arg);
    for(i=0;i<cnt;++i){
        sleep(1);
        printf("running thread...1: count: %d\n",i+1);
    }
    return NULL;
}

// void* thread_main2(void* arg){

//     int i;
//     int cnt= *((int*)arg);
//     for(i=0;i<cnt;++i){
//         sleep(2);
//         printf("running thread...2: count: %d\n", i+1);
//     }
//     return NULL;
// }