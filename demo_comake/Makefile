###########################################################################
# Automatically generated by comake (1.0.1)  							  #
###########################################################################

#################设计系统参数#######################################
WORKROOT	?=	./
IDLCC	:=	$(WORKROOT)/public/idlcompiler/output/bin/mcy
RPCCC :=  $(WORKROOT)/public/ubrpc/output/bin/ubrpcgen
CC	:=	gcc
CXX	:=	g++
LEX	:=	flex
YACC	:= yacc
CFLAGS	:=	-pipe -Wall -W -g -fPIC
CXXFLAGS	:=	-pipe -Wall -W -g -fPIC
LEXFLAGS	:=	
YACCFLAGS	:=	
IDLFLAGS	:=  
LINKFLAGS	:=  -rdynamic
LINK	:=	g++
AR	:=	ar cqs
RANLIB	:=	
COMAKE	:=	comake

###############baidu lib 的32位 64位支持#################
HARDWARE_PLATFORM := $(shell uname -m)
ifeq ($(HARDWARE_PLATFORM),x86_64)
	lib2=lib2-64
	third=third-64
else
	lib2=lib2
	third=third
endif
##########################################

# 编译参数
DEP_INCPATH = 
DEP_LDFLAGS = 
DEP_LDLIBS = 
INCPATH =  -I.
MAKDEP = Makefile.dep


#start target
first : all

############# 默认推到公式
.SUFFIXES: .c .cpp .cc .cxx .C .idl .des
.PRECIOUS: %.cpp

.cpp.o:
	$(CXX) -c -o $@ $<  $(CXXFLAGS) $(CPPFLAGS) $(INCPATH)

.cc.o:
	$(CXX) -c -o $@ $<  $(CXXFLAGS) $(CPPFLAGS) $(INCPATH)

.cxx.o:
	$(CXX) -c -o $@ $<  $(CXXFLAGS) $(CPPFLAGS) $(INCPATH)

.C.o:
	$(CXX) -c -o $@ $<  $(CXXFLAGS) $(CPPFLAGS) $(INCPATH)

.c.o:
	$(CC) -c -o $@ $<  $(CFLAGS) $(CPPFLAGS) $(INCPATH)

.idl.cpp:
	$(IDLCC) --ns=$(*F) -o $* $< $(CPPFLAGS) $(INCPATH) $(IDLFLAGS)

#############
###cpp 支持
%info : %
	ccp $<
#############


#__$MAKEFILE_RULES$__



###############编译目标
all :  target output 
.PHONY : all clean test output comake src conf 

target : main 
#target : rpcidl main 
#target : 
#__$target_CMDLINE$__

rpcidl : 

clean_rpcidl : 


test : 	./test_main	


comake :
	-make clean
	-comake 

#-include $(MAKDEP)


#----------------build target : main--------------------

main : CC := gcc
main : CXX := g++
main : CXXFLAGS := -pipe -Wall -W -g -fPIC
main : CPPFLAGS := 
main : IDLFLAGS := 
main : CFLAGS := -pipe -Wall -W -g -fPIC
main : INCPATH :=  -I. $(DEP_INCPATH)
main : LDLIBS := -lcrypto -lm -lpthread $(DEP_LDLIBS)
main : LDFLAGS :=  $(DEP_LDFLAGS)
main : LINKFLAGS := -rdynamic

main_SOURCES := $(wildcard main.cpp)
#main_HEADERS := $(wildcard *.h)
main_HEADERS := *.h
main_IDLSRC := $(wildcard __$IDLSRC_VALUE$__)
main_IDLSRCCPP := $(patsubst %.idl,%.cpp, $(main_IDLSRC))
main_IDLSRCH := $(patsubst %.idl,%.h, $(main_IDLSRC))
main_CONFDES := $(wildcard __$CONFDES$_VALUE$__ main.des)
main_CONFRANGE := $(patsubst %.des,%.range, $(main_CONFDES))
main_OBJS := $(main_IDLSRC:.idl=.o)
main_OBJS += $(main_SOURCES:.c=.o)
main_OBJS := $(main_OBJS:.cc=.o)
main_OBJS := $(main_OBJS:.cpp=.o)
main_OBJS := $(main_OBJS:.cxx=.o)
main_OBJS := $(main_OBJS:.C=.o)
main_OBJS := $(main_OBJS:.idl=.o)
main_OBJS := $(main_OBJS:.yacc=.o)
main_OBJS := $(main_OBJS:.lex=.o)
main : $(main_OBJS) 
	@echo "force_clean"
	$(foreach n, $(wildcard ), $(if ifeq($(suffix $(n)), .c), $(CC) -c -o $(basename $(n)).o $(n) $(CXXFLAGS) $(CPPFLAGS) $(INCPATH);  , $(CXX) -c -o $(basename $(n)).o $(n) $(CXXFLAGS) $(CPPFLAGS) $(INCPATH); ))
	@`for x in $(main_CONFDES);do cpp -C -o main.range $$x $(CPPFLAGS) $(INCPATH);mkdir -p conf;cp main.range conf/; done`
	$(LINK) $^ -o $@ -Xlinker "-(" $(LDFLAGS) $(LDLIBS) $(LINKFLAGS) -Xlinker "-)"


define main_output
	mkdir -p output
	mkdir -p output/bin
	cp -rf main output/bin
	`if [ -e "conf" ];then cp -rf conf output/ ;fi`

endef
	

define main_clean
	-rm -rf $(main_OBJS) $(main_IDLSRCCPP) $(main_IDLSRCH) main.range conf/main.range
	-rm -rf main
	-rm -rf output
	-rm -rf ccp_output.error   ccp_output_scm.xml  ccp_output.xml ccp_output.pclint  ccp_output.txt
endef
	

define main_ccpc
	ccp $(main_SOURCES) --formatter vim
endef
	

define main_cov
	
endef
	



#---------------------end build target : main------------------

#----------------build target : test_main--------------------

test_main : CC := gcc
test_main : CXX := g++
test_main : CXXFLAGS := -pipe -Wall -W -g -fPIC
test_main : CPPFLAGS := 
test_main : IDLFLAGS := 
test_main : CFLAGS := -pipe -Wall -W -g -fPIC
test_main : INCPATH :=  -I. $(DEP_INCPATH)
test_main : LDLIBS := -lcrypto -lm -lpthread $(DEP_LDLIBS)
test_main : LDFLAGS :=  $(DEP_LDFLAGS)
test_main : LINKFLAGS := -rdynamic

test_main_SOURCES := $(wildcard test.cpp)
#test_main_HEADERS := $(wildcard *.h)
test_main_HEADERS := *.h
test_main_IDLSRC := $(wildcard __$IDLSRC_VALUE$__)
test_main_IDLSRCCPP := $(patsubst %.idl,%.cpp, $(test_main_IDLSRC))
test_main_IDLSRCH := $(patsubst %.idl,%.h, $(test_main_IDLSRC))
test_main_CONFDES := $(wildcard __$CONFDES$_VALUE$__ test_main.des)
test_main_CONFRANGE := $(patsubst %.des,%.range, $(test_main_CONFDES))
test_main_OBJS := $(test_main_IDLSRC:.idl=.o)
test_main_OBJS += $(test_main_SOURCES:.c=.o)
test_main_OBJS := $(test_main_OBJS:.cc=.o)
test_main_OBJS := $(test_main_OBJS:.cpp=.o)
test_main_OBJS := $(test_main_OBJS:.cxx=.o)
test_main_OBJS := $(test_main_OBJS:.C=.o)
test_main_OBJS := $(test_main_OBJS:.idl=.o)
test_main_OBJS := $(test_main_OBJS:.yacc=.o)
test_main_OBJS := $(test_main_OBJS:.lex=.o)
test_main : $(test_main_OBJS) 
	@echo "force_clean"
	$(foreach n, $(wildcard ), $(if ifeq($(suffix $(n)), .c), $(CC) -c -o $(basename $(n)).o $(n) $(CXXFLAGS) $(CPPFLAGS) $(INCPATH);  , $(CXX) -c -o $(basename $(n)).o $(n) $(CXXFLAGS) $(CPPFLAGS) $(INCPATH); ))
	@`for x in $(test_main_CONFDES);do cpp -C -o test_main.range $$x $(CPPFLAGS) $(INCPATH);mkdir -p conf;cp test_main.range conf/; done`
	$(LINK) $^ -o $@ -Xlinker "-(" $(LDFLAGS) $(LDLIBS) $(LINKFLAGS) -Xlinker "-)"


define test_main_output
	
endef
	

define test_main_clean
	-rm -rf $(test_main_OBJS) $(test_main_IDLSRCCPP) $(test_main_IDLSRCH) test_main.range conf/test_main.range
	-rm -rf test_main
	-rm -rf output
	-rm -rf ccp_output.error   ccp_output_scm.xml  ccp_output.xml ccp_output.pclint  ccp_output.txt
endef
	

define test_main_ccpc
	ccp $(test_main_SOURCES) --formatter vim
endef
	

define test_main_cov
	
endef
	



#---------------------end build target : test_main------------------

define _output
	$(main_output)
	$(test_main_output)
endef
	

define _clean
	$(main_clean)
	$(test_main_clean)
endef
	

ccpc : 
	$(main_ccpc)
	$(test_main_ccpc)

cov : 
	cov01 -1
	make clean
	make 
	cov01 -0



output : main 
	$(_output)
	rm -rf $(MAKDEP)

$(MAKDEP) : $(wildcard comake_autogen.cpp main.cpp test.cpp)
	-$(CC) -MG -MM $(CPPFLAGS) $(INCPATH) $(DEP_INCPATH) $^ > $@

clean:
	$(_clean)
	rm -rf $(MAKDEP)


