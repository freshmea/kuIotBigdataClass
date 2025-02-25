TARGET = adress client uecho_server uecho_client

all: ${TARGET}

adress: adress.o
	cc -o $@ $<

client: client.o
	cc -o $@ $<

uecho_server: uecho_sever.o
	cc -o $@ $<

uecho_client: uecho_client.o
	cc -o $@ $<

clean:
	rm -rf ${TARGET}
	rm -rf *.o
