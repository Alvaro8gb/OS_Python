# Define the C compiler to use
CC = gcc

# Define any compile-time flags
CFLAGS = -Wall -g

# Define the C source files
SRCS = signal_set.c signal_set_customize.c

# Define the C object files 
OBJS = $(SRCS:.c=.o)

# Define the executable files
EXECS = $(SRCS:.c=)

# The following part of the Makefile is generic; it can be used to 
# build any executable just by changing the definitions above

all:    $(EXECS)

$(EXECS): % : %.o
	$(CC) $(CFLAGS) -o $@ $<

.c.o:
	$(CC) $(CFLAGS) -c $<  -o $@

# Clean old builds
clean:
	rm -f *.o *~ $(EXECS)

# Define a phony target to avoid problems with local files named 'clean'
.PHONY: clean

var-env:
	export SLEEP_SECS=10