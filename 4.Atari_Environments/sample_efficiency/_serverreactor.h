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
#line 37 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
typedef generic_port_instance_struct _serverreactor_infos_t;
#line 36 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
typedef generic_port_instance_struct _serverreactor_seed_t;
typedef struct {
    struct self_base_t base;
    char *_lf_name;
    PyObject* _lf_py_reaction_function_0;
    PyObject* _lf_py_reaction_function_1;
    
    #line 38 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    PyObject* step_num;
    #line 39 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    PyObject* start_time;
    #line 37 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    // Multiport input array will be malloc'd later.
    #line 37 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    _serverreactor_infos_t** _lf_infos;
    #line 37 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    int _lf_infos_width;
    #line 37 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    // Default input (in case it does not get connected)
    #line 37 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    _serverreactor_infos_t _lf_default__infos;
    #line 37 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    // Struct to support efficiently reading sparse inputs.
    #line 37 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    lf_sparse_io_record_t* _lf_infos__sparse;
    #line 36 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    _serverreactor_seed_t _lf_seed;
    #line 36 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    int _lf_seed_width;
    #line 41 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    reaction_t _lf__reaction_0;
    #line 46 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    reaction_t _lf__reaction_1;
    trigger_t _lf__startup;
    reaction_t* _lf__startup_reactions[1];
    #line 37 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    trigger_t _lf__infos;
    #line 37 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_efficiency.lf"
    reaction_t* _lf__infos_reactions[1];
    #ifdef FEDERATED
    trigger_t* _lf__infos_network_port_status;
    
    #endif // FEDERATED
} _serverreactor_self_t;
_serverreactor_self_t* new__serverreactor();
#endif // _SERVERREACTOR_H
