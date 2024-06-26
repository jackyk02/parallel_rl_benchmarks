#ifndef _LEARNERREACTOR_H
#define _LEARNERREACTOR_H
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
#line 153 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
typedef generic_port_instance_struct _learnerreactor_dataset_t;
#line 152 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
typedef generic_port_instance_struct _learnerreactor_gradients_t;
typedef struct {
    struct self_base_t base;
    char *_lf_name;
    PyObject* _lf_py_reaction_function_0;
    PyObject* _lf_py_reaction_function_1;
    
    #line 155 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    PyObject* start_time;
    #line 156 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    PyObject* q_net_state;
    #line 157 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    PyObject* round;
    #line 153 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    _learnerreactor_dataset_t* _lf_dataset;
    #line 153 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    // width of -2 indicates that it is not a multiport.
    #line 153 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    int _lf_dataset_width;
    #line 153 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    // Default input (in case it does not get connected)
    #line 153 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    _learnerreactor_dataset_t _lf_default__dataset;
    #line 152 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    _learnerreactor_gradients_t _lf_gradients;
    #line 152 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    int _lf_gradients_width;
    #line 159 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    reaction_t _lf__reaction_0;
    #line 167 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    reaction_t _lf__reaction_1;
    trigger_t _lf__startup;
    reaction_t* _lf__startup_reactions[1];
    #line 153 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    trigger_t _lf__dataset;
    #line 153 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    reaction_t* _lf__dataset_reactions[1];
    #ifdef FEDERATED
    
    #endif // FEDERATED
} _learnerreactor_self_t;
_learnerreactor_self_t* new__learnerreactor();
#endif // _LEARNERREACTOR_H
