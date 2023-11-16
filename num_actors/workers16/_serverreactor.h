#ifndef _SERVERREACTOR_H
#define _SERVERREACTOR_H
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
#line 25 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
typedef generic_port_instance_struct _serverreactor_updated_parameters_t;
#line 24 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
typedef generic_port_instance_struct _serverreactor_global_parameters_t;
typedef struct {
    struct self_base_t base;
    char *_lf_name;
    PyObject* _lf_py_reaction_function_0;
    PyObject* _lf_py_reaction_function_1;
    
    #line 26 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    PyObject* round_num;
    #line 27 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    PyObject* benchmark_start_time;
    #line 28 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    PyObject* total_start_time;
    #line 25 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    // Multiport input array will be malloc'd later.
    #line 25 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    _serverreactor_updated_parameters_t** _lf_updated_parameters;
    #line 25 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    int _lf_updated_parameters_width;
    #line 25 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    // Default input (in case it does not get connected)
    #line 25 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    _serverreactor_updated_parameters_t _lf_default__updated_parameters;
    #line 25 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    // Struct to support efficiently reading sparse inputs.
    #line 25 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    lf_sparse_io_record_t* _lf_updated_parameters__sparse;
    #line 24 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    _serverreactor_global_parameters_t _lf_global_parameters;
    #line 24 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    int _lf_global_parameters_width;
    #line 30 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    reaction_t _lf__reaction_0;
    #line 39 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    reaction_t _lf__reaction_1;
    trigger_t _lf__startup;
    reaction_t* _lf__startup_reactions[1];
    #line 25 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    trigger_t _lf__updated_parameters;
    #line 25 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers16.lf"
    reaction_t* _lf__updated_parameters_reactions[1];
    #ifdef FEDERATED
    trigger_t* _lf__updated_parameters_network_port_status;
    
    #endif // FEDERATED
} _serverreactor_self_t;
_serverreactor_self_t* new__serverreactor();
#endif // _SERVERREACTOR_H
