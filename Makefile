
all: selfrep 

selfrep : selfrep.c
	gcc  $< -g -o $@ 

rep: rep.c
	gcc $< -g -o $@ 

clean:
	rm -f loxstub loxctl *.o *.out *~ 
