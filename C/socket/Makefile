TARGET = adress client uecho_server uecho_client info echo_server echo_client

all: ${TARGET}

adress: adress.o
	cc -o $@ $<

client: client.o
	cc -o $@ $<

uecho_server: uecho_sever.o
	cc -o $@ $<

uecho_client: uecho_client.o
	cc -o $@ $<

info: info.o
	cc -o $@ $<

echo_server: echo_server.o
	cc -o $@ $<

echo_client: echo_client.o
	cc -o $@ $<

clean:
	rm -rf ${TARGET}
	rm -rf *.o
