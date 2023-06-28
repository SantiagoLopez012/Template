#include "HelloWorld_py.h"

void hello_world_py(){
	hello_world();
}

void allo_py(std::string &S){
	allo(S);
}

void init_module(py::module &M){
	M.def("hello_world", &hello_world_py, "Hello World!");
	M.def("allo", &allo_py, "S"_a, "Prints S");	
}

PYBIND11_MODULE(libHelloWorld, M){
	init_module(M);
}