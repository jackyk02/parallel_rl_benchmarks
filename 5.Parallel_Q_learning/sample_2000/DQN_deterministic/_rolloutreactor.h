#ifndef _ROLLOUTREACTOR_H
#define _ROLLOUTREACTOR_H
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
#line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
typedef generic_port_instance_struct _rolloutreactor_gradients_t;
#line 82 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
typedef generic_port_instance_struct _rolloutreactor_trajectories_t;
typedef struct {
    struct self_base_t base;
    char *_lf_name;
    PyObject* _lf_py_reaction_function_0;
    PyObject* _lf_py_reaction_function_1;
    
    #line 84 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    PyObject* env;
    #line 85 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    PyObject* obs;
    #line 86 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    PyObject* q_net;
    #line 87 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    PyObject* rng;
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    _rolloutreactor_gradients_t* _lf_gradients;
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    // width of -2 indicates that it is not a multiport.
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    int _lf_gradients_width;
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    // Default input (in case it does not get connected)
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    _rolloutreactor_gradients_t _lf_default__gradients;
    #line 82 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    _rolloutreactor_trajectories_t _lf_trajectories;
    #line 82 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    int _lf_trajectories_width;
    #line 89 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    reaction_t _lf__reaction_0;
    #line 98 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    reaction_t _lf__reaction_1;
    trigger_t _lf__startup;
    reaction_t* _lf__startup_reactions[1];
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    trigger_t _lf__gradients;
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    reaction_t* _lf__gradients_reactions[1];
    #ifdef FEDERATED
    
    #endif // FEDERATED
} _rolloutreactor_self_t;
_rolloutreactor_self_t* new__rolloutreactor();
#endif // _ROLLOUTREACTOR_H
