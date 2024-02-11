#include <sys/sysmacros.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

#define handle_error(msg) \
          do { perror(msg); exit(EXIT_FAILURE); } while (0)
 
int test_signal(sigset_t * set, int signal){
 int rt = sigismember(set,signal);
 
 if ( rt == -1){
   fprintf(stderr, "Error sigismember() signal %d", signal);
   exit(EXIT_FAILURE);
 }
 return rt;
}

void add_signal2set(sigset_t * set, int signal){
 
 if( sigaddset(set, signal) == -1 ){
   fprintf(stderr, "Error sigaddset() signal %d", signal);
   exit(EXIT_FAILURE);
 }
}
 
int main(){
 
   sigset_t block_signals, pending_signals;
 
   if(sigemptyset(&block_signals) == -1) handle_error("Error in sigemptyset()");
 
   add_signal2set(&block_signals, SIGINT ); // Control + C
   add_signal2set(&block_signals, SIGTSTP); // Control + Z
 
   if( sigprocmask(SIG_BLOCK, &block_signals, NULL) == -1) handle_error("Error in sigprocmask()");
 
 
   char * val = getenv("SLEEP_SECS");
   if ( val == NULL) handle_error("Error getting env variable : SLEEP_SECS");
 
   int segs = atoi(val);
 
   if(segs == 0) handle_error("Invalid seconds to sleep");
 
   printf("Sleeping %d seconds\n", segs);
 
   sleep(segs);
 
   if ( sigpending(&pending_signals) == -1)handle_error("Error in sigpending()");
 
   if( test_signal(&pending_signals, SIGINT)){
     printf("\nSignal  SIGINT recived\n");
   }
 
   if( test_signal(&pending_signals, SIGTSTP)){
      printf("\nSignal SIGTSTP recived\n");
 
      sigset_t stop_signal; // Se crea para que solo desbloque la señal  stop.
      if(sigemptyset(&stop_signal) == -1) handle_error("Error in sigemptyset()");
     
      add_signal2set(&stop_signal, SIGTSTP);
      sigprocmask(SIG_UNBLOCK, &stop_signal, NULL);
   }
 
   printf("Ending program\n");
 
 
   return 0;
}