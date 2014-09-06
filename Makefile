CC=gcc
CFLAGS=-Wall -Werror -g
LDFLAGS=-lm

ALL=multi_of_3n5

all: $(ALL)

multi_of_3n5: multi_of_3n5.o
	$(CC) $(LDFLAGS) -o $@ $^

multi_of_3n5.o: multi_of_3n5.c
	$(CC) $(CLFAGS) -c $<

clean:
	rm -rf core* *.o *.gch $(ALL)
