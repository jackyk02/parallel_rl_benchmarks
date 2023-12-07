#ifndef _CLIENTREACTOR_H
#define _CLIENTREACTOR_H
#include <limits.h>
#include "include/core/platform.h"
#include "include/api/api.h"
#include "include/core/reactor.h"
#include "include/core/reactor_common.h"
#include "include/core/threaded/scheduler.h"
#include "include/core/mixed_radix.h"
#include "include/core/port.h"
#include "include/core/environment.h"
int lf_reactor_c_main(int argc, const char* argv[]);
#include "pythontarget.h"
#include "include/core/reactor.h"
#include <limits.h>
#include "include/core/platform.h"
#include "include/api/api.h"
#include "include/core/reactor.h"
#include "include/core/reactor_common.h"
#include "include/core/threaded/scheduler.h"
#include "include/core/mixed_radix.h"
#include "include/core/port.h"
#include "include/core/environment.h"
int lf_reactor_c_main(int argc, const char* argv[]);
#include "pythontarget.h"
#line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
typedef generic_port_instance_struct _clientreactor_global_parameters_t;
#line 12 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
typedef generic_port_instance_struct _clientreactor_updated_parameters_t;
typedef struct {
    struct self_base_t base;
    char *_lf_name;
    PyObject* _lf_py_reaction_function_0;
    PyObject* _lf_py_reaction_function_1;
    
    
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    _clientreactor_global_parameters_t* _lf_global_parameters;
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    // width of -2 indicates that it is not a multiport.
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    int _lf_global_parameters_width;
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    // Default input (in case it does not get connected)
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    _clientreactor_global_parameters_t _lf_default__global_parameters;
    #line 12 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    _clientreactor_updated_parameters_t _lf_updated_parameters;
    #line 12 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    int _lf_updated_parameters_width;
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    reaction_t _lf__reaction_0;
    #line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    reaction_t _lf__reaction_1;
    trigger_t _lf__startup;
    reaction_t* _lf__startup_reactions[1];
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    trigger_t _lf__global_parameters;
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    reaction_t* _lf__global_parameters_reactions[1];
    #ifdef FEDERATED
    
    #endif // FEDERATED
} _clientreactor_self_t;
_clientreactor_self_t* new__clientreactor();
#endif // _CLIENTREACTOR_H
