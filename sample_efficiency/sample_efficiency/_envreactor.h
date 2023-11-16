#ifndef _ENVREACTOR_H
#define _ENVREACTOR_H
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
#line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
typedef generic_port_instance_struct _envreactor_seed_t;
#line 17 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
typedef generic_port_instance_struct _envreactor_infos_t;
typedef struct {
    struct self_base_t base;
    char *_lf_name;
    PyObject* _lf_py_reaction_function_0;
    PyObject* _lf_py_reaction_function_1;
    
    
    #line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    _envreactor_seed_t* _lf_seed;
    #line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    // width of -2 indicates that it is not a multiport.
    #line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    int _lf_seed_width;
    #line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    // Default input (in case it does not get connected)
    #line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    _envreactor_seed_t _lf_default__seed;
    #line 17 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    _envreactor_infos_t _lf_infos;
    #line 17 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    int _lf_infos_width;
    #line 19 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    reaction_t _lf__reaction_0;
    #line 24 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    reaction_t _lf__reaction_1;
    trigger_t _lf__startup;
    reaction_t* _lf__startup_reactions[1];
    #line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    trigger_t _lf__seed;
    #line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    reaction_t* _lf__seed_reactions[1];
    #ifdef FEDERATED
    
    #endif // FEDERATED
} _envreactor_self_t;
_envreactor_self_t* new__envreactor();
#endif // _ENVREACTOR_H
