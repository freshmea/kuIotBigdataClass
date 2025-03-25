#include<unistd.h>
#include<stdio.h>
#include<pthread.h>     // posix
#include<semaphore.h>

// set thread
void* thread_main1(void* arg);
void* thread_main2(void* arg);
void* thread_main3(void* arg);

//set semaphore
static sem_t sem_one;
static sem_t sem_two;
static sem_t sem_three;
static int num;

int main(int argc, char* argv[]){

    pthread_t t_id1, t_id2, t_id3;

    // semaphore init
    sem_init(&sem_one,0,0);
    sem_init(&sem_two,0,1);
    sem_init(&sem_three,0,2);

    // set pthread
    if(pthread_create(&t_id1, NULL, thread_main1,NULL)!=0){
        puts("pthread_create() error");
        return -1;
    }
    if(pthread_create(&t_id2, NULL, thread_main2,NULL)!=0){
        puts("pthread_create() error");
        return -1;
    }
    if(pthread_create(&t_id3, NULL, thread_main3,NULL)!=0){
        puts("pthread_create() error");
        return -1;
    }

    // stay pthread for main
    pthread_join(t_id1, NULL);
    pthread_join(t_id2, NULL);
    pthread_join(t_id3, NULL);
    
    // semaphore destory
    sem_destroy(&sem_one);
    sem_destroy(&sem_two);
    sem_destroy(&sem_three);

    sleep(5); puts("end of main");
    return 0;
}

  

// pthread fuction

void* thread_main1(void* arg){
    int i;
    for(i=0;i<5;++i){
        sleep(1);
        sem_wait(&sem_one);
        printf("running thread...1\n");
        sem_post(&sem_three);
    }
    return NULL;
}

void* thread_main2(void* arg){
    int i;
    for(i=0;i<5;++i){
        sleep(1);
        sem_wait(&sem_two);
        printf("running thread...2\n");
        sem_post(&sem_one);
    }
    return NULL;
}

void* thread_main3(void* arg){
    int i;
    for(i=0;i<5;++i){
        sleep(1);
        sem_wait(&sem_three);
        printf("running thread...3\n");
        sem_post(&sem_two);
    }
    return NULL;
}