CXX = g++
CXXFLAGS = -std=c++14 -Wall -g -MMD
EXEC = chess
OBJECTS = main.o board.o move.o
DEPENDS = ${OBJECTS:.o=.d}

${EXEC}: ${OBJECTS}
	${CXX} ${CXXFLAGS} ${OBJECTS} -o ${EXEC} 
-include ${DEPENDS}


.PHONY: clean

clean:
	rm ${OBJECTS} ${EXEC} ${DEPENDS}
