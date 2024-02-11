#include <sys/sysmacros.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
 
#define handle_error(msg) \
          do { perror(msg); exit(EXIT_FAILURE); } while (0)
          
volatile int N_SIGINT = 0;
volatile int N_SIGTSTP = 0;
 
static void handler(int signal){
 
   if(signal == SIGINT ){
        N_SIGINT +=1;
   }
 
   if(signal == SIGTSTP ){
        N_SIGTSTP +=1;
   }
    
}

void add_signal2set(sigset_t * set, int signal){
 
 if( sigaddset(set, signal) == -1 ){
   fprintf(stderr, "Error sigaddset() signal %d", signal);
   exit(EXIT_FAILURE);
 }
}
 
int main(){
 
   sigset_t block_signals;
 
   if(sigemptyset(&block_signals) == -1) handle_error("Error in sigemptyset()");
   add_signal2set(&block_signals, SIGINT );
   add_signal2set(&block_signals, SIGTSTP);
 
   struct sigaction sa;

   sa.sa_flags = SA_SIGINFO;
   if(sigemptyset(&sa.sa_mask) == -1) handle_error("Error in sigemptyset()");
   sa.sa_handler = (void *)  handler;
  
   if (sigaction(SIGINT, &sa, NULL) == -1) handle_error("Error in sigaction(SIGINT)");
   if (sigaction(SIGTSTP, &sa, NULL) == -1) handle_error("Error in sigaction(SIGTSTP)");
 
   while (N_SIGINT + N_SIGTSTP < 10 ){
      sigsuspend(&sa.sa_mask);
   }

   if ( sigprocmask(SIG_BLOCK, &block_signals, NULL) == -1) handle_error("Error in sigaction(SIGTSTP)");
 
   printf("\nNumber of SIGINT: %d\n", N_SIGINT);
   printf("Number of SIGTSTP: %d\n", N_SIGTSTP);
 
   return 0;
}