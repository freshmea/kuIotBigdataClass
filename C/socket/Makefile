TARGET = adress client

all: ${TARGET}

adress: adress.o
	cc -o $@ $<

client: client.o
	cc -o $@ $<

clean:
	rm -rf ${TARGET}
	rm -rf *.o
