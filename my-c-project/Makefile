CC = gcc
CFLAGS = -Iinclude `sdl2-config --cflags`
LDLIBS = `sdl2-config --libs` -lSDL2_ttf
SRC = src/main.c src/utils.c src/tetris.c
OBJ = $(SRC:.c=.o)
EXEC = my-c-project

all: $(EXEC)

$(EXEC): $(OBJ)
	$(CC) -o $@ $^ $(LDLIBS)

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f $(OBJ) $(EXEC)
